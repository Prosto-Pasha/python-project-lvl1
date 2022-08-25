"""Логика игры 'Наибольший общий делитель'."""

from random import randint

# Правила игры
RULES = 'Find the greatest common divisor of given numbers.'
# Тип ответа (строка или число)
ANSWER_TYPE = 'integer'


def get_question_answer():
    """
    Получить вопрос и правильный ответ.

    Returns:
        tuple : кортеж с текстом вопроса и правильным ответом
    """
    max_number = 150  # Максимальное число
    number1 = randint(0, max_number)  # Случайное целое число от 1 до 150
    number2 = randint(0, max_number)  # Случайное целое число от 1 до 150
    question_text = '{0} {1}'.format(number1, number2)
    # Вычисляем правильный ответ
    correct_answer = euqlid_gcd(number1, number2)
    return (question_text, correct_answer)


def euqlid_gcd(number1, number2):
    """
    Определяем наибольший общий делитель чисел number1 и number2.

    Методом Евклида.

    Parameters:
        number1 : число, первый параметр.
        number2 : число, второй параметр.

    Returns:
        integer : число, наибольший общий делитель чисел number1 и number2
    """
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 %= number2
        else:
            number2 %= number1
    return number1 + number2
