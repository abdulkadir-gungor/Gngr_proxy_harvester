# Gngr_proxy_harvester
It checks the free proxy addresses it collects from websites and saves the working proxy addresses to the file.

"Gngr proxy harvester" - ücretsiz proxy toplayan ve kontrol eden bir uygulama örneğidir. "pyinstaller" ile derlenerek "exe" haline getirildikten sonra Python Scriptlerinde kullanmak üzere çalışan ücretsiz proxy adresleri elde edilebilir. https://www.youtube.com/watch?v=GAmMjMAJA8E adresinde örnek bir kullanıma ait video bulunmaktadır.

Kaynak kodun derlenmiş ('exe' uzantılı) dosya hali https://drive.google.com/file/d/14OBfxPVWVgYPob1qMB1Ba5O9aoejjGYJ/view?usp=sharing adresine konulmuştur.  Rar şifresi "Gngr-v1.0".

Program çalışması durumunda iki adet dosya üretir. "untrusted_proxy_list.txt" adlı dosya, web sitelerinden toplanan henüz kontrol edilmemiş proxy adreslerini içerir. "trusted_proxy_list.txt" adlı dosya da elde edilen proxy adreslerinin hem "http" hemde "https" olarak kontrol edilerek çalıştığı tespit edilmiş proxy adreslerini içerir. Kullanacağınız proxy adresleri "trusted_proxy_list.txt" adlı dosyadadır. "examples" adlı klasörünün içinde bulunan iki adet python script-i kullanıma örnek olması açısından verilmiştir.



Gereksinimler
--------------
Gerekli kütüphaneler: requests, pyinstaller

>> pip install requests

>> pip install pyinstaller

"pyinstaller" kodu tek parça çalıştırılabilir dosya haline getirmek için kullanılacak.



Kaynak Kodu Derlemek İçin
----------------------------
pyinstaller --onefile --icon=main.ico Gngr_proxy_harvester.py

Aşağıda PyCharm programı üzerinde nasıl derlendiği resim olarak gösterilmektedir.


[1]

![e1](https://user-images.githubusercontent.com/71177413/114309499-fe586800-9aef-11eb-8706-94a995bc96c5.JPG)



[2]

![e2](https://user-images.githubusercontent.com/71177413/114309508-0b755700-9af0-11eb-9f6f-7ef7d4f70d74.JPG)


[3]

![e3](https://user-images.githubusercontent.com/71177413/114309514-1203ce80-9af0-11eb-85e8-bae827799467.JPG)


[4]

![e4](https://user-images.githubusercontent.com/71177413/114309531-2647cb80-9af0-11eb-9261-f2f2eeb91d1d.JPG)


[5]

![e5](https://user-images.githubusercontent.com/71177413/114309542-2cd64300-9af0-11eb-99e7-a9716f2898fc.JPG)


[6]

![e6](https://user-images.githubusercontent.com/71177413/114309561-3eb7e600-9af0-11eb-8375-68e6c35592ee.JPG)



"examples" Adlı Klasör
----------------------
"examples" adlı klasörde "Gngr_proxy_harvester" programı ile  python scriptlerinin nasıl entegre kullanabileceği gösterilmektedir. Aşağıda beraber kullanıma ait resimler gösterilmektedir.  


[1]

![n3](https://user-images.githubusercontent.com/71177413/114309821-4330ce80-9af1-11eb-8bcb-536fd50bf0a0.jpg)



[2]

![n2](https://user-images.githubusercontent.com/71177413/114309830-49bf4600-9af1-11eb-9dde-941cab27daf5.jpg)


Önemli Not
----------------------
Program proxy adreslerini ücretsiz sitelerden toplamaktadır. Bu yüzden toplanan proxy adresleri birden fazla proxy çeşidine ait olabilir.


Yasal Uyarı
----------------
Eğitim amacıyla hazırlanmıştır.

Kullanıcıların bazı kullanım şekilleri suça sebep olabilir.

Olumsuz durumlarla karşılaşmamak için "Yasal_Uyarı.txt" dosyasını okuyunuz.
