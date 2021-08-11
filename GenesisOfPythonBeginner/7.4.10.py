
Количество членов

На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является одно из трех слов: «стоп», «хватит», «достаточно» (маленькими буквами, без кавычек). Напишите программу, которая выводит общее количество членов данной последовательности.

Формат входных данных
На вход программе подается последовательность слов, каждое слово на отдельной строке.

Формат выходных данных
Программа должна вывести общее количество членов данной последовательности.

Sample Input 1:

Skyrim
GTA
Mafia
стоп
Battlefield

Sample Output 1:

3

Sample Input 2:

Yandex
Google
Opera
Safari
хватит
Mozilla

Sample Output 2:

4

Sample Input 3:

Skype
Viber
Telegram
WhatsApp
Discord
достаточно

Sample Output 3:

5

outword, outword_count = "", -1

while outword != "стоп" and outword != "хватит" and outword != "достаточно":
    outword_count += 1
    outword = input()
print(outword_count)
