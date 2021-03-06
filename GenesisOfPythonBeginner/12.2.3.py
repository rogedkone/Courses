
Сумма чисел

На вход программе подается строка текста, содержащая натуральные числа. Напишите программу, которая вставляет между каждым числом знак +, а затем вычисляет сумму полученных чисел.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Строковый метод join() работает только со списком строк.

Sample Input 1:

2 5 11 33 55

Sample Output 1:

2+5+11+33+55=106

Sample Input 2:

1 1 1

Sample Output 2:

1+1+1=3

n = input().split()

my_list = [int(n[i]) for i in range(len(n))]

print(*my_list, sep="+", end="=")
print(sum(my_list))
