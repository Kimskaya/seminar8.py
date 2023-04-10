# Создать телефонный справочник. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Возможность импорта и экспорта данных в формате .txt.
# 5. Возможность изменения данных
# 6. Возможность удаления данных

import re
def add_person_data():           
    surname = input("Фамилия: ")
    name = input("Имя: ")
    middle_name = input("Отчество: ")
    phone_number = input("Телефон: ")
    data = open("phonebook.txt", "a", encoding="utf-8")
    data.writelines(f"Фамилия: {surname} Имя: {name} Отчество: {middle_name} Телефон: {phone_number}\n")
    data.close()

def search_data_in_phonebook():     
    look_for = input("Что ищете?: ")
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        for line in data:
            if look_for in line:
                print(line)
            
def print_phonebook():       
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        for line in data:
            print(line)

def import_data():     
    imp_phonebook = input("Введите ссылку для добавлени данных: ")
    with open(imp_phonebook, "r", encoding="utf-8") as data:
        with open("phonebook.txt", "a+", encoding="utf-8") as data_1:
            for line in data:
                if line not in data_1.readlines():
                    data_1.write(line)
            data_1.write("\n")
        print("Данные импортированы")

def export_data():      
    exp_phonebook = input("Введите ссылку: ")
    with open("phonebook.txt", "r", encoding="utf-8") as data_1:
        with open(exp_phonebook, "a+", encoding="utf-8") as data:
            for line in data_1:
                if line not in data.readlines():
                    data.write(line)
            data.write("\n")
        print("Данные экспортированны.")

def change_data():
    with open("phonebook.txt", "r+", encoding="utf-8") as data:
        text = data.read()
        current_data = input("введите данные, которые хотите изменить: ")
        new_data = input("Введите новые данные: ")
        text = text.replace(current_data, new_data)
        data.seek(0)     
        data.write(text) 
        data.truncate()
        print("Данные изменены") 

def delete_line():   
    data_to_delete = input("Что хотите удалить?: ")
    with open("phonebook.txt", "r+", encoding="utf-8") as data:
        lines = data.readlines()      

    with open("phonebook.txt", "w", encoding="utf-8") as data_1:        
        for line in lines:
            if data_to_delete not in line:
                data_1.write(line)
        print("Данные удалены")

     
print("""Меню:
1 - добавить запись 
2 - Поиск 
3 - Вывод телефонной книги на экран 
4 - Импорт в файл
5 - Экспорт из файла
6 - Изменить запись
7 - Удалить запись
8 - Выход
""")

action = int(input("Выберите действие: "))
if action == 1:
    add_person_data()
elif action == 2:
    search_data_in_phonebook()
elif action == 3:
    print_phonebook()
elif action == 4:
    import_data()
elif action == 5:
    export_data()
elif action == 6:
    change_data()
elif action == 7:
    delete_line()
else:
    print("""Неверный ввод""")

