""" 
Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках 
не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного 
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
"""
"""  
poem = input("Ведите слово или выражение: ")
ok = poem[:len(poem)//2]
syllable_count1 = 0
for i in ok:
      if(i == 'а' or i =='е' or i == 'и' or i == 'о' or i == 'у' or i == 'А' or i == 'Е' or i == 'И' or i == 'О' or i == 'У'):
            syllable_count1 += 1
print(f"Количество слогов в первой части введенного выражении равно: {syllable_count1}")
not_ok = poem[len(poem)//2:]
syllable_count2 = 0
for i in not_ok:
      if(i == 'а' or i =='е' or i == 'и' or i == 'о' or i == 'у' or i == 'А' or i == 'Е' or i == 'И' or i == 'О' or i == 'У'):
            syllable_count2 += 1
print(f"Количество слогов во второй части введенного выражении равно: {syllable_count2}")
if syllable_count1 == syllable_count2:
    print(f'Парам пам-пам, с ритмом все в порядке')
else:
    print('Пам парам, с ритмом все не в порядке')
 """
""" 
Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента 
функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
 """
"""  
def print_operation_table(operation, num_rows, num_columns):   
    for i in range(1, num_rows + 1):
        print(' ')
        for j in range(1, num_columns + 1):
            print(operation(i, j), end=' ')
print_operation_table(lambda x, y: x * y, 6, 6)
 """
"""  
from random import randint
r = int(input('количество строк: '))
c = int(input('количество столбцов: '))
total = [[randint(10, 99) for j in range(c)] for i in range(r)]
import numpy as np
x = np.array(total)
print(*x, sep='\n')
print (x[1][1])
 """
 
# input_str = input('Пожалуйста, предоставьте входные данные\n')
# delimiter = input('Пожалуйста, укажите текущий разделитель\n') 
# delimiter_new = input('Пожалуйста, укажите новый разделитель\n') 
# output_str = input_str.replace(delimiter, delimiter_new) 
# print('Обновленные данные =', output_str)

# f = open('Телефонный справочник.txt', 'r')
# print(f.read())
# f.close()

# import mmap
# with open('Телефонный справочник.txt', 'rb+') as f:
#     s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
#     if s.find('blabla') != -1:
#         print('true')
 
 

 