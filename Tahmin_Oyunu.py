import random
x=random.randrange(0,1000)
for i in range(9):
    sayi=int(input("Sayı giriniz = "))
    if sayi == x:
        print('Tebrikler kazandınız!!! Sayı = ',x,'Kalan hak = ',8-i)
        break
    elif sayi > x:
        print('Sayımdan büyük sayı girdiniz! KALAN HAK = ',8-i)
    elif sayi < x:
        print('Sayımdan küçük sayı girdiniz! KALAN HAK = ',8-i)
if i==8:
    print('Kaybettiniz! :( Sayı = ',x)