"""Логика игры 'Простое ли число?'."""

import math
from random import randint

from brain_games import common_proc


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
        tuple : кортеж с двумя элементами. Число - вопрос и строка - правильный ответ ('yes' или 'no').
    """
    max_number = 1000  # Максимальное число для вопроса
    question_number = randint(1, max_number)  # Число - вопрос от 1 до 1000
    correct_answer = is_simple(question_number)
    return (question_number, correct_answer)


def start_game(user_name):
    """
    Игра 'Простое ли число?'.

    Parameters:
        user_name : строка, имя игрока.
    """
    number_of_correct_answers = 0  # Счётчик правильных ответов
    number_of_rounds = 3  # Число раундов игры, необходимое для победы
    while number_of_correct_answers < number_of_rounds:  # Если правильных ответов меньше трёх, то продолжаем игру
        question_text, correct_answer = get_round()
        common_proc.ask_question(question_text)  # Задаём вопрос пользователю
        user_answer = common_proc.find_answer('string')  # Узнаём ответ пользователя
        number_of_correct_answers += common_proc.check_answer(user_answer, correct_answer, user_name)
    if number_of_correct_answers == 3:  # Поздравим пользователя при трёх правильных ответах
        common_proc.greet_user(user_name)
