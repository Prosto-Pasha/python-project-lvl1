"""Общие процедуры игр разума."""

import prompt

NUMBER_OF_ROUNDS = 3  # Число раундов игры, необходимое для победы
CORRECT_ANSWER_WEIGHT = 1  # 'Вес' правильного ответа
WRONG_ANSWER_WEIGHT = NUMBER_OF_ROUNDS + 1  # 'Вес' неправильного ответа


def start_game(game):
    """
    Основная процедура запуска игры.

    Parameters:
        game : модуль игры.
    """
    player_name = welcome_player()
    # Выводим правила игры
    print(game.RULES)
    number_of_correct_answers = 0  # Счётчик правильных ответов
    # Если правильных ответов меньше необходимого, то продолжаем игру
    while number_of_correct_answers < NUMBER_OF_ROUNDS:
        # Получим текст вопроса и правильный ответ
        question_text, correct_answer = game.get_question_answer()
        # Задаём вопрос игроку
        print('Question: {0}'.format(question_text))
        # Узнаём ответ игрока
        player_answer = prompt.string('Your answer: ')
        number_of_correct_answers += check_answer(
            player_answer,
            correct_answer,
            player_name,
        )
    # Поздравим игрока при необходимом количестве правильных ответов
    if number_of_correct_answers == 3:
        print('Congratulations, {0}!'.format(player_name))


def welcome_player():
    """
    Знакомимся с игроком и приветствуем его.

    Returns:
        string : player name
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def check_answer(player_answer, correct_answer, player_name):
    """
    Проверить ответ игрока, вывести результат проверки и вернуть 'вес' ответа.

    Parameters:
        player_answer : строка : ответ игрока.
        correct_answer : строка : правильный ответ.
        player_name : строка : имя игрока.

    Returns:
            integer : 'вес' ответа игрока.
    """
    # Сравниваем ответ игрока и правильный ответ
    if player_answer == correct_answer:
        # Правильный ответ
        print('Correct!')
        return CORRECT_ANSWER_WEIGHT
    # Неправильный ответ
    wrong_answer = "'{0}' is wrong answer ;(. Correct answer was '{1}'"
    print(wrong_answer.format(player_answer, correct_answer))
    print("Let's try again, {0}!".format(player_name))
    return WRONG_ANSWER_WEIGHT
