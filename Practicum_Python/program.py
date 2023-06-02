from math import sqrt

a, b, c = float(input()), float(input()), float(input())

d = pow(b, 2) - 4*a*c

if d > 0:    
    print(min(((-b - sqrt(d)) / (2*a)), ((-b + sqrt(d)) / (2*a))))
    print(max(((-b - sqrt(d)) / (2*a)), ((-b + sqrt(d)) / (2*a))))
elif d == 0:
    print(-b / (2*a))
elif d < 0:
    print('Нет корней')