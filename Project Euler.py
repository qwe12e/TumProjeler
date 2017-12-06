nereye = input("gir")
if nereye == "1":
    # 1000 e kadar 3 veya 5 in katlarını topla
    a = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            a += i
    print(a)

elif nereye == "2":
    # 4 milyonun altindaki çift fibonacci sayilarini topla
    a = 1
    b = 2
    toplam = 2
    for i in range(30):
        c = b + a
        a = b
        b = c
        print(c)
        if c % 2 == 0:
            print(c)
            toplam += c
        
    print(toplam)
elif nereye == "3":
    # 600851475143 sayısının en buyuk asal katsayisi kactir
    def isPrime(num):
        for i in range(2, int(num / 2)):
            if num % i == 0:
                return False
        return True


    def largestPrimeFactor(num):
        rest = num
        i = 1
        while rest != 1:
            i = i + 1
            if isPrime(i) and rest % i == 0:
                print(rest, " Sayısı---", i, " ile bölündü")
                rest = rest / i
        return i


    print(largestPrimeFactor(600851475143))
elif nereye == "4":
    for i in range(100, 1000):
        for j in range(100, i):
            carpim = i * j
            if len(str(carpim)) == 6:
                if str(carpim)[0] == str(carpim)[len(str(carpim)) - 1] and\
                                str(carpim)[1] == str(carpim)[len(str(carpim)) - 2] and\
                                str(carpim)[2] == str(carpim)[len(str(carpim)) - 3]:
                    print(carpim)
elif nereye == "5":
    # 232792560
    for i in range(20,1000000000):
        if i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0 and i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and\
                                i % 9 == 0 and i % 10 == 0 and i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and\
                                i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and\
                                i % 19 == 0:
            print(i)

elif nereye == "6":
    toplam = 0
    toplu=0
    for i in range(1, 101):
        toplam += i**2
        toplu += i
    toplu = toplu**2
    # Parantez kare ve normal karelerin toplamı arasındaki farkı gösteren program
    print("(...)^2 = ", toplu, " .^2+.^2... = ", toplam, "Farkı = ", str(toplu - toplam))

elif nereye == "7":
    def get_primes(start, stop):
        dct = {x: True for x in list(range(start, stop + 1))}
        x = start

        while x ** 2 <= stop:
            if dct[x]:
                y = x ** 2
                while y <= stop:
                    dct[y] = False
                    y += x
            x += 1

        lst = []
        for x, y in dct.items():
            if y:
                lst.append(x)
        return lst


    res = get_primes(2, 1000000)
    print(res[10000])

elif nereye == "8":
    # 73167176531330624919225119674426574742355349194934
    # 96983520312774506326239578318016984801869478851843
    # 85861560789112949495459501737958331952853208805511
    # 12540698747158523863050715693290963295227443043557
    # 66896648950445244523161731856403098711121722383113
    # 62229893423380308135336276614282806444486645238749
    # 30358907296290491560440772390713810515859307960866
    # 70172427121883998797908792274921901699720888093776
    # 65727333001053367881220235421809751254540594752243
    # 52584907711670556013604839586446706324415722155397
    # 53697817977846174064955149290862569321978468622482
    # 83972241375657056057490261407972968652414535100474
    # 82166370484403199890008895243450658541227588666881
    # 16427171479924442928230863465674813919123162824586
    # 17866458359124566529476545682848912883142607690042
    # 24219022671055626321111109370544217506941658960408
    # 07198403850962455444362981230987879927244284909188
    # 84580156166097919133875499200524063689912560717606
    # 05886116467109405077541002256983155200055935729725
    # 71636269561882670428252483600823257530420752963450
    sayi = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    liste = list()
    for j in range(len(sayi)-12):
        toplam = 1
        for i in range(j, j + 13):
            toplam *= int(sayi[i])
        liste.append(toplam)
        print(j, ".Sefer toplam = ", toplam)
    print(max(liste))


