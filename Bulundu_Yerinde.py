import random

n = 4
b = True
while b:
    r = random.randint(1234, 9876)
    rstr = str(r)
    b = False
    for i in range(0, n - 1):
        for j in range(i+1, n):
            if rstr[i] == rstr[j]:
                b = True
cikis = '0000'
tstr = ''
deneme = 0
while tstr != cikis:
    b = True
    while b:
        tstr = input('Lütfen Sayınızı Giriniz (0000-oyundan çıkar) = ')
        if tstr == cikis:
            print('Kaybettin!')
            print('Tuttuğum Sayı ', rstr, 'idi.')
            tstr = cikis
            break
        if tstr != cikis:
            b = False
            for i in range(0, n - 1):
                for j in range(i + 1, n):
                    if tstr[i] == tstr[j]:
                        b = True
            if b:
                print('girilen sayının rakamları farklı olmalıdır...')
    if tstr != cikis:
        deneme += 1
        if deneme < 10:
            bulundu = 0
            yerinde = 0
            for i in range(n):
                if rstr.find(tstr[i]) > -1:
                    bulundu += 1
                if rstr[i] == tstr[i]:
                    yerinde += 1
            print(tstr, ':', bulundu, ' tane bulundu...')
            print(tstr, ':', yerinde, ' tane yerinde...')
            print(10-deneme, "Hakkınız Kaldı.")

            if yerinde == n:
                print("Tebrikler!")
                print(deneme, " Denemede Buldunuz!")
                if input("Yeni Oyun İçin 'y' ye basınız") == 'y':
                    print("\n"*50)
                else:
                    tstr = cikis
        else:
            print("Hakkınız Bitti!\nSayı =", rstr, " idi")
            tstr = cikis