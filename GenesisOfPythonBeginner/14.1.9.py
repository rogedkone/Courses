
Магические даты

Магическая дата – это дата, когда день, умноженный на месяц, равен числу образованному последними двумя цифрами года.

Напишите функцию, is_magic(date) которая принимает в качестве аргумента строковое представление корректой даты и возвращает значение True если дата является магической и False в противном случае.

Примечание. Следующий программный код:

print(is_magic('10.06.1960'))
print(is_magic('11.06.1960'))

должен выводить:

True
False

def is_magic(date):
    x = date.split(".")
    return int(x[0]) * int(x[1]) == int(x[2]) % 100

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
