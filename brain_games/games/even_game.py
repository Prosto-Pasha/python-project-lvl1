"""Логика игры 'Проверка на чётность'."""

from random import randint

from brain_games import common_proc


def start_game(user_name):
    """
    Игра 'Проверка на чётность'.

    Parameters:
        user_name : строка, имя игрока.
    """
    number_of_correct_answers = 0  # Счётчик правильных ответов
    number_of_rounds = 3  # Число раундов игры, необходимое для победы
    # Если правильных ответов меньше трёх, то продолжаем игру
    while number_of_correct_answers < number_of_rounds:
        number = randint(0, 1000)  # Случайное целое число от 0 до 1000
        common_proc.ask_question(number)  # Задаём вопрос пользователю
        # Узнаём ответ пользователя
        user_answer = common_proc.find_answer('string')
        # Вычисляем правильный ответ
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        number_of_correct_answers += common_proc.check_answer(
            user_answer,
            correct_answer,
            user_name,
        )
    # Поздравим пользователя при трёх правильных ответах
    if number_of_correct_answers == 3:
        common_proc.greet_user(user_name)
