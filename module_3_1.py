calls = 0                                            # Создать переменную calls = 0 вне функций.
# Функция count_calls подсчитывающая вызовы остальных функций.
def count_calls(call):                               # Создать функцию count_calls и изменять в ней значение переменной calls.
    global calls                                     # Используем переменную calls из глобального списка имен
    calls += call                                    # Увеличиваем значение на указанное число (в данном случае на 1) call
    return calls                                     # С помощью оператора return возвращаем данные calls после выполнения работы самой функции.

# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
def string_info(string):                             # Создать функцию string_info с параметром string
    a = []                                           # Создаем список [] переменной а
    a.append(len(string))                            # Добавим в строку а и пределим длину вводимого значения строки
    a.append(string.upper())                         # Строку а вывести в верхнем регистре
    a.append(string.lower())                         # Строку а вывести в нижнем регистре
    count_calls(1)                                   # Вызываем функцию count_calls(1)
    return a                                         # Возвращаем данные строки а после выполнения работы самой функции.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
# False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
def is_contains(string_info, is_contains):           # Создать функцию is_contains с двумя параметрами string и list_to_search
    string_info.lower()                              # Принимаем первый аргумент
    new_is_contains = []
    count_calls(1)
    for i in is_contains:
        new_is_contains.append(i.lower())
    return (string_info.lower() in new_is_contains)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)


