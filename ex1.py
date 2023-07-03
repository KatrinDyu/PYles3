# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#5
#   1 2 3 4 5
#   3
#   -> 1
from random import randint
my_list = []
n = int(input())
for i in range(n):
   # item = randint(1, 99)
    my_list.append(randint(1, 99))
for i in my_list:
    print(i, end=' ')
x = int(input())
count = 0
for i in range (n):
    if my_list[i] == x:
        count += 1
print(count)
print()