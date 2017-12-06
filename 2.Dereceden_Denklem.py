import math
a = int(input("ax2+bx+c=0 Denklemi için a'yı giriniz = "))
if a==1:
    b = int(input("x2+bx+c=0 Denklemi için b'yı giriniz = " ))
    if b >= 0:
        c = int(input("x2+%dx+c=0 Denklemi için c'yı giriniz = " %  b))
    else:
        c = int(input("x2%dx+c=0 Denklemi için c'yı giriniz = " % b))
else:
    b = int(input("%dx2+bx+c=0 Denklemi için b'yı giriniz = " % a))
    if b >= 0:
        c = int(input("%dx2+%dx+c=0 Denklemi için c'yı giriniz = " % (a, b)))
    else:
        c = int(input("%dx2%dx+c=0 Denklemi için c'yı giriniz = " % (a, b)))

disk = (b * b) - (4 * a * c)
if  disk > 0:
    x1 = (- b - math.sqrt(disk)) / (2 * a)
    x2 = (- b + math.sqrt(disk)) / (2 * a)
    print("İki farklı gerçel kökü vardır.\n X1 = %d \n X2 = %d " % (x1 , x2))

elif disk < 0:
    print("Denkleminin gerçel kökü yoktur." )
else:
    x =  - b / (2 * a)
    print('Kökler çakışık x = ', x)