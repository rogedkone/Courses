
Начало столетия

Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля. Если год оканчивается, то выведите «YES», иначе выведите «NO».

Формат входных данных
На вход программе подаётся натуральное число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

2000

Sample Output 1:

YES

Sample Input 2:

1999

Sample Output 2:

NO

Sample Input 3:

3000

Sample Output 3:

YES

a = int(input())

if a % 10 == 0 and a % 100 == 0:
    print("YES")
else:
    print("NO")