# primszám vagy nem prím szám meghatározása
def primszam_e(n):
    """Ellenőrzi, hogy a szám prím-e."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# Felhasználói bemenet
try:
    szam = int(input("Kérem adjon meg egy számot: "))
    if primszam_e(szam):
        print(f"{szam} egy prím szám.")
    else:
        print(f"{szam} nem prím szám.")
except ValueError:
    print("Kérem, érvényes egész számot adjon meg.")    
# This code checks if a number is prime or not.
# It defines a function that checks for primality and handles user input.
# It prints whether the number is prime or not.         
