"""Общие процедуры игр разума."""

import prompt

NUMBER_OF_ROUNDS = 3  # Число раундов игры, необходимое для победы
CORRECT_ANSWER_WEIGHT = 1  # 'Вес' правильного ответа
WRONG_ANSWER_WEIGHT = NUMBER_OF_ROUNDS + 1  # 'Вес' неправильного ответа


def run(game):
    """
    Основная процедура запуска игры.

    Parameters:
        game : модуль игры.
    """
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(player_name))
    print(game.RULES)
    # Если правильных ответов меньше необходимого, то продолжаем игру
    for _ in range(NUMBER_OF_ROUNDS):
        # Получим текст вопроса и правильный ответ
        question_text, correct_answer = game.get_question_answer()
        print('Question: {0}'.format(question_text))
        player_answer = prompt.string('Your answer: ')
        if player_answer == correct_answer:
            # Правильный ответ
            print('Correct!')
        else:
            # Неправильный ответ
            wrong_answer = "'{0}' is wrong answer ;(. Correct answer was '{1}'"
            print(wrong_answer.format(player_answer, correct_answer))
            print("Let's try again, {0}!".format(player_name))
            return
    print('Congratulations, {0}!'.format(player_name))
