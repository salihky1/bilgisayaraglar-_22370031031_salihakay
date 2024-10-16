from scapy.all import ARP, Ether, srp, get_if_addr, conf
import os
import speedtest
import networkx as nx
import matplotlib.pyplot as plt


def ag_tarama(aralik):
    arp_istek = ARP(pdst=aralik)
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    paket = ether_frame / arp_istek
    sonuc = srp(paket, timeout=2, verbose=False)[0]
    cihazlar = []
    for gonderilen, alinan in sonuc:
        cihazlar.append({'ip': alinan.psrc, 'mac': alinan.hwsrc})
    return cihazlar


def cihazlari_goster(cihazlar):
    print("Ağa Bağlı Cihazlar:")
    print("IP Adresi\t\tMAC Adresi")
    print("-" * 40)
    for cihaz in cihazlar:
        print(f"{cihaz['ip']}\t\t{cihaz['mac']}")


def statik_ip_atama(arayuz, ip):
    os.system(f"sudo ifconfig {arayuz} {ip} netmask 255.255.255.0")
    print(f"{arayuz} arayüzüne {ip} statik IP atandı.")


def dns_ayarlarini_yap(dns):
    with open('/etc/resolv.conf', 'w') as dosya:
        dosya.write(f"nameserver {dns}\n")
    print(f"DNS sunucusu {dns} olarak ayarlandı.")


def ag_hizi_testi():
    tester = speedtest.Speedtest()
    print("İndirme Hızı: ", tester.download() / 1_000_000, "Mbps")
    print("Yükleme Hızı: ", tester.upload() / 1_000_000, "Mbps")


def agi_gorsellestir(cihazlar):
    grafik = nx.Graph()
    for cihaz in cihazlar:
        grafik.add_node(cihaz['ip'])
    for i in range(len(cihazlar) - 1):
        grafik.add_edge(cihazlar[i]['ip'], cihazlar[i + 1]['ip'])
    nx.draw(grafik, with_labels=True)
    plt.show()


def ag_durumunu_kontrol_et():
    print("Ağ Arayüz Durumları:")
    for arayuz in conf.ifaces:
        ip_adresi = get_if_addr(arayuz)
        print(f"{arayuz}: {ip_adresi if ip_adresi else 'Bağlı Değil'}")


def arayuzleri_listele():
    print("Mevcut Ağ Arayüzleri:")
    for arayuz in conf.ifaces:
        print(arayuz)


if __name__ == "__main__":
    while True:
        print("\nAğ Yapılandırma Aracı")
        print("1. Ağ Tarayıcı")
        print("2. Statik IP Atama")
        print("3. DNS Ayarları")
        print("4. Ağ Hız Testi")
        print("5. Ağ Görselleştir")
        print("6. Ağ Durumunu Kontrol Et")
        print("7. Ağ Arayüzlerini Listele")
        print("8. Çıkış")

        secim = input("Bir seçenek girin: ")

        if secim == "1":
            ip_araligi = input("Tarama yapılacak IP aralığını girin (örn: 192.168.1.1/24): ")
            bulunan_ciHazlar = ag_tarama(ip_araligi)
            cihazlari_goster(bulunan_ciHazlar)
        elif secim == "2":
            arayuz_adi = input("Arayüz ismini girin (örn: eth0): ")
            ip_adresi = input("Atanacak IP adresini girin: ")
            statik_ip_atama(arayuz_adi, ip_adresi)
        elif secim == "3":
            dns_sunucusu = input("Yeni DNS sunucusunu girin: ")
            dns_ayarlarini_yap(dns_sunucusu)
        elif secim == "4":
            ag_hizi_testi()
        elif secim == "5":
            bulunan_ciHazlar = ag_tarama("192.168.1.1/24")
            agi_gorsellestir(bulunan_ciHazlar)
        elif secim == "6":
            ag_durumunu_kontrol_et()
        elif secim == "7":
            arayuzleri_listele()
        elif secim == "8":
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
