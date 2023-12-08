aloshatar=0
felsohatar=0
osszeg=0

alsohatar = int(input("kérem adja meg a sorozat alsó határát"))
felsohatar = int(input("kérem a sorozat felső határát"))

while alsohatar <= felsohatar: 
    osszeg = osszeg+alsohatar
    alsohatar=alsohatar+1

    print("a sorozat tagjainak összege", osszeg)
    
