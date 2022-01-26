import random
import time

print("""
******************************************
SAYI TAHMİN ETME OYUNU
1 İLE 40 ARASINDA SAYIYI TAHMİN EDİNİZ
******************************************
""")

rastgele_sayı = random.randint(1,40)
tahmin_hakkı = 7
while True:
    tahmin = int(input("Tahmininiz : "))

    if (tahmin <rastgele_sayı ) :
        print("Bilgiler Sorgulanıyor....")
        time.sleep(1)
        print("Daha yüksek bir sayı söyleyin")
        tahmin_hakkı -= 1
    elif (tahmin > rastgele_sayı ) :
        print("Bilgiler Sorgulanıyor....")
        time.sleep(1)
        print("Daha düşük bir sayı söyleyin")
        tahmin_hakkı -= 1

    else:
        print("Bilgiler Sorgulanıyor....")
        print("Tebrikler tahmininiz doğru !")
        break

    if tahmin_hakkı==0 :
        print("Tahmin hakkınız bitti .")
        print("Sayınız:",rastgele_sayı)