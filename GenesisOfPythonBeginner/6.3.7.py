
Футбольная команда

Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:

«Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».

Формат входных данных
На вход программе подаётся строка – название футбольной команды.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

Barcelona

Sample Output 1:

Футбольная команда Barcelona имеет длину 9 символов

Sample Input 2:

Real Madrid

Sample Output 2:

Футбольная команда Real Madrid имеет длину 11 символов

Sample Input 3:

Manchester United

Sample Output 3:

Футбольная команда Manchester United имеет длину 17 символов

Sample Input 4:

Milan

Sample Output 4:

Футбольная команда Milan имеет длину 5 символов

comname = str(input())

print("Футбольная команда " + comname + " имеет длину " + str(len(comname)) + " символов")
