import random 
kérdés = input("kérdezd meg a Bűvös labdát: ")
válasz = random.randint(1, 8)
if válasz == 1:
    print("Biztos")
elif válasz == 2:
    print("Jó kilátások")
elif válasz == 3:
    print("Bízhatsz benne")
elif válasz == 4:
    print("Kérdezd meg késöbb")
elif válasz == 5:
    print("Koncentrálj kérdezd meg újra")
elif válasz == 6:
    print("A válasz homályos, próbáld újra")
elif válasz == 7:
    print("A válaszom nem")
elif válasz == 8:
    print("Forrásaim szerint nem")
else:
    print("Ez nem kérdés!")
print("A Bűvös labda válasza: ", válasz)
print("Kérdésed: ", kérdés) 
print("Vége a játék!")
# A Bűvös labda játék vége