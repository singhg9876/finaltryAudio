from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Record
from random import randrange
sample_text = ["ब्लॉगिंग Hindi Vs Hinglish या English किसी भाषा मे शुरुआत करें जिससे हम एक Successful Blogger बन सकें.", "आपको यह मालूम होना चाहिए कि गूगल ने कोई जानकारी नही दी गयी है की गूगल Hindi Vs Hinglish में कौन सी भाषा को सवश्रेष्ठ मानता हैं.", "इस विषय में हमने पता लगाया है की Hindi Vs Hinglish में से Blogging के लिए कौन सी भाषा सवश्रेष्ठ हैं.", "आज कल Hindi Blogging में Bloggers बहुत ही ज्यादा संख्या में Hindi Blog बना रहे है. क्यों की Google पर Hindi में सर्च करने वाले Visiter की संख्या भी 2013 से लगातार बढ़ रही है.", "50 करोड़ से भी ज्यादा लोग आज पूरी दुनिया में Hindi भाषा का ज्ञान रखते है. इससे यही सिद्ध होता है की Hindi भाषा में Blogging करना सही है.", "बस आपको Hindi Blogging की शुरुआत में अच्छी मेहनत करना है. आज हर कोई अपने Hindi Blogs को Google में Rank करना चाहता है और यह आसान भी नही है, क्यों की English Blogging के जैसे ही Hindi में Blogging करने पर Competition भी उतना High होने वाला है.","यदि आपको Hindi Language में Blog Post लिखने में आसानी होती है और आपको Hindi Blogging में रूचि है तो आपको Blogging हिंदी में करना चाहिए."]
size_of_sample_text = len(sample_text)
def record(request):
    if request.method == "POST":
        print("working till now 2")
        audio_file = request.FILES.get("recorded_audio")
        language = request.POST.get("language")
        record = Record.objects.create(language=language, voice_record=audio_file)
        print("working till now 2")
        record.save()
        messages.success(request, "Audio recording successfully added!")
        return JsonResponse(
            {
                "url": record.get_absolute_url(),
                "success": True,
            }
        )
    para = sample_text[randrange(size_of_sample_text)]    
    context = {"page_title": "Record audio", "para":para}
    return render(request, "core/record.html", context)


def record_detail(request, id):
    record = get_object_or_404(Record, id=id)
    context = {
        "page_title": "Recorded audio detail",
        "record": record,
    }
    return render(request, "core/record_detail.html", context)


def index(request):
    records = Record.objects.all()
    context = {"page_title": "Voice records", "records": records}
    return render(request, "core/index.html", context)
