
max и min

Дано натуральное число n, (n≥10)n, \, (n \ge 10)n,(n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.

Формат входных данных 
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести максимальную и минимальную цифры введенного числа (с поясняющей надписью).

Sample Input 1:

26670

Sample Output 1:

Максимальная цифра равна 7
Минимальная цифра равна 0

Sample Input 2:

8945

Sample Output 2:

Максимальная цифра равна 9
Минимальная цифра равна 4

Sample Input 3:

7645897791

Sample Output 3:

Максимальная цифра равна 9
Минимальная цифра равна 1

n = int(input())
minvalue, maxvalue = 10, 0
while n != 0:  # пока в числе есть цифры
    last_digit = n % 10  # получить последнюю цифру
    minvalue, maxvalue = min(minvalue, last_digit), max(maxvalue, last_digit)
    n = n // 10  # удалить последнюю цифру из числа
print("Максимальная цифра равна", maxvalue)
print("Минимальная цифра равна", minvalue)