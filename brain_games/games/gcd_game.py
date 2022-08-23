"""Логика игры 'Наибольший общий делитель'."""

from random import randint

from brain_games import common_proc


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


def start_game(user_name):
    """
    Игра 'Наибольший общий делитель'.

    Parameters:
        user_name : строка, имя игрока.
    """
    number_of_correct_answers = 0  # Счётчик правильных ответов
    number_of_rounds = 3  # Число раундов игры, необходимое для победы
    # Если правильных ответов меньше трёх, то продолжаем игру
    while number_of_correct_answers < number_of_rounds:
        max_number = 150  # Максимальное число
        number1 = randint(0, max_number)  # Случайное целое число от 1 до 150
        number2 = randint(0, max_number)  # Случайное целое число от 1 до 150
        question_text = '{0} {1}'.format(number1, number2)
        common_proc.ask_question(question_text)  # Задаём вопрос пользователю
        # Узнаём ответ пользователя
        user_answer = common_proc.find_answer('integer')
        # Вычисляем правильный ответ
        correct_answer = euqlid_gcd(number1, number2)
        number_of_correct_answers += common_proc.check_answer(
            user_answer,
            correct_answer,
            user_name,
        )
    # Поздравим пользователя при трёх правильных ответах
    if number_of_correct_answers == 3:
        common_proc.greet_user(user_name)
