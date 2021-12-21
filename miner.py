def print_field():
    print("    ", end="")
    for i in range(n):
        if i > 9:
            print(i + 1, end=" ")
        else:
            print(i + 1, end="  ")
    print()
    for i in range(len(a)):
        if i < 9:
            print(i + 1, end="  ")
        else:
            print(i + 1, end=" ")
        for j in range(len(a[i])):
            print(" " + a[i][j], end=" ")
        print()


import sys
import random
n = 10
a = []
mines = []
for i in range(n):
    a.append(["□"] * n)
print_field()
for i in range(len(a)):
    print("Введите координаты хода (строка, столбец)")
    i,j = map(int, input().split())
    nothing = random.randint(1,2)
    if nothing == 1:
        a[i-1][j-1] = " "
        print_field()
    if nothing == 2:
        a[i-1][j-1] = "*"
        print_field()
        sys.exit()