import math

asal_sayılar=[]
def AsalSayılar(n):
    while n % 2 == 0:
        print(2,)
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            print(i, )
            n = n // i
            asal_sayılar.append(i)



    if n > 2:
        print(n)
        asal_sayılar.append(n)
    print(f"En büyük asal çarpan : {max(asal_sayılar)}\nEn küçük asal çarpan : {min(asal_sayılar)}")



n = 21
AsalSayılar(n)