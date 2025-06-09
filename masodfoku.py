# másodfokú egyenlet megoldása
import cmath
def masodfoku_egyenlet(a, b, c):
    """Másodfokú egyenlet megoldása: ax^2 + bx + c = 0"""
    if a == 0:
        raise ValueError("Az 'a' együttható nem lehet nulla.")
    
    d = b**2 - 4*a*c  # diszkrimináns
    if d < 0:
        # komplex gyökök
        x1 = (-b + cmath.sqrt(d)) / (2 * a)
        x2 = (-b - cmath.sqrt(d)) / (2 * a)
    else:
        # valós gyökök
        x1 = (-b + d**0.5) / (2 * a)
        x2 = (-b - d**0.5) / (2 * a)
    
    return x1, x2
# Felhasználói bemenet
try:
    a = float(input("Kérem az 'a' együtthatót: "))
    b = float(input("Kérem a 'b' együtthatót: "))
    c = float(input("Kérem a 'c' együtthatót: "))
    
    gyok1, gyok2 = masodfoku_egyenlet(a, b, c)
    print(f"A másodfokú egyenlet gyökei: x1 = {gyok1}, x2 = {gyok2}")
except ValueError as e:
    print(f"Hiba: {e}")
# This code solves a quadratic equation of the form ax^2 + bx + c = 0.
# It calculates the roots using the quadratic formula and handles both real and complex roots.