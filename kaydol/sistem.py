import kayıtclass
import json_kontrol as jk

kullanıcıvt = jk.kullanıcıvt_oku()["kvt"]
if len(kullanıcıvt) != 0:
    for a in kullanıcıvt:
        kayıtclass.kayıtclass(a["ad"],a["soyad"],a["email"],a["şifre"],a["id"])

def giriş():
    while True:
        print("1.kaydol\n2.giriş yap\n[1,2]")
        cvp = str(input())
        if cvp == "1":
            return kayıtclass.kaydol()
        elif cvp =="2":
            return kayıtclass.giriş_yap()
        else:print("lütfen geçerli bir seçim yapın")

kullanıcı = giriş()

def kontrol_paneli():
    while True:
        print("işlemler:")
        print("1.anasayfayı görünüle\n2.gönderi gönder\n3.gönderi sil\n4.tüm gönderilerini görüntüle\nx.sistemi kapat\n[1,2,3,4,x]")
        cvp = str(input("işeminizi seçiniz: "))
        if cvp == "1":
            jk.anasayfayı_oku()
        elif cvp == "2":
            jk.gönderi_yayınla(kullanıcı)
        elif cvp == "3":
            jk.gönderi_kaldır(kullanıcı)
        elif cvp == "4":
            jk.bütün_gönderilerini_gör(kullanıcı)
        elif cvp == "x":
            print("oturum kapatılmıştır")
            break
        else:print("lütfen geçerili ibr seçim yapınız")

kontrol_paneli()





"onur turan"