elif nereye == "9":
    # a ^2 + b ^2 = c ^2 Formülünde a<b<c olacak şekilde a + b + c = 1000 bulunuz abc = ?
    # Eski Formülüm
    # for a in range(1, 332):
    #     for b in range(a + 1, 499):
    #         for c in range(b + 1, 1002):
    #             ak = a ** 2
    #             bk = b ** 2
    #             ck = c ** 2
    #             if ak + bk == ck:
    #                 if a + b + c == 1000:
    #                     print(a, "^2 + ", b, "^2 = ", c, "^2 Toplamı = ",str(a + b + c))
    #                     break
    import math
    a = 1
    b = 2
    c = 0
    a_max = 332
    b_max = 499
    while a + b + c != 1000:
        if a + 1 < b and a <= a_max:
            a += 1
        else:
            b += 1
            a = 1
        c = math.sqrt(a ** 2 + b ** 2)
    print(a, "^2 + ", b, "^2 = ", c, "^2")
    print(int(a * b * c))
elif nereye == "10":
    def get_primes(start, stop):
        dct = {x: True for x in list(range(start, stop + 1))}
        x = start

        while x ** 2 <= stop:
            if dct[x]:
                y = x ** 2
                while y <= stop:
                    dct[y] = False
                    y += x
            x += 1

        toplam = 0
        for x, y in dct.items():
            if y:
                toplam += x

        return toplam
    res = get_primes(2, 2000000)
    print(res)
elif nereye == "11":
    print("Bu soruyu yapamadım tekrar bakacam.")
    # sayıyı almak için
    # with open("ProjectEuler11.txt", "r") as file:
    #     liste = file.read().split(" ")
    #
    # def deneme(liste2, num):
    #     carpimlist = list()
    #     # sag capraz
    #     for j in range(num, num + 17):
    #         toplam = 1
    #         toplam *= int(liste2[j])
    #         toplam *= int(liste2[j + 21])
    #         toplam *= int(liste2[j + 42])
    #         toplam *= int(liste2[j + 63])
    #         carpimlist.append(toplam)
    #     # sol capraz
    #     for t in range(num+3, num):
    #         toplam = 1
    #         toplam *= int(liste2[j])
    #         toplam *= int(liste2[j + 22])
    #         toplam *= int(liste2[j + 41])
    #         toplam *= int(liste2[j + 60])
    #         carpimlist.append(toplam)
    #     # Yan yana
    #     for i in range(num + 16):
    #         toplam = 1
    #         for j in range(i, i + 4):
    #             toplam *= int(liste[j])
    #         carpimlist.append(toplam)
    #     # Alt alta
    #     for i in range(20):
    #         toplam = 1
    #         toplam *= int(liste[num + i])
    #         toplam *= int(liste[num + 20 + i])
    #         toplam *= int(liste[num + 40 + i])
    #         toplam *= int(liste[num + 60 + i])
    #         carpimlist.append(toplam)
    #     return carpimlist
    # denemelist = [0]
    # for y in range(0, 321, 20):
    #     print("y ", y)
    #     denemelist.extend(deneme(liste, y))
    # denemelist.sort()# Gerekli değil
    # print(denemelist)# Gerekli değil
    # print(max(denemelist))
elif nereye == "12":
    def triangular(maks):
        for i in range(1, maks + 1):
            yield i * (i + 1) // 2
    def get_primes(start, stop):
        dct = {x: True for x in list(range(start, stop + 1))}
        x = start

        while x ** 2 <= stop:
            if dct[x]:
                y = x ** 2
                while y <= stop:
                    dct[y] = False
                    y += x
            x += 1

        lst = []
        for x, y in dct.items():
            if y:
                lst.append(x)
        return lst
    bolunenliste = {}
    asalsayi = get_primes(2,2000000)
    triangularlistesi = [i for i in triangular(1000)]
    while True:
        i = 0
        j = 0
        bufferliste = list()
        if triangularlistesi[i] < asalsayi[j]:
            if triangularlistesi[i] % asalsayi[j] == 00:
                bufferliste.append(asalsayi[j])
            else:
                j += 1
            break
        else:
            if len(triangularlistesi) == i:
                break
            else:
                i += 1


    print(bolunenliste)
    listt = dict()
    for i, j in bolunenliste.items():
        listt[i] = len(j)
    print(listt.values())

elif nereye == "q":
    quit()


