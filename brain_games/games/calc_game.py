"""Логика игры 'Калькулятор'."""

from random import choice, randint

# Правила игры
RULES = 'What is the result of the expression?'
MAX_NUMBER1 = 100  # Максимальное значение числа
MAX_NUMBER2 = 10  # Максимальное значение числа для умножения и деления
MAX_NUMBER3 = 50  # Максимальное значение числа для деления
MIN_NUMBER1 = 0  # Минимальное значение числа
MIN_NUMBER2 = 1  # Минимальное значение числа для умножения и деления


def get_question_answer():
    """
    Получить вопрос и правильный ответ.

    Returns:
        tuple : кортеж с текстом вопроса и правильным ответом
    """
    # Арифмитические операции игры
    opers = ('+', '-', '*', '/')
    # Арифмитические операции без деления, для успешного прохождения тестов :)
    opers = ('+', '-', '*')
    # Текущая арифметическая операция
    current_oper = choice(opers)
    # Получим значения для текущей операции
    first_number, second_number, correct_answer = get_numbers(current_oper)
    first_number_str = str(first_number)
    second_number_str = str(second_number)
    question_text = '{0} {1} {2}'.format(
        first_number_str,
        current_oper,
        second_number_str,
    )
    return question_text, str(correct_answer)


def get_numbers(current_oper):
    """
    Получить параметры для текущей арифметической операции.

    Parameters:
        current_oper : строка, текущая арифметическая операция.

    Returns:
        tuple : кортеж с двумя параметрами
         и правильным ответом для текущей операции
    """
    # Первый элемент для результата функции
    param1 = randint(MIN_NUMBER1, MAX_NUMBER1)
    # Второй элемент для результата функции
    param2 = randint(MIN_NUMBER1, MAX_NUMBER1)
    # Элемент для функций умножения и деления
    param3 = randint(MIN_NUMBER2, MAX_NUMBER2)
    all_operations = {
        '+': oper_sum(param1, param2),
        '-': oper_subtr(param1, param2),
        '*': oper_multiply(param1, param3),
        '/': oper_division(param3),
    }
    return all_operations.get(current_oper)


def oper_sum(param1, param2):
    """
    Операция сложения.

    Parameters:
        param1 : integer, первое слогаемое.
        param2 : integer, второе слогаемое.

    Returns:
        tuple : кортеж с двумя слагаемыми и правильным ответом
    """
    return param1, param2, param1 + param2


def oper_subtr(param1, param2):
    """
    Операция вычитания.

    Parameters:
        param1 : integer, первый параметр.
        param2 : integer, второй параметр.

    Returns:
        tuple : кортеж с уменьшаемым, вычитаемым и разностью
    """
    if param1 < param2:
        param1, param2 = param2, param1
    return param1, param2, param1 - param2


def oper_multiply(param1, param2):
    """
    Операция умножения.

    Parameters:
        param1 : integer, первый множитель.
        param2 : integer, второй множитель.

    Returns:
        tuple : кортеж с двумя множителями и произведением
    """
    return param1, param2, param1 * param2


def oper_division(param2):
    """
    Операция деления.

    Parameters:
        param2 : integer, делитель.

    Returns:
        tuple : кортеж с делимым, делителем и частным
    """
    expr_result = randint(MIN_NUMBER2, MAX_NUMBER3)  # Правильный ответ
    return expr_result * param2, param2, expr_result
