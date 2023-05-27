# Sample Input 1:
# 150
# Sample Output 1:
# 150 мин - это 2 час 30 минут.


x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if x2 > y1 or x1 > y2: print('пустое множество')
elif y1 == x2: print(y1)
elif y2 == x1: print(y2)
elif x2 >= x1 and y2 >= y1:
    print(x2, y1)
elif x1 >= x2 and y1 >= y2:
    print(x1, y2)
    # ОТРИЦАТЕЛЬНЫЕ ЗНАЧЕНИЯ:
elif x1 < 0 or x2 < 0 or y1 < 0 or y2 < 0:
    if x2 >= x1 and y2 <= y1:
        print(x2, y2)
    if x1 >= x2 and y1 <= y2:
        print(x1, y1)


