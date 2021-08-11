
Все вместе 2

Дано натуральное число. Напишите программу, которая вычисляет:

    количество цифр 3 в нем;
    сколько раз в нем встречается последняя цифра;
    количество четных цифр;
    сумму его цифр, больших пяти;
    произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
    сколько раз в нем встречается цифры 0 и 5 (всего суммарно).

Формат входных данных 
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке.

Sample Input 1:

56639

Sample Output 1:

1
1
2
21
9
1

Sample Input 2:

56689932106

Sample Output 2:

1
3
6
44
648
2

Sample Input 3:

255

Sample Output 3:

0
2
1
0
1
2

num = int(input())
cifra3=0
posl_cifra=num%10
count_posl_cifra=0
count_chet_cifr=0
sum_cifr5=0
proiz_cifr7=1
count_0_5=0
while num!=0:
    last_digit = num % 10
    if last_digit==3:
        cifra3+=1
    if last_digit==posl_cifra:
        count_posl_cifra+=1
    if last_digit%2==0:
        count_chet_cifr+=1
    if last_digit>5:
        sum_cifr5+=last_digit
    if last_digit>7:
        proiz_cifr7*=last_digit
    if last_digit==0 or last_digit==5:
        count_0_5+=1
    num = num // 10
print(cifra3)
print(count_posl_cifra)
print(count_chet_cifr)
print(sum_cifr5)
print(proiz_cifr7)
print(count_0_5)
