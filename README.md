AĞ YAPILANDIRMA ARACI Yazılım Çıktı Raporu
ÖĞRETİM ELEMANI: Dr. Öğr. Üyesi HASAN SERDAR
AD - SOYAD: Salih Akay
OKUL NUMARASI: 22370031031
SINIF: 3. Sınıf
DERS: Bilgisayar Ağları

1. Proje Tanımı
Bu proje, kullanıcıların ağ yönetimini ve yapılandırmasını kolaylaştırmak amacıyla tasarlanmış bir ağ yapılandırma aracıdır. Araç, çeşitli ağ yönetim fonksiyonları sunarak kullanıcıların ağ kaynaklarını daha etkin bir şekilde yönetmelerine yardımcı olur.

2. Kullanılan Teknolojiler
Python: Ağ ile etkileşim sağlayan ve veri işleme için kullanıldı.
Scapy: Ağ taraması ve paket analizi için kullanıldı.
NetworkX: Ağ yapılarının analizi ve görselleştirilmesi için kullanıldı.
Matplotlib: Veri görselleştirme ve grafiksel temsil için kullanıldı.
Speedtest-cli: İnternet hız testi için kullanıldı.
3. Fonksiyonlar ve Çıktıları
3.1. Ağ Tarayıcı

Açıklama: Belirli bir IP aralığında tarama yaparak ağa bağlı cihazların bilgilerini toplar.

Örnek Çıktı:

IP Adresi: 192.168.1.1 - MAC Adresi: 00:11:22:33:44:55
IP Adresi: 192.168.1.2 - MAC Adresi: 00:11:22:33:44:66
IP Adresi: 192.168.1.3 - MAC Adresi: 00:11:22:33:44:77
3.2. Statik IP Atama

Açıklama: Kullanıcıların belirli bir ağ arayüzüne statik IP adresi atamalarını sağlar.

Mesaj: eth0 arayüzüne 192.168.1.100 statik IP atandı.

3.3. DNS Ayarları

Açıklama: Kullanıcıların ağ üzerindeki DNS ayarlarını değiştirmelerine olanak tanır.

Mesaj: DNS sunucusu 7.7.7.7 olarak ayarlandı.

3.4. Ağ Hız Testi

Açıklama: Kullanıcının internet hızını ölçerek mevcut bağlantı performansını değerlendirir.

Test Sonuçları:

İndirme Hızı: 50.25 Mbps
Yükleme Hızı: 10.75 Mbps
3.5. Ağ Görselleştir

Açıklama: Ağa bağlı cihazları grafiksel bir formatta temsil eder.

Görselleştirilen Cihazlar:

192.168.1.1
192.168.1.2
192.168.1.3
3.6. Ağ Durumunu Kontrol Et

Açıklama: Ağ arayüzlerinin durumunu kontrol eder.

Kontrol Sonuçları:

eth0: 192.168.1.100
wlan0: Bağlı Değil
3.7. Ağ Arayüzlerini Listele

Açıklama: Mevcut ağ arayüzlerini görüntüler.

Mevcut Ağ Arayüzleri:

eth0
wlan0
lo
3.8. Çıkış

Açıklama: Kullanıcıların uygulamadan güvenli bir şekilde çıkmalarını sağlar.

4. Uygulamanın Geliştirilmesi
Geliştirilen ağ yapılandırma aracı, ağ yönetimi konusundaki bilgileri pekiştirmiştir. Araç, kullanıcıların ağ taraması, statik IP ataması, DNS ayarları, ağ hızı testi gibi önemli ağ yönetim fonksiyonlarını gerçekleştirerek kullanıcı deneyimini artırmaktadır.

4.1. Geliştirme Süreci

Proje, Python programlama dili ve ilgili kütüphaneler kullanılarak geliştirilmiştir.
Proje sürecinde karşılaşılan zorluklar, özellikle ağ taraması ve veri toplama aşamalarında optimize edilmiştir.
4.2. Gelecek Çalışmalar

Otomasyon: Belirli ağ görevlerini otomatikleştirmek için zamanlama ve otomasyon özellikleri eklenmesi.
Kullanıcı Arayüzü: Daha kullanıcı dostu bir grafik arayüz tasarlanması.
Gelişmiş İzleme: Ağ trafiğini ve performansını gerçek zamanlı olarak izleyen ek özellikler eklenmesi.
Güvenlik: Ağ güvenliği ile ilgili daha fazla özellik ekleyerek, kullanıcıların ağlarını daha güvenli hale getirmelerine yardımcı olunması.
5. Sonuç
Geliştirilen ağ yapılandırma aracı, kullanıcıların ağa bağlı cihazları yönetmelerine, ağ ayarlarını yapılandırmalarına ve ağ hızlarını test etmelerine olanak tanımaktadır. Proje, ağ yönetimi konusunda derinlemesine bilgi edinme fırsatı sunmuş ve daha karmaşık ağ sistemlerinin yönetiminde gerekli olan temelleri atmıştır. Bu araç, kullanıcıların ağ yapılandırmalarını optimize etmeleri ve ağ kaynaklarını daha verimli kullanmaları için önemli bir katkı sağlamaktadır.

6. Ekler
Proje ile ilgili kod örnekleri, grafikler ve diğer ilgili belgeler eklenebilir.

Not: Bu rapor, ağ yapılandırma aracı ile ilgili tüm bilgileri ve çıktıları kapsamaktadır. Herhangi bir ek bilgi veya açıklama gerektiğinde lütfen benimle iletişime geçin.
