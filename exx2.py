#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к 
#заданному числу X. Пользователь в первой строке вводит натуральное число 
#N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
#Последняя строка содержит число X
#5
#    1 2 3 4 5
#    6
#    -> 5
from random import randint
my_list = []
n = int(input())
for i in range(n):
    my_list.append(randint(1, 6))
for i in my_list:
    print(i, end=' ')
x = int(input())

iskomoe = 0
for i in range(n):
    if x - my_list[i] < x - my_list[i+1]:
        my_list[i] = iskomoe
    else:
          my_list[i+1] = iskomoe
print(iskomoe)
