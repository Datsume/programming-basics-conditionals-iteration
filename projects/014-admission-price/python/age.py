
#age=input("Age:")

#if int(age)>=18:
#    print("Sei maggiorenne")
#else:
#    print("Sei minorenne")



age=input("Age:")
license=input("License:")

if int(age)>=18 and license=="si":
    print("Puoi guidare")
elif int(age)>=18 and license=="no":
    print("Fatti la patente")
else:
    print("Aspetta qualche anno")