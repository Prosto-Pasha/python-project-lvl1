"""Логика игры 'Калькулятор'."""

from random import choice, randint

from brain_games import common_proc


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
    max_number3 = 50  # Максимальное значение числа для деления
    expr_result = randint(1, max_number3)  # Число от 1 до 50
    return (expr_result * param2, param2, expr_result)


def get_numbers(current_oper):
    """
    Получить параметры для текущей арифметической операции.

    Parameters:
        current_oper : строка, текущая арифметическая операция.

    Returns:
        tuple : кортеж с двумя параметрами и правильным ответом для текущей операции

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
    param1 = randint(0, max_number)  # Первый элемент для результата функции (от 0 до 100)
    param2 = randint(0, max_number)  # Второй элемент для результата функции (от 0 до 100)
    param3 = randint(1, max_number2)  # Элемент для функций умножения и деления (от 1 до 10)
    all_operations = {
        '+': oper_sum(param1, param2),
        '-': oper_subtr(param1, param2),
        '*': oper_multiply(param1, param3),
        '/': oper_division(param3),
    }
    return all_operations.get(current_oper)


def start_game(user_name):
    """
    Игра 'Калькулятор'.

    Parameters:
        user_name : строка, имя игрока.
    """
    number_of_correct_answers = 0  # Счётчик правильных ответов
    number_of_rounds = 3  # Число раундов игры, необходимое для победы
    opers = ('+', '-', '*', '/')  # Арифмитические операции игры
    while number_of_correct_answers < number_of_rounds:  # Если правильных ответов меньше трёх, то продолжаем игру
        current_oper = choice(opers)  # Текущая арифметическая операция
        first_number, second_number, correct_answer = get_numbers(current_oper)  # Получим значения для текущей операции
        first_number_str = str(first_number)
        second_number_str = str(second_number)
        question_text = '{0} {1} {2}'.format(first_number_str, current_oper, second_number_str)
        common_proc.ask_question(question_text)  # Задаём вопрос пользователю
        user_answer = common_proc.find_answer('integer')  # Узнаём ответ пользователя
        number_of_correct_answers += common_proc.check_answer(user_answer, correct_answer, user_name)
    if number_of_correct_answers == 3:  # Поздравим пользователя при трёх правильных ответах
        common_proc.greet_user(user_name)
