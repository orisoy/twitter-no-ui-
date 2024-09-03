import json
from random import choice
from os import chdir
from datetime import datetime

gönderi_idleri=[]

def gönderi_id_oluşturucu():
    with open("anasayfa.json","r") as dosya:
        veri0 = json.load(dosya)
        for gönderi in veri0["gönderiler"]:
            gönderi_idleri.append(gönderi["gönderi id"])
    while True:
        uid = choice(range(1000,10000000))
        if uid in gönderi_idleri:
            continue
        else : 
            return uid

def tarih_saat():
    şimdi = datetime.now()
    zmn = şimdi.strftime("%d,%m,%Y %H:%M")
    return zmn

chdir(r"C:\Users\Lenovo\OneDrive\Masaüstü\yazılım dnemeleri\kişişel projeler\kaydol")

def anasayfa_oku():
    with open("anasayfa.json","r") as dosya:
        return json.load(dosya)

def kullanıcıvt_oku():
    with open("kullanıcıvt.json","r") as dosya:
        return json.load(dosya)

def kullanıcı_ekle(hesap):
    kveri = kullanıcıvt_oku()
    eklenecek_hesap = {
        "ad":hesap.ad,
        "soyad":hesap.soyad,
        "email":hesap.email,
        "şifre":hesap.şifre,
        "id":hesap.id
    }
    kveri["kvt"].append(eklenecek_hesap)
    with open("kullanıcıvt.json","w") as dosya:
        json.dump(kveri,dosya,indent=4)


def anasayfayı_oku():
    veri0 = anasayfa_oku()
    kaynak = veri0["gönderiler"]
    sayı = 0
    tane = 5
    while True:
        gönderi = kaynak[sayı:sayı+tane]
        print(" ")
        for a in gönderi:
            print(f"{a["ad"]} {a["soyad"]}\n{a["gonderi"]}\n{a["tarih ve saat"]}\n ")
        print("< önceki sayfa,> sonraki sayfa,x ansayadan çık")
        print("[<,>,x]")
        cvp00 = input()
        if cvp00 == "<" :
            if sayı == 0:
                print("ilk sayfadasınız") 
            else:sayı -= tane
        if cvp00 == ">" :
            if sayı >= len(kaynak):
                print("son sayfadasınız") 
            else:sayı += tane
        if cvp00 == "x":
            print("anasayfadan çıktınız")
            break



def gönderi_yayınla(kullanıcı):
    veri1 = anasayfa_oku()
    while True:
        msj = input("lütfen göndermek istediğiniz gönderiyi yazınız: ")
        if len(msj) > 300:
            print("lütfen en fazla 300 karakter kullanın")
        else:break
    kayıt =  {
        "ad": kullanıcı.ad,
        "soyad": kullanıcı.soyad,
        "tarih ve saat": tarih_saat(),
        "gonderi": msj,
        "id": kullanıcı.id,
        "gönderi id":gönderi_id_oluşturucu()
        }
    
    veri1["gönderiler"].append(kayıt)
    with open("anasayfa.json","w") as dosya:
        json.dump(veri1,dosya,indent=4)

def bütün_gönderilerini_gör(kullanıcı):
    gönderi_listesi = []
    veri123 = anasayfa_oku()
    for gönderi in veri123["gönderiler"]:
        if kullanıcı.id == gönderi["id"]:
            gönderi_listesi.append(gönderi)
    print(" ")
    for a in gönderi_listesi:
        msj = f"{a["tarih ve saat"]}\ngönderi id: {a["gönderi id"]}\n{a["gonderi"]}\n "
        print(msj)
    return gönderi_listesi

def gönderi_kaldır(kullanıcı):
    veri01 = anasayfa_oku()
    hsp_gönderileri = bütün_gönderilerini_gör(kullanıcı)
    silinecek = input("silinmesi gereken gönderinin gönderi idsini griniz: ")
    msj_silindi = False
    for a in hsp_gönderileri:
        if int(silinecek) == a["gönderi id"]:
            print("gönderi başarıyla silinmiştir")
            veri01["gönderiler"].remove(a)
            with open("anasayfa.json","w") as dosya:
                json.dump(veri01,dosya,indent=4)
            msj_silindi = True
    if msj_silindi == False:
        print("gönderi bulunamadı")


"onur turan"

