"""Логика игры 'Проверка на чётность'."""

from random import randint

import prompt


def start_game(user_name):
    """
    Игра 'Проверка на чётность'.

    Parameters:
        user_name : строка, имя игрока.
    """
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_of_correct_answers = 0
    while number_of_correct_answers < 3:
        number = randint(0, 1000)
        print('Question: {0}'.format(number))
        user_answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        if user_answer == correct_answer:
            print('Correct!')
            number_of_correct_answers += 1
        else:
            wrong_answer = "'{0}' is wrong answer ;(. Correct answer was '{1}'"
            print(wrong_answer.format(user_answer, correct_answer))
            print("Let's try again, {0}!".format(user_name))
            break
    if number_of_correct_answers == 3:
        print('Congratulations, {0}!'.format(user_name))
