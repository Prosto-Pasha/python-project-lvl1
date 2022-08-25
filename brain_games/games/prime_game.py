"""Логика игры 'Простое ли число?'."""

import math
from random import randint

# Правила игры
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
# Тип ответа (строка или число)
ANSWER_TYPE = 'string'


def get_question_answer():
    """
    Получить вопрос и правильный ответ.

    Returns:
        tuple : кортеж с текстом вопроса и правильным ответом
    """
    question_text, correct_answer = get_round()
    return (question_text, correct_answer)


def is_simple(number):
    """
    Проверить, простое ли число.

    Parameters:
        number : число, проверяемое число.

    Returns:
        string : строка : правильный ответ ('yes' или 'no').
    """
    max_index = int(math.sqrt(number))
    index = 2
    while index <= max_index:
        if number % index == 0:
            return 'no'
        index += 1
    return 'yes'


def get_round():
    """
    Получить число и правильный ответ для очередного раунда.

    Returns:
        tuple : кортеж с двумя элементами.
        Число - вопрос и строка - правильный ответ ('yes' или 'no').
    """
    max_number = 1000  # Максимальное число для вопроса
    question_number = randint(1, max_number)  # Число - вопрос от 1 до 1000
    correct_answer = is_simple(question_number)
    return (question_number, correct_answer)
