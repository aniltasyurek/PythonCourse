#1. Python Nedir ?
#Python, kolay okunabilir, öğrenmesi basit ve güçlü bir programlama dilidir. Veri analizi, web geliştirme, yapay zeka, otomasyon gibi birçok alanda kullanılır.


#2. İlk Python Kodu (Merhaba Dünya!)

print("Merhaba Dünya!")


#3. Değişkenler ve Veri Tipleri

sayi = 10       # Tam sayı (int)
pi = 3.14       # Ondalıklı sayı (float)
isim = "Ali"    # Metin (string)
dogru_mu = True # Mantıksal (bool)


#4. Kullanıcıdan Veri Alma (input)

isim = input("Adınız nedir? ")
print("Merhaba", isim, "!")

#5. Koşullu İfadeler (if - else)

yas = int(input("Yaşınızı Girin :"))
if yas >= 18:
    print("Ehliyet alabilirsiniz")
else:
    print("Ehliyet alamazsınız")


#6. Döngüler (for ve while)

###### for ######
for i in range(5):
    print("Merhaba!", i)

###### while ######
sayi1 = 1
while sayi1 <= 5:
    print(sayi1)
    sayi1 += 1   #sayi1 = sayi1 + 1

###### break ######
for a in range(10):
    if a == 5:
        break #5'e gelince döngüyü durdur
    print(a)


#7. Listeler (Diziler)

meyveler = ["Elma","Armut","Muz","Çilek"]
print(meyveler[0]) #ilk eleman
print(meyveler[-1]) #son eleman

for meyve in meyveler:
    print(meyve)


#8. Fonksiyonlar

def selam_ver(isim):
    print("Merhaba", isim)
selam_ver("Ahmet")

###### return ######
def topla(a,b):
    return a+b
sonuc = topla(3,4)
print(sonuc)


#9. Hata Yönetimi (try - except)

try:
    sayi2 = int(input("Bir sayı gir : "))
    print("Girilen sayı:", sayi2)
except ValueError:
    print("Hata! Lütfen bir sayı girin") #string bir değer girersen bunu yazdırır

#10.Sözlük (Dictionary)

kisi = {
    "isim": "Ahmet",
    "yas": 25,
    "sehir": "İstanbul"
}

print(kisi["isim"]) #Ahmet
print(kisi["yas"]) #25
print(kisi["sehir"]) #İstanbul
print(kisi)

kisi["yas"] = 26 #Yeni eleman ekleme

for anahtar, deger in kisi.items():
    print(anahtar, ":", deger)

#10. Demet (Tuple)

demet = ("Elma", "Armut", "Muz")
print(demet[0])  # Elma
print(demet[-1]) # Muz

#demet[0] = "Çilek"  # Hata! Tuple değiştirilemez.

def koordinatlar():
    return (40.7128, 74.0060)  # Enlem ve boylam döndürülüyor

enlem, boylam = koordinatlar()
print("Enlem:", enlem)
print("Boylam:", boylam)


#10. Küme (Set)

kume = {1, 2, 3, 4, 4, 2}  # Tekrar eden sayılar otomatik silinir
print(kume)  # {1, 2, 3, 4}

kume.add(5)      # Eleman ekleme
kume.remove(2)   # Eleman silme
print(kume)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # Birleşim → {1, 2, 3, 4, 5, 6}
print(A & B)  # Kesişim → {3, 4}
print(A - B)  # Fark → {1, 2}


#11.Lambda Fonksiyonları

###Normal fonksiyon
def kare_al(x):
    return x ** 2

print(kare_al(5))  # 25

###Lambda fonksiyonu ile aynı işlem
kare = lambda x: x ** 2
print(kare(5))  # 25

###Lambda Fonksiyonlarını Liste İçinde Kullanma
sayilar = [1, 2, 3, 4, 5]
kareler = list(map(lambda x: x ** 2, sayilar))
print(kareler)  # [1, 4, 9, 16, 25]

###Lambda ile Filtreleme
sayilar = [10, 25, 30, 45, 50, 75]
# 30'dan büyük sayıları filtreleyelim
buyuk_sayilar = list(filter(lambda x: x > 30, sayilar))
print(buyuk_sayilar)  # [45, 50, 75]





