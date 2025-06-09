# legnagyobb közös osztó, legkisebb közös többszörös
import math
def gcd(a, b):
    """Calculate the greatest common divisor (GCD) of two numbers."""
    while b:
        a, b = b, a % b
    return abs(a)
def lcm(a, b):
    """Calculate the least common multiple (LCM) of two numbers."""
    return abs(a * b) // gcd(a, b)

number1 = int(input("Kérem az első számot: "))
number2 = int(input("Kérem a második számot: "))    
result = gcd(number1, number2)
print(f"A legnagyobb közös osztó: {result}")
print(f"A legkisebb közös többszörös: {lcm(number1, number2)}")
# This code calculates the greatest common divisor (GCD) and least common multiple (LCM) of two numbers. 