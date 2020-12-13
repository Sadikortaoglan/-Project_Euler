sayi=0
sayi1=1
cift=[]
sum=0
for i in range(0,40):
    sayi3 = sayi + sayi1
    if sayi3<4000000:
        print(sayi3)
        sayi=sayi1
        sayi1=sayi3
        if sayi3%2==0:
            cift.append(sayi3)
print(len(cift))
for i in cift:
    sum+=i
print("Toplam Çift sayıların değeri: " , sum )