# put your python code here
a = int(input())
b = int(input())
c = int(input())

# находим максимум
if b <= a >= c:
    print(a)
elif a <= b >= c:
    print(b)
elif a <= c >= b:
    print(c)

# находим минимум
if (b >= a and a <= c):
    print(a)
elif (a >= b and b <= c):
    print(b)
elif (a >= c and c <= b):
    print(c)

# находим второе число
if (b <= a >= c) and (a >= b <= c):
    print(c)
elif (b >= a <= c) and (a <= b >= c):
    print(c)
elif (a <= b >= c) and (a >= c <= b):
    print(a)
elif (a >= b <= c) and (a <= c >= b):
    print(a)
else:
    print(b)
