toplam=[]
sum1=0
for i in range(1,101):
     sum1+=i
     kare=i**2
     toplam.append(kare)
print(f"Karelerin toplamı :{sum(toplam)} ,Toplam değerlerin kareleri : {sum1**2}")
print(f"Fark : {(sum1**2)-sum(toplam)}")