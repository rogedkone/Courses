
Аве, Цезарь 🌶️

На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются строчными, а прописные – прописными.

Формат входных данных 
На вход программе подается строка текста на английском языке.

Формат выходных данных
Программа должна вывести зашифрованный текст в соответствии с условием задачи.

Примечание. Символы, не являющиеся английскими буквами, не изменяются.

Sample Input 1:

Day, mice. "Year" is a mistake!

Sample Output 1:

Gdb, qmgi. "Ciev" ku b tpzahrl!

Sample Input 2:

my name is Python!

Sample Output 2:

oa reqi ku Veznut!

def encrypt(text: str) -> str:
    words = []

    for word in text.split():
        new_word = ''
        word_len = len([c for c in word if c.isupper() or c.islower()])

        for char in word:
            if char.isupper():
                new_word += chr((ord(char) + word_len - 65) % 26 + 65)
            elif char.islower():
                new_word += chr((ord(char) + word_len - 97) % 26 + 97)
            else:
                new_word += char
        words.append(new_word)

    return ' '.join(words)


text = input()
print(encrypt(text))
