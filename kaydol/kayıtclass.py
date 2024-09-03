from random import choice
import json_kontrol as jk
import json

kullanıcılar = {}
kullanıcılaremail = {}
id_liste = []
girişvt = {}

class kayıtclass():
    
    def __init__(self,ad,soyad,email,şifre,id):
        self.ad = ad
        self.soyad = soyad
        self.email = email
        self.şifre = şifre
        self.id = id
        id_liste.append(self.id)
        kullanıcılar[self.id] = self
        for a in kullanıcılar.values():
            girişvt[a.email] = a




def id_oluşturucu():
    while True:
        uid = choice(range(100000,1000000))
        if uid in id_liste:
            continue
        else : 
            return uid
        
def kaydol():
    while True: 
        email = str(input("eposta adresinizi giriniz: "))
        if "@" not in email or "." not in email:
            print("eposta adresi geçersiz")
        elif email in girişvt.keys(): 
            print("aynı email sistemde bulunuyor")
            print("yoksa giriş yapmak istermisiniz [y.n]")
            cevap = str(input())
            if cevap == "y":
                print("giriş yapma sekmesine yönlerndirildiniz")
                return giriş_yap()
            elif cevap == "n":
                continue
            else:print("geçersiz giriş yaptınız")
        else : break
    while True:
        şifre = str(input("şifre oluşturunuz: "))
        if len(şifre) < 6 :
            print("lütfen en az 6 karakter kullanın")
        else : break
    while True:
        şifre2 = str(input("şifre nizi tekrarlayınız: "))
        if şifre != şifre2:
            print("lütfen şifrelerinizin aynı olduğundan emin olun")
        else : break
    ad = str(input("adınızı giriniz: "))
    soyad = input("soyadınızı giriniz: ")
    uid = id_oluşturucu()
    abc = kayıtclass(ad,soyad,email,şifre,uid)
    jk.kullanıcı_ekle(abc)
    anahtar = uid
    return kullanıcılar[anahtar]


def giriş_yap():
    yanlış_şifre = 0
    while True: 
        email = str(input("eposta adresinizi giriniz: "))
        if "@" not in email or "." not in email:
            print("eposta adresi geçersiz")
        elif email not in girişvt.keys() :
            print("kayıtlı eposta adresi bulunmamaktadır")
        else: break
    while True:
        şifre = str(input("şifrenizi giriniz: "))
        if girişvt[email].şifre != şifre and yanlış_şifre >= 2:
            while True:  
                print("şifrenizimi unuttunuz yenilemek istermsiniz? [y,n]")
                cvp = input()
                if cvp == "y" :
                    return şifre_yenile()
                elif cvp == "n": 
                    yanlış_şifre = 0
                else: print("lütfen geçerli bir seçim yapın")
            break
        elif girişvt[email].şifre != şifre:
            print("şireniz eşleşmedi lütfen tekrar deneyiniz")
            yanlış_şifre += 1
        else : 
            anahtar = girişvt[email].id
            return kullanıcılar[anahtar]
        

def şifre_yenile(): 
    while True: 
        email = str(input("eposta adresinizi giriniz: "))
        if "@" not in email or "." not in email:
            print("eposta adresi geçersiz")
        elif email not in girişvt.keys() :
            print("kayıtlı eposta adresi bulunmamaktadır")
        else: break
    while True:
        isim = input("lütfen hesabınızı ismini giriniz: ")
        if isim == girişvt[email].ad:
            while True:
                şifre = str(input("yeni şifrenizi oluşturunuz: "))
                if len(şifre) < 6 :
                    print("lütfen en az 6 karakter kullanın")
                else : break
            while True:
                şifre2 = str(input("şifre nizi tekrarlayınız: "))
                if şifre != şifre2:
                    print("lütfen şifrelerinizin aynı olduğundan emin olun")
                else : break        
            girişvt[email].şifre = şifre2 
            kvt = jk.kullanıcıvt_oku()
            for a in kvt["kvt"]:
                if email == a["email"]:
                    a["şifre"] = şifre2
            with open("kullanıcıvt.json","w") as dosya:
                json.dump(kvt,dosya,indent=4)
            print("şifreniz başarılı bir şekilde yenilendi")
            return girişvt[email]
        else : print("adınız uyuşmuyor")




"onur turan"




