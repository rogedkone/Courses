
Пересчет временного интервала

Напишите программу для пересчёта величины временного интервала, заданного в минутах, в величину, выраженную в часах и минутах.

Формат входных данных
На вход программе подаётся целое число – количество минут.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

150

Sample Output 1:

150 мин - это 2 час 30 минут.

Sample Input 2:

50

Sample Output 2:

50 мин - это 0 час 50 минут.

Sample Input 3:

240

Sample Output 3:

240 мин - это 4 час 0 минут.

a = int(input())
print(a, "мин - это", a // 60, "час", a % 60, "минут.")
