
Ревью кода - 9

На обработку поступает последовательность из 4 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10610^6106. Нужно написать программу, которая выводит на экран количество нечётных чисел в исходной последовательности и максимальное нечётное число. Если нечётных чисел нет, требуется на экран вывести «NO». Программист торопился и написал программу неправильно.

Найдите все ошибки в этой программе (их может быть одна или несколько). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.

Примечание. Обратите внимание, что требуется найти ошибки в имеющейся программе, а не написать свою, возможно, использующую другой алгоритм решения.
n = 4
count = 0
maximum = - 10 ** 6 - 1
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
#            break
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
