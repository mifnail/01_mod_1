import csv

csv_file = []


# Открываю csv файл
def file_open():
    global csv_file
    with open('data.csv', "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            csv_file.append(row)
    print('Файл открыт. Записей:', len(csv_file))


# Добавление данных
def insert(vin, gnum, mark, model, age, ls, km, count, price):
    global csv_file
    try:
        csv_file.append(
            {'vin': vin, 'gnum': gnum, 'mark': mark, 'model': model, 'age': age, 'ls': ls, 'km': km, 'count': count,
             'price': price})
    except Exception as e:
        return f'Ошибка при добавленнии новой записи {e}'
    return "Данные добавлены."


# Удалить по аргументу
def drop_by_arg(val, col_name='фио'):
    global csv_file
    try:
        csv_file = list(filter(lambda x: x[col_name] != val, csv_file))
    except Exception as e:
        return f'Строка со значением {val} поля {col_name} не найдена'
    return (f'Строка со значением "{val}" столбца "{col_name}" удалена.')


# Поиск
def find(val, col_name='фио'):
    print(*list(filter(lambda x: x[col_name] == val, csv_file)))


# Средний возраст
def avg_age():
    print("Средний возраст:",
          sum([int(row['возраст']) for row in csv_file]) // len(csv_file))


# Сохранение
def save():
    with open('data.csv', "w", encoding="utf-8", newline="") as file:
        columns = ['ном', 'фио', 'возраст', 'телефон', 'отдел']
        writer = csv.DictWriter(file, delimiter=";", fieldnames=columns)
        writer.writeheader()
        writer.writerows(csv_file)
        print("Данные добавлены!")


# Открыт ли файл или нет
def show_csv():
    if len(csv_file) == 0:
        print(type(csv_file))
    else:
        print('{:<5}{:<25}{:<8}{:<12}{:<15}'.format(
            'ном', 'фио', 'возраст', 'телефон', 'отдел'
        ))
        for el in csv_file:
            print('{:<5}{:<25}{:<8}{:<12}{:<15}'.format(el["ном"],
                                                        el["фио"],
                                                        el["возраст"],
                                                        el["телефон"],
                                                        el['отдел']))
