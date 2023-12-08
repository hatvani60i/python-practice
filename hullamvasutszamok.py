szam=int(input("adj meg egy számot: "))
lepesek = 0

while szam > 1:
    
    if szam % 2 == 0:
        szam=int(szam/2)
        print(szam)
        lepesek = lepesek + 1

    else:
        szam=int((szam*3)+1)
        lepesek=lepesek + 1
        print(szam)
print ("ennyi lepesbol szamoltam ki:")
print(lepesek)
