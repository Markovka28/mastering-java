""" d = {}
d['q'] = 'qwerty'
print(d)

dic={'up': '|', 'down': '/' }
for i in dic:
    print('{up}:{down}'.format(i, dic[i])) """
    
"""    Напишите программу, которая принимает на вхостроку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n. """

""" s = 'a a a b a c b b d'.split()
l = {}
r = ''
for i in range(len(s)):
    if s[i] not in l.keys():
        l[s[i]] = 1
        r += f'{s[i]} '
    else:
        r += f'{s[i]}_{l[s[i]]} '
        l[s[i]] += 1
print(r) """

# s = 'a a a b a c b b d d'.split()
# r = ''
# for i, letter in enumerate((s)):
#     if s[:i].count(letter)<1:
#         r+=letter+' '
#     else:
#         r+=f'{letter}_{s[:i].count(letter)} '
# print(r)

""" Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте. """


""" s = "She sells, sea shells on the sea shore. The shells\
 that she sells are sea shells! I'm sure So if she sells sea \
shells on the sea shore? I'm sure that\n the shells are sea \
shore shells"
r = [i.strip('.,?!\n').lower() for i in s.split()]
r = set(r)
print(r)
print(len(r)) """

""" Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам. """


num = int(input('Введите число: '))
max = num
while num != 0:
    if num > max and num != 0:
       max = num
    num = int(input())
print(f'{max = }')