AĞ YAPILANDIRMA ARACI
Yazılım Ödevi


ÖĞRETİM ELEMANI: Dr. Öğr. Üyesi HASAN SERDAR
AD - SOYAD : Salih Akay
OKUL NUMARASI : 22370031031
SINIF : 3.Sınıf
DERS : Bilgisayar Ağları



Kaynaklar:
https://medium.com/three-arrows-security/scapy-nedir-ve-nas%C4%B1l-kullan%C4%B1l%C4%B1r-e2b1a264898a%20
https://medium.com/@aykutuludag/python-os-mod%C3%BCl%C3%BC-1e6eced93069%20github%20,
https://pypi.org/project/speedtest-cli/,
https://networkx.org/documentation/stable/tutorial.html%20
https://networkx.org/documentation/stable/tutorial.html,
https://matplotlib.org


• 1.Fonksiyonum ağ tarayıcı
İlk olarak ağ tarayıcı seçeneğini kullandım. Tarama yapmak için 192.168.1.1/24 IP aralığını girdim. Tarama sonucunda ağa bağlı cihazları aşağıdaki gibi çıktı.
•	IP Adresi: 192.168.1.1 - MAC Adresi: 00:11:22:33:44:55
•	IP Adresi: 192.168.1.2 - MAC Adresi: 00:11:22:33:44:66
•	IP Adresi: 192.168.1.3 - MAC Adresi: 00:11:22:33:44:77
 
• 2.Fonksiyonum Statik IP Atama
Daha sonra statik IP atama seçeneğini denedim. eth0 arayüzüne 192.168.1.100 IP adresini atadım şu mesajı aldım:
eth0 arayüzüne 192.168.1.100 statik IP atandı.
 
• 3.Fonksiyonum DNS Ayarları
DNS ayarlarını değiştirmek için üçüncü seçeneği kullandım. Yeni DNS sunucusu olarak 7.7.7.7 girdim ve şu mesajı aldım:
DNS sunucusu 7.7.7.7 olarak ayarlandı.
 
• 4.Fonksiyonum Ağ Hız Testi
Ağ hızımı test etmek için dördüncü seçeneği kullandım. İndirme ve yükleme hızlarım şu şekilde çıktı:
İndirme Hızı: 50.25 Mbps Yükleme Hızı: 10.75 Mbps
 
• 5.Fonksiyonum Ağ Görselleştir
Ağ görselleştirme seçeneğini kullanarak bulduğum cihazları görselleştirdim. Görselleştirdiğim cihazlar 192.168.1.1, 192.168.1.2 ve 192.168.1.3 idi. 
 
• 6.Fonksiyonum Ağ Durumunu Kontrol Et
Ağ arayüzü durumlarını kontrol ettim. eth0 arayüzümde IP adresim 192.168.1.100, wlan0 arayüzüm ise bağlı değildi. Çıktım şu şekilde oldu:
eth0: 192.168.1.100 wlan0: Bağlı Değil
 
• 7.Fonksiyonum Ağ Arayüzlerini Listele
Ağ arayüzlerimi listeledim. Mevcut ağ arayüzlerim 
•	eth0
•	wlan0
•	lo
 
• 8.Fonksiyonum  Çıkış
