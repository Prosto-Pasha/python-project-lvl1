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
    game_is_over = False
    while number_of_correct_answers < number_of_rounds or game_is_over:  # Если правильных ответов меньше трёх, то продолжаем игру
        number = randint(0, 1000)  # Случайное целое число от 0 до 1000
        common_proc.ask_question(number)  # Задаём вопрос пользователю
        user_answer = common_proc.find_answer('string')  # Узнаём ответ пользователя
        correct_answer = 'yes' if number % 2 == 0 else 'no'  # Вычисляем правильный ответ
        if common_proc.compare_answers(user_answer, correct_answer):  # Сравниваем ответ игрока и правильный ответ
            print('Correct!')
            number_of_correct_answers += 1  # Увеличиваем счётчик правильных ответов
        else:
            common_proc.wrong_answer_report(user_answer, correct_answer)  # Сообщим о неправильном ответе
            print("Let's try again, {0}!".format(user_name))
            game_is_over = True  # Завершаем игру при неправильном ответе
    if number_of_correct_answers == 3:  # Поздравим пользователя при трёх правильных ответах
        common_proc.greet_user(user_name)
