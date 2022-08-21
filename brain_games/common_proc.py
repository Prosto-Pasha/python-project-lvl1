"""Общие процедуры игр разума."""

import prompt


def welcome_user(game_rules):
    """
    Знакомимся с игроком и приветствуем его.

    Parameters:
        game_rules : строка, правила игры.

    Returns:
        string : player name
    """
    print('Welcome to Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(game_rules)
    return name


def ask_question(question):
    """
    Задать вопрос.

    Parameters:
        question : строка, текст вопроса.
    """
    print('Question: {0}'.format(question))


def find_answer(answer_type):
    """
    Узнать ответ игрока.

    Parameters:
        answer_type : строка, тип значения ответа.

    Returns:
            string : ответ игрока
    """
    user_answer = ''
    if answer_type == 'string':
        user_answer = prompt.string('Your answer: ')
    elif answer_type == 'integer':
        user_answer = prompt.integer('Your answer: ')
    return user_answer


def compare_answers(user_answer, correct_answer):
    """
    Узнать ответ игрока.

    Parameters:
        user_answer : произвольный : ответ игрока.
        correct_answer : произвольный : правильный ответ.

    Returns:
            bool : результат сравнения ответа игрока с правильным ответом
    """
    return user_answer == correct_answer


def wrong_answer_report(user_answer, correct_answer):
    """
    Сообщить о неправильном ответе игрока.

    Parameters:
        user_answer : произвольный : ответ игрока.
        correct_answer : произвольный : правильный ответ.
    """
    wrong_answer = "'{0}' is wrong answer ;(. Correct answer was '{1}'"
    print(wrong_answer.format(user_answer, correct_answer))


def greet_user(user_name):
    """
    Поздравить игрока с победой.

    Parameters:
        user_name : строка, имя игрока.
    """
    print('Congratulations, {0}!'.format(user_name))
