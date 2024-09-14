"""
1. Seviye: Basit
Soru: Kullanıcıdan iki sayı alarak bu sayıları toplayan bir programın pseudo kodunu yazın.

"""
from pickle import FALSE

a = int(input("1. Sayıyı Giriniz: "))
b = int(input("2. Sayıyı Giriniz: "))

def num_sum(num1,num2):
    print("Sonuc: ",num1+num2)

num_sum(a,b)
"""
2. Seviye: Orta
Soru: 1'den 100'e kadar olan sayıları toplayan bir programın pseudo kodunu yazın.
"""
n = 100
toplam = (n*(n+1))/2
print(toplam)

#########################
toplam = 0

for sayi in range(1,101):
    toplam += sayi

print("Sonuc: ",toplam)

"""
3. Seviye: İleri
Soru: Kullanıcıdan alınan bir sayının asal olup olmadığını bulan bir programın pseudo kodunu yazın.

"""
x = int(input("Sayı Giriniz: "))
def check(num):
    if num < 2:
        return False

    for i in range(2, num):

        if num % i == 0:
            return False
        return True

if check(x):
    print(f"{x} bir asal sayıdır.")
else:
    print(f"{x} bir asal sayı değildir.")

"""
4. Seviye: Zor
Soru: Bir dizideki (array) elemanların tekrar edip etmediğini kontrol eden bir programın python kodunu yazın.

"""
def check(dizi):
    for eleman in dizi:
        if dizi.count(eleman) > 1:
            return True
    return False

dizi = input("Bir dizi girin (elemanları boşlukla ayırın): ").split()

if check(dizi):
    print("Dizide tekrar eden elemanlar var.")
else:
    print("Dizide tekrar eden eleman yok.")
