
Ревью кода-1 🌶️🌶️

На обработку поступает последовательность из 101010 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10610^6106. Нужно написать программу, которая выводит на экран количество неотрицательных чисел последовательности и их произведение. Если неотрицательных чисел нет, требуется вывести на экран «NO». Программист торопился и написал программу неправильно.

Найдите все ошибки в этой программе (их ровно 444). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.

Примечание 1. Число xxx не превышает по абсолютной величине 10610^6106, если −106≤x ≤106-10^6 \le x \le 10^6−106≤x ≤106.

Примечание 2. При необходимости вы можете добавить необходимые строки кода.

count = 0
p = 1
for i in range(1, 11):
    x = int(input())
    if x >= 0:
        p *= x
        count += 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')
