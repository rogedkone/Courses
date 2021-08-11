
Змеиный регистр

Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

Примечание 1. Почитать подробнее о стилях именования можно тут.

Примечание 2. Следующий программный код:

print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))

должен выводить:

this_is_camel_cased
is_prime_number

def convert_to_python_case(text):
    s = ""
    for i in range(len(text)):
        if text[i].isupper():
            s += "_" + text[i].lower()
        elif text[i].isdigit():
            s += text[i]
        else:
            s += text[i].lower()
    return s[1::]
# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
