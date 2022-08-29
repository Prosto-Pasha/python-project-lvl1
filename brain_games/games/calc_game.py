"""Логика игры 'Калькулятор'."""

import operator
from random import choice, randint

# Правила игры
RULES = 'What is the result of the expression?'
MIN_NUMBER = 1  # Минимальное значение числа
MAX_NUMBER = 100  # Максимальное значение числа


def get_question_answer():
    """
    Получить вопрос и правильный ответ.

    Returns:
        tuple : кортеж с текстом вопроса и правильным ответом
    """
    # Арифмитическая операция
    current_oper = choice(('+', '-', '*'))
    param1 = randint(MIN_NUMBER, MAX_NUMBER)
    param2 = randint(MIN_NUMBER, MAX_NUMBER)
    if param1 < param2 and current_oper == '-':
        param1, param2 = param2, param1
    # Получим значения для текущей операции
    first_number, second_number, correct_answer = get_numbers(
        current_oper,
        param1,
        param2,
    )
    first_number_str = str(first_number)
    second_number_str = str(second_number)
    question_text = '{0} {1} {2}'.format(
        first_number_str,
        current_oper,
        second_number_str,
    )
    return question_text, str(correct_answer)


def get_numbers(current_oper, param1, param2):
    """
    Получить параметры для текущей арифметической операции.

    Parameters:
        current_oper : строка, текущая арифметическая операция.
        param1 : integer, первый параметр операции.
        param2 : integer, второй параметр операции.

    Returns:
        tuple : кортеж с двумя параметрами
         и правильным ответом для текущей операции
    """
    all_operations = {
        '+': operator.add(param1, param2),
        '-': operator.sub(param1, param2),
        '*': operator.mul(param1, param2),
    }
    return param1, param2, all_operations.get(current_oper)
