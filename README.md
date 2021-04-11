# Gngr_proxy_harvester
It checks the free proxy addresses it collects from websites and saves the working proxy addresses to the file.

"Gngr proxy harvester" - ücretsiz proxy toplayan ve kontrol eden bir uygulama örneğidir. "pyinstaller" ile derlenerek "exe" haline getirildikten sonra Python Scriptlerinde kullanmak üzere çalışan ücretsiz proxy adresleri elde edebilir. https://www.youtube.com/watch?v=GAmMjMAJA8E adresinde örnek bir kullanım şeklinin videosu bulunmaktadır.

Kaynak kodun derlenmiş ('exe' uzantılı) dosya hali https://drive.google.com/file/d/14OBfxPVWVgYPob1qMB1Ba5O9aoejjGYJ/view?usp=sharing adresine konulmuştur.  Rar şifresi "Gngr-v1.0".

Program çalışması durumunda iki adet dosya üretir. "untrusted_proxy_list.txt" adlı dosya, web sitelerinden toplanan henüz kontrol edilmemiş proxy adreslerini içerir. "trusted_proxy_list.txt" adlı dosya da elde edilen proxy adreslerinin hem "http" hemde "https" olarak kontrol edilerek çalıştığı tespit edilmiş proxy adreslerini içerir. Kullancağınız proxy adresleri "trusted_proxy_list.txt" adlı dosyadadır. "examples" adlı klasörünün içinde bulunan iki adet python script-i kullanıma örnek olması açısından verilmiştir.


