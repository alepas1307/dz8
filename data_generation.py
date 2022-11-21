import random
import csv
import logger as lg


file = open('employees.csv', 'w')
newrecord = "ID,Name,Surname,PhoneNumber,Position\n"
file.writelines(newrecord)

ls_name = ['Svetlana', 'Olga', 'Anton', 'Anna', 'Inna',
           'Viktor', 'Vasilisa', 'Alex', 'Miron', 'Igor', 'Anna']
ls_surname = ['Kovalenko', 'Sidorenko', 'Mironenko',
              'Galich', 'Shapiro', 'Duma', 'Duma', 'Shagal', 'Moroz']
ls_position = ['director', 'accountant', 'secretary', 'manager']


def list_of_numbers():
    # s = '+'
    randomListPhone = random.randint(79000000000, 80000000000)
    # s = s + str(randomListPhone)
    return str(randomListPhone)
# рандомно соеденить имена фамилии и номера телефонов (отдельный метод) def + присвоение id


def string_creation():
    s = ""
    s = s + random.choice(ls_name) + ',' + random.choice(ls_surname) + ',' + \
        list_of_numbers() + ',' + random.choice(ls_surname) + random.choice(ls_position)
    return s


def start():
    for i in range(100):
        a = f'{str(i + 1)},{string_creation()}\n'
        file.write(a)
    file.close()


start()