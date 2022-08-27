"""Логика игры 'Проверка на чётность'."""

from random import randint

# Правила игры
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 0  # Минимальное значение числа
MAX_NUMBER = 1000  # Максимальное значение числа


def get_question_answer():
    """
    Получить вопрос и правильный ответ.

    Returns:
        tuple : кортеж с текстом вопроса и правильным ответом
    """
    number = randint(MIN_NUMBER, MAX_NUMBER)  # Случайное целое число
    # Вычисляем правильный ответ
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return str(number), correct_answer
