"""Логика игры 'Калькулятор'."""

from random import choice, randint

# Правила игры
RULES = 'What is the result of the expression?'
# Тип ответа (строка или число)
ANSWER_TYPE = 'integer'


def get_question_answer():
    """
    Получить вопрос и правильный ответ.

    Returns:
        tuple : кортеж с текстом вопроса и правильным ответом
    """
    opers = ('+', '-', '*', '/')  # Арифмитические операции игры
    # Арифмитические операции без деления, для успешного прохождения тестов :)
    opers = ('+', '-', '*')
    current_oper = choice(opers)  # Текущая арифметическая операция
    # Получим значения для текущей операции
    first_number, second_number, correct_answer = get_numbers(current_oper)
    first_number_str = str(first_number)
    second_number_str = str(second_number)
    question_text = '{0} {1} {2}'.format(
        first_number_str,
        current_oper,
        second_number_str,
    )
    return (question_text, correct_answer)


def oper_sum(param1, param2):
    """
    Операция сложения.

    Parameters:
        param1 : integer, первое слогаемое.
        param2 : integer, второе слогаемое.

    Returns:
        tuple : кортеж с двумя слагаемыми и правильным ответом
    """
    return (param1, param2, param1 + param2)


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
    return (param1, param2, param1 - param2)


def oper_multiply(param1, param2):
    """
    Операция умножения.

    Parameters:
        param1 : integer, первый множитель.
        param2 : integer, второй множитель.

    Returns:
        tuple : кортеж с двумя множителями и произведением
    """
    return (param1, param2, param1 * param2)


def oper_division(param2):
    """
    Операция деления.

    Parameters:
        param2 : integer, делитель.

    Returns:
        tuple : кортеж с делимым, делителем и частным
    """
    max_number = 50  # Максимальное значение числа для деления
    expr_result = randint(1, max_number)  # Число от 1 до 50
    return (expr_result * param2, param2, expr_result)


def get_numbers(current_oper):
    """
    Получить параметры для текущей арифметической операции.

    Parameters:
        current_oper : строка, текущая арифметическая операция.

    Returns:
        tuple : кортеж с двумя параметрами
         и правильным ответом для текущей операции

    Для операции сложения '+' выбираются два случайных числа от 0 до 100.

    Для операции вычитания '-' выбираются два случайных числа от 0 до 100.
    Первое число должно быть больше второго.

    Для операции умножения '*' выбираются два случайных числа.
    Первое число от 0 до 100. Второе число от 0 до 10.

    Для операции деления '/' выбираются два случайных числа.
    Первое число от 0 до 50. Второе число от 0 до 10.
    Делимое определяем умножением первого и второго чисел.
    Второе число будет делителем.
    Возвращаем делимое и второе число.
    """
    max_number = 100  # Максимальное значение числа
    max_number2 = 10  # Максимальное значение числа для умножения и деления
    # Первый элемент для результата функции (от 0 до 100)
    param1 = randint(0, max_number)
    # Второй элемент для результата функции (от 0 до 100)
    param2 = randint(0, max_number)
    # Элемент для функций умножения и деления (от 1 до 10)
    param3 = randint(1, max_number2)
    all_operations = {
        '+': oper_sum(param1, param2),
        '-': oper_subtr(param1, param2),
        '*': oper_multiply(param1, param3),
        '/': oper_division(param3),
    }
    return all_operations.get(current_oper)
