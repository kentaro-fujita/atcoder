import math

A, B, C, D = map(int, input().split())

num1 = B // C - (A-1) // C
num2 = B // D - (A-1) // D
gcdCD = C * D // math.gcd(C, D)
num3 = B // gcdCD - (A-1) // gcdCD

print(B - A - num1 - num2 + num3 + 1)