
Шифр Цезаря 🌶️

Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям и использует шифр Цезаря. Это их и подвело, ведь данный шифр очень простой. Однако в постапокалипсисе люди плохо знают все тонкости довоенного мира, поэтому ученые из НКР не могут понять как именно нужно декодировать данные сообщения. Напишите программу для декодирования этого шифра.

Формат входных данных
В первой строке дается число n  (1≤ n≤ 25)n \, (1 \le n \le 25)n (1≤ n≤ 25) – сдвиг, во второй строке даётся закодированное сообщение в виде строки со строчными латинскими буквами.

Формат выходных данных
Программа должна вывести одну строку – декодированное сообщение. Обратите внимание, что нужно декодировать сообщение, а не закодировать.

Sample Input 1:

1
bwfusvfupdbftbs

Sample Output 1:

avetruetocaesar

Sample Input 2:

14
fsfftsfufksttskskt

Sample Output 2:

rerrfergrweffewewf

n = int(input())
a = input()

for i in a:
    k = ord(i)-n
    if k < 97:
        k = k + 26
    print(chr(k), end = '')
