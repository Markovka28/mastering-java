# Задача №38.
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# 5. Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести
# имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных


import os
with open("Телефонный справочник.txt", 'w') as telephone_directory:
    telephone_directory.write(''' 
Шашков Давид Кириллович. телефон: 55(04)986-81-75. Город: Москва. 
Никифоров Артур Дамирович. телефон: 625(77)261-03-02. Город: Екатеринбург. 
Федотов Мечислав Юрьевич. телефон: 145(971)934-04-71. Город: Казань. 
Власов Иосиф Онисимович. телефон: 454(98)753-07-13 Город: Челябинск. 
Лапин Игнат Тимурович. телефон: 8(02)537-44-49. Город: Сочи.
                            ''')
    
def data_search():
    with open("Телефонный справочник.txt", 'r') as telephone_directory:
        file = telephone_directory.read()
        for line in file.splitlines():
            print(line)
    with open(r"Телефонный справочник.txt", 'r') as telephone_directory:
        search = telephone_directory.read()
        content = input('Введите искомое значение: ')
        while True:
            if content in search:
                print('строка существует в файле')
            else:
                print('строка не существует в файле')
            break
data_search()

def changing_data():
    with open('Телефонный справочник.txt', 'r+') as telephone_directory:
        old_name = input('Укажите данные которые необходимо заменить: ')
        new_name = input('Укажите новые данные: ')
        output_str = telephone_directory.read().replace(old_name, new_name)
        print('Данные обновлены!', telephone_directory.read())
    with open('Телефонный справочник.txt', 'w') as telephone_directory:
        telephone_directory.write(output_str)
        print(output_str)
changing_data()

def deleting_data(original_file, temp_file, string_to_delete):
    original_file = 'Телефонный справочник.txt'
    temp_file = 'Телефонный справочник!.txt'
    string_to_delete = input('Укажите данные которые необходимо удалить: ')
    with open(original_file, "r") as in_telephone_directory:
        with open(temp_file, "w") as out_telephone_directory:
            for line in in_telephone_directory:
                for word in string_to_delete:
                    line = line.replace(word, ' ')
                    out_telephone_directory.write(line)
    os.replace('Телефонный справочник!.txt', 'Телефонный справочник.txt')
    with open("Телефонный справочник.txt", 'r') as telephone_directory:
        file = telephone_directory.read()
        print(file)

