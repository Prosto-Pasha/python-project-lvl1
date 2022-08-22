"""Логика игры 'Калькулятор'."""

from random import choice, randint

from brain_games import common_proc


def get_numbers(current_oper):
    """
    Получить параметры для текущей арифметической опреации.

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
    max_number3 = 50  # Максимальное значение числа для деления
    param1 = randint(0, max_number)  # Первый элемент для результата функции (от 0 до 100)
    param2 = randint(0, max_number)  # Второй элемент для результата функции (от 0 до 100)
    param3 = randint(0, max_number2)  # Элемент для функций умножения и деления (от 0 до 10)
    correct_answer = 0  # Правильный результат функции
    if current_oper == '+':
        correct_answer = param1 + param2
    elif current_oper == '-':
        if param1 < param2:
            param1, param2 = param2, param1
        correct_answer = param1 - param2
    elif current_oper == '*':
        param2 = param3
        correct_answer = param1 * param2
    elif current_oper == '/':
        expr_result = randint(0, max_number3)  # Число от 0 до 50
        param2 = param3
        param1 = expr_result * param2
        correct_answer = param1 / param2
    return (param1, param2, correct_answer)


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
