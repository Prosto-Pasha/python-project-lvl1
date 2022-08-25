"""Логика игры 'Проверка на чётность'."""

from random import randint

# Правила игры
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
# Тип ответа (строка или число)
ANSWER_TYPE = 'string'


def get_question_answer():
    """
    Получить вопрос и правильный ответ.

    Returns:
        tuple : кортеж с текстом вопроса и правильным ответом
    """
    number = randint(0, 1000)  # Случайное целое число от 0 до 1000
    # Вычисляем правильный ответ
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return (str(number), correct_answer)
