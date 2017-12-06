for numara in range(2,1000):
    for i in range(2,numara):
        if numara%i == 0:
            break
    else:
            print(numara)