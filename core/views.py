from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Record
from random import randrange
sample_text = ["ब्लॉगिंग Hindi Vs Hinglish या English किसी भाषा मे शुरुआत करें जिससे हम एक Successful Blogger बन सकें.", "आपको यह मालूम होना चाहिए कि गूगल ने कोई जानकारी नही दी गयी है की गूगल Hindi Vs Hinglish में कौन सी भाषा को सवश्रेष्ठ मानता हैं.", "इस विषय में हमने पता लगाया है की Hindi Vs Hinglish में से Blogging के लिए कौन सी भाषा सवश्रेष्ठ हैं.", "आज कल Hindi Blogging में Bloggers बहुत ही ज्यादा संख्या में Hindi Blog बना रहे है. क्यों की Google पर Hindi में सर्च करने वाले Visiter की संख्या भी 2013 से लगातार बढ़ रही है.", "50 करोड़ से भी ज्यादा लोग आज पूरी दुनिया में Hindi भाषा का ज्ञान रखते है. इससे यही सिद्ध होता है की Hindi भाषा में Blogging करना सही है.", "बस आपको Hindi Blogging की शुरुआत में अच्छी मेहनत करना है. आज हर कोई अपने Hindi Blogs को Google में Rank करना चाहता है और यह आसान भी नही है, क्यों की English Blogging के जैसे ही Hindi में Blogging करने पर Competition भी उतना High होने वाला है.","यदि आपको Hindi Language में Blog Post लिखने में आसानी होती है और आपको Hindi Blogging में रूचि है तो आपको Blogging हिंदी में करना चाहिए.","इस tutorial में हम impress window के भागों के बारे में सीखेंगे और कैसे स्लाइड इन्सर्ट करें और कॉपी करें फॉन्ट तथा फॉन्ट को फॉर्मेट करना सीखेंगे", "लिबर ऑफिस impress में एक प्रस्तुति document बनाना और बुनियादी formatting के इस spoken tutorial में आपका स्वागत है","यहाँ हम अपने ऑपरेटिंग सिस्टम के रूप में gnu/linux और लिबरऑफिस वर्जन 334 का उपयोग कर रहे हैं चलिए अपनी प्रस्तुति प्रेजैटेशन sample impress open करते हैं जिसे पिछले tutorial में बनाया था", "चलिए देखते हैं कि screen पर क्या क्या है मध्य में हम खाली जगह देखते है जोकि workspace है जहाँ हम काम करेंगे जैसे कि आप देख सकते हैं workspace में 5 tabs हैं जिन्हें view buttons कहते हैं", "फिलहाल normal टैब चुनित हैं यह मुख्य view है अलगअलग slides बनाने के लिए outline view प्रत्येक slide के outline format में विषय शीर्षक bulleted और क्रमांकित सूचियाँ बताता है" ," notes view प्रत्येक slide में notes जोड़ने की सुविधा देता है जोकि प्रस्तुतिकरण के वक्त नज़र नहीं the handout view slides को हैन्डाउट के रूप में print करने की सुविधा देता है", "यहाँ हमें एक पेज पर कितने slides print करने हैं इसका चुनाव कर सकते हैं slide sorter view slides की थम्बनेल बताता है अब फिर से normal view button पर click करते हैं", "screen की बाईं ओर आप slides pane देखते हैं यह प्रस्तुति में slides के थम्बनेल सम्मिलित करता है दाएँ तरफ tasks pane हैं जिसमें अनुभाग है लेआउट्स section में पहले से ही कुछ सैम्पल लेआउट्स मौजूद हैं", "हम उनका उपयोग ऐसे ही कर सकते हैं या आवश्यकता अनुसार कुछ बदलाव करके उपयोग कर सकते हैं जैसे जैसे हम इन tutorial में आगे बढ़ेंगे इन sections को विस्तार में देखेंगे""चलिए अब सीखते हैं कि कैसे slide को insert करें यानि जोड़ें slides pane में दूसरी slide पर क्लिक करके उसे चुनें अब insert और slide पर click करें हम देखते हैं कि दूसरी slide के बाद एक नई खाली slide जुड़ गई है",
"slide पर शीर्षक लिखने के लिए टेक्स्टबार में click to add title पर click करें अब short term strategy type करें और text box के बाहर click करें अतः शीर्षक इस तरह से जोड़ सकते हैं",
"यहाँ दो तरीके है जिससे हम slide की प्रतिलिपि डुप्लिकेट बना सकते हैं पहले तरीके को देखते हैं insert पर click करें और फिर duplicate slide पर click करें हम देख सकते हैं कि एक नई duplicate slide हमारी पहली बनाई गई slide के बाद जोड़ी गई है",
"या तो workspace pane में जाकर slide sorter क्लिक करके slide sorter view पर जाएँ अब सातवीं स्लाइड को कॉपी करें स्लाइड पर राइट क्लिक करें और कांटेक्स्ट मेन्यू से copy चुनें",
"आखरी स्लाइड पर राइट क्लिक करें paste पर क्लिक करें after चुनें और ok click करें प्रेसेंटेशन के अंत में आपने स्लाइड की एक कॉपी बना ली है चलिए अब फोंट्स और फोंट्स को फॉर्मेट करने के कुछ तरीके देखते हैं",
"long term goal नामक slide पर double क्लिक करके उसे चुनते हैं body टेक्स्ट बॉक्स पर क्लिक करें और पुरे टेक्स्ट को चुनें अब इसे डिलीट करें अब निम्न टाइप करें : reduce costs reduce dependence on few vendors develop customized applications","libreoffice writer documents में font का प्रकार और font size को जिस प्रकार बदला था यहाँ भी वैसे ही कर सकते हैं text की एक line चुनें text format टूलबार में font type को albany से arial black में बदलें",
"और font size को 32 से 40 में बदलें text box से बाहर कहीं भी click करें ध्यान दें कि font बदल गई है हम main menu से format पर क्लिक करके और फिर character option पर क्लिक करके भी font को बदल सकते हैं",
"यह एक डायलॉग बॉक्स खोलेगा जिसमें हम अपनी आवश्यकतानुसार फॉन्ट स्टाइल और साइज़ सेट कर सकते हैं इस डायलॉग बॉक्स को बंद करते हैं font का color बदलने के लिए हम development up to present नामक slide को चुनते हैं",
"body text box पर click करते हैं और फिर सारे text को चुनते हैं font color icon के पास में डाउन arrow पर click करें और जो चाहिए वो color चुनें text box के बाहर कहीं भी click करें",
"colour में हुए बदलाव को देखें libreoffice documents में जिस प्रकार से bold italics और underline जैसे formatting की थी यहाँ भी उसी प्रकार से कर सकते हैं",
"recommendations नामक slide को चुनें body text box पर click करें और text की एक line चुनें अब bold italics और underline icons पर click करें text box के बाहर कहीं भी click करें",
"संक्षिप्त में बताते हैं कि हमने क्या सीखा इस tutorial में हमने इम्प्रेस विंडो के भागों के बारे में सीखा और कैसे स्लाइड इन्सर्ट करें और कॉपी करें फॉन्ट to फॉन्ट को फॉर्मेट करना सीखा",
"इस व्यापक नियत कार्य की कोशिश करें एक नयी प्रस्तुति बनाए तीसरी और चौथी slide के बीच एक slide जोड़ें प्रस्तुति के अंत में चौथी स्लाइड की एक कॉपी बनाए",
"दूसरी स्लाइड में एक टेक्स्ट बॉक्स बनाए उसमें कुछ टेक्स्ट टाइप करें text के format को 32 font size में बदलें text को bold italic underlined करें और नीला रंग दें निम्न link पर उपलब्ध video देखें",
"यह spoken tutorial project को सारांशित करता है यदि आपके पास अच्छा bandwidth नहीं है तो आप इसे download करके देख सकते हैं spoken tutorial project team spoken tutorial का उपयोग करके कार्यशालाएँ भी चलाते हैं",
"जो online test pass करते हैं उनको प्रमाणपत्र भी देते हैं अधिक जानकारी के लिए कृपया हमें contact @spokentutorial org पर लिखें spoken tutorial project talktoateacher project का हिस्सा है",
"यह भारत सरकार के एमएचआरडी के आईसीटी के माध्यम से राष्ट्रीय साक्षरता mission द्वारा समर्थित है इस mission पर अधिक जानकारी के लिए उपलब्ध लिंक पर संपर्क करें",
"यह स्क्रिप्ट सकीना शेख द्वारा अनुवादित है आईआई टी बॉम्बे की ओर से मैं रवि कुमार अब आपसे विदा लेता हूँ हमसे जुड़ने के लिए धन्यवाद नमस्कार ! command line arguments पर spoken tutorial में आपका स्वागत है",
"इस tutorial में हम एक उदाहरण से arguments के साथ main function के बारे में सीखेंगे इस tutorial के लिए मैं उपयोग कर रही हूँ ubuntu operating system version 1110 और ubuntu पर gcc compiler version 461",
"इस tutorial के अनुसरण के लिए आपको c tutorials से परिचित होना चाहिए यदि नहीं तो सम्बंधित tutorials के लिए कृपया हमारी दर्शायी website पर जाएँ",
"अब अपना program शुरू करते हैं मेरे पास एक code file है मैं इसे खोलूँगी main hyphen with hyphen args c file का name है",
"अब मैं program को समझाती हूँ ये header files हैं stdio h core input और output functions को परिभाषित करता है stdlib h header file निम्न को परिभाषित करता है",
"यह हमारा main function है इसके अंदर हमने दो arguments passed किये हैं argc program को दिए गए command line arguments की संख्या को दिखाता है",
"यह program के वास्तविक name को सम्मिलित करता है argv index 0 से शुरू होने वाले वास्तविक arguments को रखता है index 0 उस program का name है",
"index 1 program को passed किया गया पहला argument होगा index 2 program को passed किया गया दूसरा argument होगा और आगे भी इसी प्रकार यह statement program को passed किये गए arguments की कुल संख्या को दिखायेगा",
"यह program को passed किये गए पहले argument को दिखायेगा 1 index 1 पर argument को दिखाता है while condition arguments की संख्या को घटाएगी",
"यह statement program को passed किये गए सारे arguments को print करेगा at में हमारे पास return 0 statement है अब अपने keyboard पर एक साथ ctrl + alt + t कीज़ दबाकर terminal खोलते हैं",
"type करें: gcc space main hyphen with hyphen args c space hyphen o space args enter दबाएं type करें: dot slash args enter दबाएं आप निम्न की तरह output देख सकते हैं:",
"command line arguments निष्पादन के दौरान दिए जाते हैं arguments की कुल संख्या 1 है क्योंकि zeroth arguments अपने आप में निष्पादन योग्य filename है पहला argument null है क्योंकि हमने program को कोई भी argument passed नहीं किया है",
"आर्ग्युमेंट्स केवल एक है जोकि dot slash args है अब दोबारा निष्पादन करते हैं अप arrow की दबाएं space type करें sunday space monday space tuesday enter दबाएंअब हम output देख सकते हैं: अब मैं output समझाती हूँ",
"arguments की कुल संख्या 4 है जैसे कि /args sunday monday और tuesday पहला argument sunday है zeroeth argument हमेशा निष्पादन योग्य file का name देता है sunday पहले argument को नियुक्त किया गया है",
"monday दूसरे argument को नियुक्त किया गया है tuesday तीसरे argument को नियुक्त किया गया है यह हमें इस tutorial के अंत में let है इसे सारांशित करते हैं इस tutorial में हमने निम्न करना सीखा कमांड लाइन आर्ग्युमेंट्सargcargv",
"नियत कार्य में भिन्न arguments के साथ program का निष्पादन करें नीचे दिए गए link पर उपलब्ध video देखें यह spoken tutorial project को सारांशित करता है अच्छी bandwidth न मिलने पर आप इसे download करके देख सकते हैं",
"spoken tutorial project team spoken tutorials का उपयोग करके कार्यशालाएं चलाती है online test pass करने वालों को प्रमाणपत्र details हैं अधिक जानकारी के लिए कृपया contact @spokentutorial org पर लिखें spoken tutorial project talk to a teacher project का हिस्सा है",
"यह भारत सरकार के it it आर डी के आई सी टी के माध्यम से राष्ट्रीय साक्षरता mission द्वारा समर्थित है इस mission पर अधिक जानकारी iit iit टी बॉम्बे से मैं श्रुति आर्य आपसे विदा लेती हूँ हमसे जुड़ने के लिए धन्यवाद",
"एक्सफिग के प्रयोग से फीडबैक डाइअग्रैम बनाने के इस मौखिक ट्यूटोरियल में आपका स्वागत है ब्लॉक डाइअग्रैम क्रीएशन के मौखिक ट्यूटोरियल में हमने यह डाइअग्रैम बनाया था हम इन्हें ब्लॉक्स ट्यूटोरियल कहेंगे कृपया इस ट्यूटोरियल को शुरू करने से पहले ब्लॉक्स ट्यूटोरियल को अच्छे से समझ ले",
"इस ट्यूटोरियल में हम समझाएंगे के इस पेज पर दिखाए गए इस तरह के ब्लॉक डाइअग्राम्स कैसे बनाए मैं एक्सफिग वर्ज़न 32 पैच लेवल 5 का इस्तेमाल करुँगी हम blockfig से शुरुआत करेंगे जोकी ब्लॉक्स ट्यूटोरियल में बनाए थे",
"एक्सफिग पर चलते है फाइल को चुनते है और फिर ओपन एंट्री बॉक्स में block को एन्टर करे और ओपन प्रेस करे या फिर blockfig पर डबल क्लिक करे file पर save as आप्शन का प्रयोग कर हम इस फिगर को feedback के नाम से सेव करते है",
"हमारे पास अब feedbackfig यह फाइल है grids पर क्लिक करके ग्रिड्स डालते है कैनवास को ऊपर या नीचे करने के लिए दाएँ तरफ स्क्रोल बार का प्रयोग करे प्रत्येक माउस बटन की भूमिका या कार्य ऊपर दाहिने तरफ दिखाया गया है",
"यह कार्य गतिविधि पर निर्भर होता है इसे उदाहरण देकर स्पष्ट करते है  मैं माउस को वर्टिकल scroll bar पर ले चलती हूँ",
"बाएं बटन के तरफ की टिप्पणी देखे मैं इसे बताने के लिए माउस को हटा नहीं सकती इसका कारण है बटंस का कार्य बदल जाएगा अगर मैं कर्सर स्क्रोल बार से दूर करू left button कैनवास को ऊपर ले जाएगा और right button उसे नीचे ले जाएगा",
"हम left या right बटन को क्लिक करने के बजाय centre button सेंटर बटन पर क्लिक कर सकते है तथा ड्रैग करके कैनवास को ऊपर या नीचे कर सकते है उसी तरह से आप ऊपर के स्क्रोल बार का प्रयोग करके कैनवास को राईट या लेफ्ट में ले जा सकते है",
"मैं अब middle buttonबीच के बटन पर क्लिक करके तथा कैनवास को पकड़कर और ड्रैग करके बॉक्स को बीच में याने सेंटर में  लाती  हूँ जैसे ही माउस को छोड़ देती हूँ  बॉक्स सेंटर में आ जाता है",
"चलिए अब इस ब्लॉक से शुरू करके हम अब फीडबैक डाइअग्रैम बनाते है इस बॉक्स को कॉपी करते है बॉक्स पर क्लिक करे और उसे चुने माउस को एक नई जगह ले जाए और क्लिक करे",
"अभी कुछ टेक्स्ट डालते है text box पर क्लिक करते है जो बाएं ओर के पैनल में t द्वारा बताया है टेक्स्ट का साइज़ चुनते है माउस को वाल्यू बॉक्स पर ले जाए और 16  एन्टर करे set पर क्लिक करे",
"अट्रिब्यूट पैनल में से  text just बटन पर क्लिक करे सेंटर अलाइन्मन्ट याने मध्य संरेखण को चुनते है पहले बॉक्स के सेंटर में क्लिक करते है ओह मैंने सही जगह नहीं चुनी है कर्सर को हटाने के लिए मैं दूसरी जगह पर क्लिक करती हूँ फिर मैं सही जगह पर क्लिक करुँगी",
"control यह टेक्स्ट अब टाइप कीजिये और माउस क्लिक करे अब हम एरो के साथ कुछ और लाइन्स एन्टर करना चाहते है polyline button पॉलीलाइन बटन को चुनते है अट्रिब्यूट पैनल में से  arrow mode बटन को चुनते है तथा दूसरे ऑप्शन को चुनते है",
"arrow type बटन तथा एक एरो हेड को क्लिक करते है एक पॉइंट पर क्लिक करते है जहाँ हम चाहते है के लाइन शुरू हो हमें जो लाइन चाहिए उसके आखिर में माउस को ले जाए अब बीच के माउस बटन से वहाँ क्लिक करते है एरो के साथ एक लाइन बनी है",
"मुझे एक सर्कल रखना है दाएँ ओर के पैनल से circle on the left को चुनते है हम उसे पहले बॉक्स के दाएँ तरफ रखेंगे माउस क्लिक करे जैसे ही मैं माउस को दूर ले जाती हूँ  सर्कल बड़ा हो जाता है जब हमें सही साइज़ मिल जाता है माउस को क्लिक करते है ओह जितना हम चाहते थे उससे बड़ा सर्कल है",
"मैं इसे ऊपर दिए एडिट बटन के प्रयोग से undo अन्डू कर सकती हूँ हम इस चीज़ को डिलीट भी कर सकते है  दाएँ ओर के पैनल में दिए delete बटन के प्रयोग से चलिए ऐसा करते है क्रोस हेयर्स के साथ एक ढांचा दिखाई पड़ता है",
"सभी चीजों याने ऑब्जेक्ट्स के की पोइंट्स भी दिखाई देते है क्रोस हेयर्स को की पॉइंट पर ले जाओ जोकी सर्कल बताता है और क्लिक करे",
"अगर कभी कोई चीज़ डिलीट हो जाती है चिंता करने की ज़रूरत नहीं आप उसे undo कर सकते है : edit बटन क्लिक करे  और वैसे ही माउस को क्लिक रखे हुए undo पर  ले जाए और फिर माउस को छोड़ दे",
"अगर कुछ ऑब्जेक्ट्स काफी नज़दीक है तो उन्हें चुनने में कठिनाई हो सकती है zoom फीचर की मदद से हम आसानी से ऑब्जेक्ट्स को चुन सकते है",
"बाएं ओर पर view  बटन को क्लिक करे  उसे पकडे रहे है और किसी भी एक ज़ूम ऑप्शन को चुने zoom to fit the canvas पर आकर माउस को छोड़ दे",
"अब चीजों के बीच विभेद करना आसान होगा मैं सर्कल को डिलीट करती हूँ मैं unzoom अनज़ूम करती हूँ स्क्रोल बटंस की मदद से मैं आकृति को मध्य में लती हूँ  मुझे  delete सिम्बल को ऑन रखना नहीं पसंद क्योंकि कभी गलती से कुछ डिलीट हो सकता है","मैं कोई भी दूसरा बटन चुनकर इसे बदल सकती हूँ मैं बाएं सर्कल को चुनती हूँ मैं दुबारा सर्कल बनाती हूँ मुझे इस लाइन से एक और लाइन डालनी है इसलिए पहले हम लाइन पर dotडॉट डालेंगे",
"बाएं ओर के पैनल से library लाइब्ररी पर क्लिक करे लाइब्ररी किताबो के देर द्वारा बताई गई है एक डाइअलॉग विंडो खुलेगा लाइब्ररी  के बगल में यह कहता है none loaded उस पर क्लिक करे और पकडे रखे उपलब्ध   ",
"लैब्ररीज़ की सूची दिखाई देगी माउस को लोजिक लाइब्ररी पर ले जाए और छोड़ दे small dot याने छोटे डॉट पर डबल क्लिक करके उसे चुने डाइअलॉग विंडो बंद होगा चुने हुए छोटे डॉट के साथ हमें क्रोस हेयर भी दिखता है क्लिक करके डॉट को लाइन पर रखते है",
"कर्सर और छोटा डॉट फिर से दिखाई पड़ता है और सुझाव देता है के हम उन्हें किसी और जगह भी रख सकते है हमें डॉट को किसी और जगह नहीं रखना माउस के राइट बटन से उसे क्लोज़ करते है राइट बटन अन्डू ऑपरेशन करता है इस केस में डॉट सेलेक्शन याने चुनाव हटा दिया गया है",
"चलिए इस डॉट से सर्कल तक एक लाइन बनाते है पॉलीलाइन को चुनते है पहले जो चुनाव हुए है वोह याद रखे गए है जैसे के arrow mode तथा  arrow type",
"एक सेशन में एक्सफिग पैरामीटर वाल्यूज़ को याद रखता हैडॉट पर क्लिक करे माउस को नीचे ले जाइए और क्लिक करे अब माउस को बाएं तरफ मोड़िए  जब तक सर्कल के आखिर तक नहीं पहुँचता क्लिक करे माउस को सर्कल पे ले जाए और अब माउस के बीच के बटन को क्लिक करे",
"सर्कल के बाएं तरफ एक और लाइन बनाते है एक्सफिग के उपरी बाएं कोने से फाइल बटन का प्रयोग करके तथा सेव को चुनकर इस फिगर को सेव करते है अब फाइल को एक्सपोर्ट करते है फाइल बटन को फिर से क्लिक करते है और एक्सपोर्ट को चुनते है",
"अब language और फिर pdf को चुनते है हमें feedbackpdf फाइल मिलती है open feedbackpdfइस कमांड से फाइल को ओपन करते है अब हमारे पास ब्लाक डाइअग्रैम है जैसा हम चाहते थे",
"हमने अपना उद्देश्य पूरा कर लिया है आपके लिए एक नियत कार्य है ब्लोक्स में अलग अलग चीज़े रखे रोटेट तथा फ्लिप जैसे अन्य ऑप्शंस की कोशिश करे feedbackfig फाइल को एडिटर में देखे तथा विभिन्न घटकों को पहचाने लाइब्ररी का इस्तेमाल कर अलग ब्लाक डाइग्राम्स बनाए",
"स्पोकेन ट्युटोरियल टोक टू टीचर  प्रोजेक्ट का हिस्सा है इसे  आई सी टी द्वारा नेशनल मिशन ओन एड्यूकेशन  एम् एच आर डी  भारत सरकार  से सहायता प्राप्त है",
"spokentutorialorg/nmeictintro  इस लिंक से यह मिशन के बारें में ज्यादा जानकारी प्राप्त की जा सकती है हम आपके सहयोग तथा आपकी प्रतिक्रिया का स्वागत करते है आई आई टी बॉम्बे की तरफ मैं सकीना अब आप से विदा लेती हूँ इस ट्यूटोरियल में शामिल होने के लिए धन्यवाद",
"लिबर ऑफिस impress में custom animation custom animation पर spoken tutorial में आपका स्वागत है इस tutorial में हम impress में custom animation के बारे में सीखेंगे",
"यहाँ हम अपने operating system के रूप में gnu/linux और libreoffice suite version 334 का उपयोग कर रहे हैं पहले प्रस्तुति sampleimpress odp खोलें",
"slides pane से potential alternatives थंबनेल पर click करें यह slide अब main main पर प्रदर्शित होती है अब सीखते हैं कि अपनी प्रस्तुति को अधिक आकर्षित बनाने के लिए custom animation का उपयोग कैसे करें slide में बायीं ओर के पहले text box को चुनें",
"यह करने के लिए text पर click करें और फिर दिखाई दे रहे border पर click करें impress window की दायीं ओर से tasks pane में custom animation पर click करें",
"add पर click करें custom animation dialog box प्रदर्शित होता है ध्यान दें कि entrance टैब खुलता है entrance टैब screen पर वस्तु के प्रदर्शन के तरीके को नियंत्रित करता है हम इस श्रृंखला के बाद के tutorials में अन्य tabs सीखेंगे",
"basic के नीचे diagonal squares चुनें आप गति को भी नियंत्रित कर सकते हैं जिस पर आपका animation प्रदर्शित होता है speed field में dropdown box पर click करें slow चुनें और ok पर click करें effect field आपको animations options set करने की अनुमति set है",
"effect field के the पर box animations प्रदर्शित करता है जो प्रस्तुति में जोड़े गये हैं ध्यान दें कि पहला animation animation की सूची में जोड़ दिया गया है",
"नीचे scroll करें और play पर click करें आपके द्वारा चुनित सभी animation का प्रिव्यू अब मुख्य main पर play होगा add slide में दूसरे text box को चुनें custom animation के नीचे add पर click करें custom animation dialog box में basic animation के नीचे wedge चुनें",
"गति को medium set करें ok पर click करें ध्यान दें कि यह animation box में जोड़ दिया गया है ध्यान दें कि सूची के animation क्रमबद्ध हैं जैसे आपने इन्हें बनाया है दूसरे animation को चुनें play button पर click करें",
"आप प्रिव्यू के लिए एक से भी अधिक animation चुन सकते हैं यह करने के लिए shift की पकड़कर रखें जब animation चुन रहे to play पर click करें आपके द्वारा चुनित सभी animations का प्रिव्यू play होता है add तीसरे text box को चुनें layouts में add पर click करें",
"entrance टैब में basic के नीचे diamond चुनें गति slow set करें ok पर click करें प्रत्येक animation कुछ default properties के साथ शुरू होता है आप change order buttons का उपयोग करके animation के क्रम को भी बदल सकते हैं",
"प्रत्येक animation के लिए default properties देखें और सीखें कि उनमें बदलाव कैसे करें सूची में पहले animation पर doubleclick करें यह diagonal squares option है",
"effects options dialog box प्रदर्शित होता है default रूप से effects टैब प्रदर्शित होता है settings में direction dropdown पर click करें और from right to top चुनें",
"इसमें प्रगति के रूप में दायें से animation की शुरूआत और शीर्ष की ओर स्थानांतरण के प्रभाव हैं dialog box को बंद करने के लिए ok पर click करें जिसे आपने जोड़ा है उस animation का निरीक्षण करने के लिए play button पर click करें",
"इस animation पर फिर से doubleclick करें effect options dialog box दिखाई देता है timing टैब पर click करें delay field में delay को 10 sec तक बढाएँ इसमें animation शुरूआत के प्रभाव एक सैकंड के बाद हैं ok पर click करें",
"अब पहले animation को चुनें play button पर click करें आप आपके द्वारा किये गये प्रभाव के बदलाव का निरीक्षण कर सकते हैं सूची में दूसरे animation पर doubleclick करें यह wedges option है जिसे हमने set किया",
"effects options dialog box प्रदर्शित होता है text animation टैब पर click करें text animation टैब text को एनिमेट करने के लिए कई options प्रदान करता है",
"group text field में by 1st level paragraphs चुनें यह चुनाव प्रत्येक bullet प्वॉइंट को अलगअलग प्रदर्शित करता है आप इस option का उपयोग कर सकते हैं जब आप दूसरे पर जाने से पहले एक बिंदु पर अच्छे से चर्चा करना चाहते हैं",
"ok पर click करें play पर click करें इस tutorial को रोकें और यह नियतकार्य करें विभिन्न animations बनाएँ और प्रत्येक animation के लिए effect options को check करें",
"अब हमारे द्वारा किये गये animation प्रभावों को देखना सीखते हैं slide show button पर click करें फिर animation को देखने के लिए screen पर कहीं भी click करें animation प्रस्तुति की नीरसता को तोड़ने और कुछ बिंदुओं को स्पष्ट करने के लिए अच्छा तरीका है जो अन्यथा समझाने के लिए कठिन हैं",
"फिर भी सावधान रहें इसका अधिक उपयोग न करें अधिक animation चर्चाधीन विषय से दर्शक का ध्यान दूसरी ओर ले जायेगा इसी के साथ हम इस tutorial की समाप्ति की ओर आ गये हैं",
"इस tutorial में हमने custom animation effect options के बारे में सीखा यहाँ आपके लिए एक नियतकार्य है तीन bullet प्वॉइंट्स के साथ एक text box बनाएँ text को एनिमेट करें जिससे कि text lineदरline दिखे",
"इस animation को play करें निम्न link पर उपलब्ध video देखें यह spoken tutorial project को सारांशित करता है यदि आपके पास अच्छा bandwidth नहीं है तो आप इसे download करके देख सकते हैं",
"spoken tutorial project team spoken tutorial का उपयोग करके कार्यशालाएँ भी चलाती है उनको प्रमाणपत्र भी देते हैं जो online test pass करते हैं अधिक जानकारी के लिए कृपया contact @spokentutorial org पर लिखें",
"spoken tutorial project talktoa teacher project का हिस्सा है यह भारत सरकार के एमएचआरडी के आईसीटी के माध्यम से राष्ट्रीय साक्षरता mission द्वारा समर्थित है",
"इस mission पर अधिक जानकारी दिए गए लिंक पर उपलब्ध है यह स्क्रिप्ट देवेन्द्र कैरवान द्वारा अनुवादित है आई आई टी मुंबई की ओर से मैं रवि कुमार अब आपसे विदा लेता हूँ हमसे जुड़ने के लिए धन्यवाद",
"गणित को एक्सफिग में अन्तः स्थापित कैसे करें इस विषय पर स्पोकेन ट्युटोरियल में आप का स्वागत है इस ट्युटोरियल में समझाएंगे के यह आकृति कैसे बनाएं दूसरे विभाग में मौजूद गणितिय उक्ति को देखे",
"इस ट्युटोरियल को समझने के बाद हम कोई भी गाणितिक उक्ति को अन्तः स्थापित कर सकते है एक्सफिग द्वारा फीडबैक डायग्राम कैसे बनाएं  इस स्पोकेन ट्युटोरियल में बनाई गयी इस आकृति से शुरुआत कर हम पिछली स्लाइड में मौजूद आकृति को भी बनाएँगे",
"हमें  एक्सफिग द्वारा फीड बेक डायग्राम कैसे बनाएं  इस ट्युटोरियल को वर्त्तमान ट्युटोरियल से पहले सीखना होगा इस ट्युटोरियल में समझाए गए विषयों के लिए  जिन चीजों की ज़रूरत है वह बताते है",
"मैं  एक्सफिग  वर्ज़न 32  पैच लेवल 5 का इस्तेमाल कर रही हूँ हमे लेटेक और उसकी सारी जानकारी होना ज़रूरी है हमें इमेज को क्रॉप याने काटने के लिए सोफ्टवेर की भी आवश्यकता हैंपिडीऍफ़ क्रोप लिनक्स और mac os x  पर चलता हैहम इसे इस  ट्युटोरियल में समझाएँगे",
"ब्रिस  विन्डोज़ पर चलता है लेकिन वह इस ट्युटोरियल में नहीं बताया गया है एक्सफिग पर जाते है फाइल का चुनाव करते है फिर ओपन सूचि को स्क्रोल करने पर  एक्सफिग द्वारा फीडबैक डायग्राम कैसे बनाएं  इस स्पोकेन ट्युटोरियल में मौजूद  feedbackfig  फाइल को देखेंगे",
"इसे क्लिक करते है इस बॉक्स में मौजूद आकृति को देखेंगे इसे ओपन करते है और इसे अन्दर ले आते है तथा ज़ूम करते है फाइल में मौजूद save as ऑप्शन का इस्तेमाल कर हम  मेथ्स maths नाम से इस आकृति को सेव करेंगेइसे सेव करते है",
"अब हमारे पास  मेथ्स  फिग  mathsfig  फाइल मौजूद है एडिट का चुनाव कर  प्लांट  टेक्स्ट को क्लिक करते हैमाउस को इधर लाकर इसे डिलीट करते है और एन्टर करते है  $gz = \frac z {z1} $",
"टाइपिंग करते वक़्त माउस बक्से के भीतर रहे इसका ख्याल रखना होगा फ्लेग की मौजूदा नोर्मल  वेल्यु को  स्पेशल  में बदलेंगे done पर क्लिक करते है टेक्स्ट लम्बा होने की वजह से वे दुसरे एन्ट्रीज़ के साथ ओवर्लाप होता है",
"चलिए टेक्स्ट को बॉक्स  के बहार लाकर  उस पर काम करते है मैं यहाँ क्लिक करती हूँ ग्रिड मोड़ का चुनाव करेंगे एक बार हमारी पसंद के फेरबदल करने के बाद हम टेक्स्ट को वापस बॉक्स के अन्दर रख सकते है",
"चलिए फाइल को सेव करेंगे  कमबाइनड पिडीऍफ़ एंड लेटेक फाइल्स  द्वारा इसे एक्सपोर्ट करते है फाइल    एक्सपोर्ट    कमबाइनड पिडीऍफ़ एंड लेटेक एक्सपोर्ट करते है मुझे  एक एरर मेसेज मिलता है चिंता की कोई आवश्यकता नहीं है टरमिनल पर जाते है",
"ls lrt टाइप करे हमें फाइल्स की सूची मिलेगी  जिस में सबसे नयी बनायीं गयी फाइल अंत में दिखाई जायेगी अंत की दो  फाइल्स  है mathspdf_t तथा mathspdf open mathspdf  यह कमांड देते है",
"इस को अन्दर ले आते हैं हम देख सकते है ब्लाक डाइअग्रैम को जोकि गणितिय उक्ति के बगैर है इसे बंद करते है इमेक्स एडिटर में हम mathspdf_t मेथ्स पिडीऍफ़_टी फाइल देख सकते है जोकि मैंने पहले ही ओपन की है ये यहाँ है इसे ओपन करते है",
"आपको  इमेक्स का इस्तेमाल नहीं करना है इस बात का ख्याल रखे जो भी एडिटर आप आसानी से काम कर सकते है उसका इस्तेमाल करे हम देख सकते हैं की  पिक्चर  परिवेश का इस्तेमाल हुआ है",
"यहाँ  इनक्लूड ग्राफिक्स  और  कलर  पॅकेजस का इस्तेमाल किया गया है इस आवश्यकता के बारे में हमें लेटेक को जानकारी देनी होगी mathsbptex   इस फाइल को ओपन करते है  जोकि इस ट्युटोरियल के लिए मैंने पहले से ही बनाया है मैने  आर्टिकल क्लास  का इस्तेमाल किया है",
"मैने  कलर  और  ग्राफिकएक्स  इन पॅकेजस का इस्तेमाल किया है क्योंकि इसका उपयोग  पिडीऍफ़_टी  pdf_t फाइल में किया गया है  जो हम पहले देख चुके है अंत में हमें  मेथ्सपिडीऍफ़_टी  mathspdf_t  का समावेश करना होगा",
"चलिए टर्मिनल पर pdflatex mathsbp कमांड को कार्यान्वित करते है mathsbppdf  बन चूका है ऐसा मेसेज हमें मिलता है open mathsbppdf कमांड के इस्तेमाल से इसे ओपन करते है हमारे पास अब आवश्यक फाइल मौजूद है इसे ज़ूम करते है",
"अब हम जानते है के गणितिय  उक्ति कार्यशील है  चलिए टेक्स्ट को अंदर ले आते है इसे सेव कर एक्सपोर्ट करते हैयह आवश्यक भाषा में पहले से मौजूद है",
"एक्सपोर्ट करे इस चेतावनी को रद्द करते है इस को पुनः संकलित करते है पिडीऍफ़ ब्राउसर को क्लिक करते है जहां फाइल मौजूद है अब हम बॉक्स के भीतर गणितिय  उक्ति को देख सकते है जो हमारी आवश्यकता के अनुरूप है",
"अगर  स्पेशल फ्लेग  का चुनाव न हो तो देखते है आगे क्या होता है चलो हम यहाँ आते है टेक्स्ट को एडिट करती हूँ   स्पेशियल फ्लैग  को  नोर्मल  में परिवर्तित करते है यह हो गया है फाइल को सेव कर इसे एक्सपोर्ट करेंगे",
"संकलन करते है  यहाँ आते है फोर्मुला आवश्यक रूप में नहीं है स्पेशियल फ्लैग  को फिर से  स्पेशियल  में परिवर्तित करेंगे फाइल को सेव कर इसे एक्सपोर्ट करे",
"पुनः संकलन करेंगेफाइल आवश्यक रूप में है इस की जांच करेंगे अब इस फोर्मुला की दिखावट में सुधार लाते है इस उदहारण में dfrac  फ्रैक्शन को बेहतर बनाने में हमारी मदद करेगा",
"इस विषय में हम frac को dfrac  में बदलेंगे मैं यहाँ क्लिक करती हूँ और माउस को बॉक्स के अन्दर रखती हूँ  d  को यहाँ रखेंगे यह हो गया है फाइल को सेव कर इसे एक्सपोर्ट करेंगे",
"पिडीऍफ़ लेटेक  का इस्तेमाल कर इसे संकलित करते है undefined control sequence \dfrac  अपरिभाषित नियंत्रण अनुक्रम  \ डीफ्रेक यह ऐरर मेसेज मिलता है \ dfrac कमांड amsmath पॅकेज में परिभाषित है परन्तु हमने उसे समाविष्ट नहीं किया  इसी वजह से लेटेक ऐरर देता है हमें इसे mathsbptex फाइल में समाविष्ट करना होगा",
"चलिए इसे करते है इमेक्स पर जाते है एन्टर करे फाइल सेव करे इसे फिर संकलित करे पहले एक्सिट याने बाहर आते है इसे पुनः संकलित करेंगे अब यह संकलित हो रहा है",
"इसे क्लिक करते है हम देख सकते है की फ्रैक्शन अब अच्छी तरह से बनकर आया है गाणितिय उक्ति एक्सफिग में कैसे अंत : स्थापित करे  इस उद्देश्य को हमने प्राप्त किया",
"एक्सफिग लेटेक कमांड्स को समझ नहीं सकता   यह बात हमें ध्यान में रखनी है पिडीऍफ़ लेटेक कमांड इसकी व्याख्या कर पाएगा संकलन के समय लेटेक कमांड्स का सही और सुसंगत होना जरूरी है",
"अब  मैं आकृति के आसपास खाली जगहों को कैसे निकालना यह समझाऊँगी टर्मिनल पर  जाते है pdfcrop mathsbppdf कमांड टाइप करे इस फाइल को मैंने mathsoutpdf फाइल में बनाया था pdfcrop पिडीऍफ़क्रोप हमें सन्देश देगा  एक पृष्ट लिखा गया है",
" पिडीऍफ़क्रोप  फाइल को स्वीकार कर  आकृति के पास की खाली जगहों को निकाल कर  क्रोप्ड फाइल को आउट पुट फाइल में परिवर्तित करता है  पिडीऍफ़क्रोप  की संस्थापना मेरे कोम्प्यूटर पर  पहले से की गयी है अगर यह मौजूद नहीं है  तो इस की संस्थापना करनी होगी",
"open mathsoutpdf इस कमांड से हम आउट पुट फाइल को देखते है इसे अन्दर ले आते हैआकृति अब बहुत छोटी बन गयी है खाली जगह जो यहाँ थी उसको निकाला जा चूका है अब इसे हम डाक्यूमेंट्स में डाल सकते है इसे बंद करते है और इसे भी स्लाइड्स पर वापस आते है",
"briss ब्रिस सॉफ्टवेर खाली जगहों को क्रॉप याने काटने में हमारी मदद करेगा ब्रिस सॉफ्टवेर  लिनक्स  mac os x तथा विन्डोज़ पर भी चलता है मैंने  mac os x  पर इसको चला के परखा है परन्तु हम इसे यहाँ पर प्रदर्शित नहीं करेंगे",
"अब हम ट्युटोरियल के अंत में आ चुके है हमारे पास आप के लिए नियत कार्य है इस ट्युटोरियल में बनायीं गयी आकृति को ज्यादा सुन्दर और संतुलित बनाना होगा अलग अलग गणितिय उक्तियों को जाचेंगे",
"फ्लिप  और  रोटेट  जैसे दुसरे विकल्पों को भी जाचेंगे इसका उल्लेख ट्युटोरियल में आपको नहीं मिलेगा अलग अलग आकृतियाँ बनाने की कोशिश करें लाइब्रेरी  का अन्वेषण करें इंटरनेट पर एक्सफिग के विषय में जानकारी ढूंढे",
"अभ्यास करने के लिए उपयोगी जानकारी  spokentutorialorg  पर उपलब्ध है स्पोकेन ट्युटोरियल की संकल्पना  what is a spoken tutorial में समझाई गई है",
"आप लेटेक का अभ्यास उपलब्ध स्पोकेन ट्यूटोरियल्स में से कर सकते है  मैंने इसे अलग टेब में डाऊनलोड किया है mathematical typesetting  गणितिय टाइप सेटिंग  यह ट्युटोरियल लेटेक में मेथ कैसे बनायें  इस बारे में जानकारी देगा",
"टेबल्स और फिगर्स  यह ट्युटोरियल  आकृति जैसे इस ट्युटोरियल में बनायीं गयी है डाक्यूमेंट्स में कैसे नियुक्त करें  इस बारे में जानकारी देगा यह वेब साईट पर एक्सफिग ट्यूटोरियल्स और अन्य विषयों के बारें में काफी जानकारी  मिलेगी स्लाइड्स पर वापस आते है",
"स्पोकेन ट्युटोरियल   टोक टू टीचर  प्रोजेक्ट का हिस्सा है इसे  आई सी टी द्वारा नेशनल मिशन ओन एड्यूकेशन  एम् एच आर डी  भारत सरकार  से सहायता प्राप्त है",
"spokentutorialorg/nmeictintro  इस लिंक से यह मिशन के बारें में ज्यादा जानकारी प्राप्त की जा सकती है हम आपके सहयोग तथा आपकी प्रतिक्रिया का स्वागत करते है",
"आई आई टी बॉम्बे की तरफ मैं सकीना अब आप से विदा लेती हूँ इस ट्यूटोरियल में शामिल होने के लिए धन्यवाद thunderbird  का उपयोग कैसे करें इस स्पोकन ट्यूटोरियल में आपका स्वागत है",
"इस tutorial में हम सीखेंगे कि: launcher में thunderbird  शॉर्टकट कैसे जोड़ें messages को टैग कैसे करें तीव्र बटलाव कैसे करें और मैसेजेस को श्रेणीबद्ध और क्रमबद्ध कैसे करें",
"हम यह भी सीखेंगे : save as और print messages फाइल अटैच करना अकाईव मैसेजेसarchive messages activity manager देखना",
"यहाँ हम उबंटू 1204 में मौजिला थंडरबर्ड 1301  का उपयोग कर रहे हैं जैसा कि हम thunderbird का अक्सर उपयोग करते हैं इसके लिए शॉर्टकट आइकन बनाएँ अब thunderbird  शॉर्टकट आइकन को launcher पर ड्रैग और ड्रॉप करें",
"पहले dash home पर क्लिक करें सर्च फील्ड में thunderbird  टाइप करें सर्च फील्ड के नीचे thunderbird  आइकन दिखाई देता है इसे चुनें और बायें माउस बटन को न छोड़ें अब आइकन को launcher  पर ड्रैग और ड्रॉप करें और बायें माउस बटन को छोड़ दें",
"इसे बंद करने के लिए dash home पर क्लिक करें launcher में thunderbird  आइकन पर क्लिक करें thunderbird विंडो खुलती है",
"gmail dot com आईडी पर  stuserone नीचे  inbox पर क्लिक करें ध्यान दें कि कुछ मैसेजेस बोल्ड हैं ये अपठित मैसेजेस हैं get mail आइकन पर क्लिक करें और get all new messages चुनें",
"हमें जीमेल अकाउंट से मैसेसेज प्राप्त हुए हैं मानिए कि हम इन मैसेजेस को sender द्वारा श्रेणीबद्ध करते हैं कॉलम हैडिंग from पर क्लिक करें मैसेजेस अब एक वर्णानुक्रमी क्रम में श्रेणीबद्ध हो गये हैं",
"from पर फिर से क्लिक करें अब मैसेजेस विपरीत वर्णानुक्रमी क्रम में श्रेणीबद्ध हो गये हैं अबsubject द्वारा श्रेणीबद्ध करें subject पर क्लिक करें अब मैसेजेस subject द्वारा श्रेणीबद्ध हो गये हैं",
"इस ट्यूटोरियल को रोकें और इस नियतकार्य को करने की कोशिश करें date received द्वारा मैसेसेज को श्रेणीबद्ध करें आप मैसेजेस को टैग भी कर सकते हैं इस तरह से आप आसानी से पता कर सकते हैं जिन मैसेजेस को आप फिर से खोलना चाहते हैं",
"आप समान मैसेजेस को एक साथ इकट्ठा करने के लिए भी टैग्स का उपयोग कर सकते हैं अब मानते हैं कि आप एक मेल को महत्वपूर्ण के रूप में टैग करना चाहते हैं inbox पर क्लिक करें पहले मेल को चुनें",
"टूलबार से tag आइकन पर क्लिक करें और important चुनें ध्यान दें कि वह मेल लालरंग में प्रदर्शित होता है निचले पैनल पर देखें मेल महत्वपूर्ण के रूप में टैग हो गया है टैग को हटाने के लिए पहले mail चुनें",
"टूलबार में tag आइकन पर क्लिक करें और फिर से important पर क्लिक करें इनबॉक्स में पहले मेल को important के रूप में और दूसरे मेल को work के रूप में टैग करें यदि हम केवल उन मेल्स को देखना चाहते हैं जो कि राइट पैनल में टैग किये गये हैं",
"क्या यह करना संभव होगा आप तीव्र बदलाव और मैसेसेज को देखने के लिए quick filter टूलबार का उपयोग कर सकते हैं टैग किये गये मैसेसेज को देखने के लिए quick filter टूलबार में tagged  आइकन पर क्लिक करें",
"केवल हमारे द्वारा टैग किये मैसेजेस प्रदर्शित होते हैं अब tagged आइकन पर फिर से क्लिक करें अब हम सभी मेल्स देख सकते हैं अब मैसेज threads  के बारे में सीखते हैं मैसेज threads क्या हैं संबंधित मैसेज जो क्रम या वार्तालाप के रूप में प्रदर्शित होते हैं",
"मैसेज threads  कहलाते हैं हम मैसेज threads का उपयोग एक सतत प्रवाह में एक पूरी वार्तालाप के रूप में संबंधित मैसेसेज को देखने के लिए करते हैं अब सीखते हैं कि यह कैसे करें",
"message threads आइकन को प्रदर्शित करने के लिए इनबॉक्स के बायें कोने में क्लिक करें मेल्स वार्तालाप के रूप में प्रदर्शित होते हैं पूर्ण वार्तालाप देखने के लिए corresponding thread के आगे threading symbol पर क्लिक करें",
"पूर्ण वार्तालाप मैसेज प्रिव्यू पैनल में दिखाई देता है thread व्यू से बाहर आने के लिए केवल thread आइकन पर फिर से क्लिक करें अब सीखते हैं कि मेल को फोल्डर में सेव और फिर प्रिंट कैसे करें",
"इस ट्यूटोरियल के प्रयोजन के लिए: हमने डेस्क्टॉप पर एक नया फोल्डर बनाया है और इसे saved mails नाम दिया है पहला मेल चुनें और सेव करें मेल पर डबलक्लिक करें",
"यह अलग टैब में खुलता है toolbar से file save as और file पर क्लिक करें save message as डायलॉग बॉक्स प्रदर्शित होता है डेस्क्टॉप के लिए ब्राउज करें और फोल्डर saved mails चुनें save पर क्लिक करें",
"मैसेज फोल्डर में सेव हो गया है saved mails फोल्डर पर जाएँ इस पर डबलक्लिक करें और इसे खोलें मेल gedit  में टेक्स्ट फाइल के रूप में खुलता है बंद करें और इस फाइल से बाहर निकलें",
"आप template  के रूप में भी मैसेज सेव कर सकते हैं टूलबार से file save as और templates पर क्लिक करें मैसेज थंडरबर्ड में templates फोल्डर में सेव होता है thunderbird दायें पैनल में templates फोल्डर पर क्लिक करेंमेल चुनें और डबलक्लिक करें",
"यह मूल मेल में सूचीबद्ध संपर्क से पूरित to एड्रैस फील्ड के साथ अलग टैब में खुलता है आप अब इस मेल में कंटेंट में बदलाव कर सकते हैं संपर्क जोड़ें या डिलीट करें और इसे भेजें सब्जेक्ट में 1 जोड़ें",
"template को बंद करने के लिए टैब के ऊपर बायें कोने पर  x आइकन पर क्लिक करें save message डायलॉग बॉक्स प्रदर्शित होता है dont save पर क्लिक करें अब मैसेज को प्रिन्ट करें",
"inbox पर क्लिक करें और दायें पैनल से दूसरा मेल चुनें और इस पर डबलक्लिक करें यह नये टैब में खुलता है मुख्य मेन्यू में file पर जाएँ और फिर print चुनें print डायलॉग बॉक्स प्रदर्शित होता है",
"हम इस मेल को छायाचित्र के रूप में orientation के साथ एक a4 शीट पर प्रिन्ट करेंगे और इस मेल की दो कॉपी बनायेंगे page setup टैब पर क्लिक करें paper size फील्ड में ड्रॉपडाउन सूची पर क्लिक करें और a4 चुनें",
"orientation फील्ड में  ड्रॉपडाउन सूची पर क्लिक करें और portrait चुनें अब general टैब पर क्लिक करें copies फील्ड में 2 प्रविष्ट करें print पर क्लिक करें यदि आपका प्रिंटर सही कंफिगर है तो मेल अब प्रिंट करना शुरू करना चाहिए",
"print डायलॉग बॉक्स से बाहर आने के लिए cancel पर क्लिक करें mail टैब को भी बंद करें अब याहू अकाऊंट पर संलग्नattachment के रूप में विडियो भेजें",]
size_of_sample_text = len(sample_text)
# def record(request):
#     if request.method == "POST":
#         print("working till now 2")
#         audio_file = request.FILES.get("recorded_audio")
#         language = request.POST.get("language")
#         record = Record.objects.create(language=language, voice_record=audio_file)
#         print("working till now 2")
#         record.save()
#         messages.success(request, "Audio recording successfully added!")
#         return JsonResponse(
#             {
#                 "url": record.get_absolute_url(),
#                 "success": True,
#             }
#         )
#     para = sample_text[randrange(size_of_sample_text)]    
#     context = {"page_title": "Record audio", "para":para}
#     return render(request, "core/record.html", context)

def record(request):
    if request.method == "POST":
        audio_file = request.FILES.get("recorded_audio")
        record = Record.objects.create(name=request.POST.get("name"),gender = request.POST.get("gender"),native_language= request.POST.get("Mother_Tongue"),age= request.POST.get("age"), state= request.POST.get("native_state"), proficiency= request.POST.get("Proficiency"), voice_record=audio_file)
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
