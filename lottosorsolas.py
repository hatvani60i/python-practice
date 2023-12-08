
import random
lottogomb = []
kiuzottszamok = []
tipp=[]
szam=0

for i in range(0, 5 ):
    int(input("kérek egy 1 és 90 koze eso szamot:",szam))
    tipp.append(szam)


for i in range(1,91):
    lottogomb.append(i)


random.shuffle(lottogomb)

for i in range (0,5):
    kiuzottszamok.append(lottogomb[i])


kiuzottszamok.sort()
tipp.sort()

print("az on tippje:",tipp)
print("a szamok sorbarendezve:",kiuzottszamok)






