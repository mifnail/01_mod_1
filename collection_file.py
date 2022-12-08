from csv_csv import file_open, insert, drop_by_arg, find, avg_age, save, show_csv,find_gnum
from builtins import print

FILENAME = "data.csv"

MENU = {
    '1': 'Открыть файл',
    '2': 'Добавить',
    '3': 'Удалить',
    '4': 'Найти по значению',
    '5': 'Вывести средний пробег',
    '6': 'Сохранить в файл',
    '7': 'Вывести записи',
    '8': 'Поиск по госномеру',
    '0': '<-Меню',
    'exit': 'Выход'
}

for key, val in MENU.items():
    print(key, '-', val)

while True:
    action = input('>_ ')
    if action == '1':
        file_open()
    elif action == '2':
        print(insert(input('vin: '), input('Гос номер: '), input('Марка: '), input('Модель: '),
                     int(input('Год выпуска: ')), int(input('Мощность: ')), int(input('ПРобег: '),),
              int(input('Количество владельцев: ')), int(input('Стоимость: '))))
    elif action == '3':
        col = input('Колонка: ')
        val = input('Значение: ')
        print(drop_by_arg(val, col_name=col))
    elif action == '4':
        val1 = input('Значение марки: ')
        val2 = input('Значение модели: ')
        find(val1, val2)
    elif action == '5':
        avg_age()
    elif action == '6':
        save()
    elif action == '0':
        for key, val in MENU.items():
            print(key, '-', val)
    elif action == '7':
        show_csv()
    elif action == '8':
        val=input("Введите гос номер авто")
        find_gnum(val)
    elif action == 'exit':
        break
