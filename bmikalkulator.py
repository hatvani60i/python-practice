magassag = float(input("ird be a magasságod cm-ben:")) 
testsuly = float(input(" irja be a testsulyat kg-ba:"))
magassagmeterben = magassag/100
bmiertek= testsuly/(magassagmeterben*magassagmeterben)
print("az ön testömeg indexe(bmi):", bmiertek)
if bmiertek<18.5: print("túlsovány")

elif bmiertek>=18.5 and bmiertek <24.9:
    print("normális")
elif bmiertek>=24.9 and bmiertek <29.9:
    print("elhízás I.szakasz")
elif bmiertek>=29.9 and bmiertek <34.9:
    print("elhízás II.szakasz") 
elif bmiertek>=34.9 and bmiertek<39.9:
    print("elhízás III.szakasza")
else:
    print("fogyál le de gyorsan")  
