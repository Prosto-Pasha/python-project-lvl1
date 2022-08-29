"""Логика игры 'Арифметическая прогрессия'."""

from random import randint

# Правила игры
RULES = 'What number is missing in the progression?'
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10
# Минимальное значение числа в прогрессии,
# минимальный шаг прогрессии,
# минимальное значение для поиска индекса правильного ответа
MIN_NUMBER = 1
MAX_NUMBER = 20  # Максимальное значение первого числа в прогрессии
MAX_STEP = 10  # Максимальный шаг прогрессии


def get_question_answer():
    """
    Получить текст вопроса и правильный ответ для очередного раунда.

    Returns:
        tuple : кортеж с двумя элементами.
            Строка с вопросом и число - правильный ответ.
    """
    progression_length = randint(
        MIN_PROGRESSION_LENGTH,
        MAX_PROGRESSION_LENGTH,
    )
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(MIN_NUMBER, MAX_STEP)
    progression_list = get_progression(first_number, progression_length, step)
    # Индекс загадываемого числа
    lucky_index = randint(MIN_NUMBER, progression_length) - 1
    correct_answer = str(progression_list[lucky_index])
    # Скрываем правильный ответ
    progression_list[lucky_index] = '..'
    question_text = get_progression_string(progression_list)
    return question_text, correct_answer


def get_progression(first_number, progression_length, step)
    """
    Получить арифметическую прогрессию.

    Parameters:
        first_number : число, первый элемент прогрессии.
        progression_length : число, количество элементов в прогрессии.
        step : число, шаг прогрессии

    Returns:
        список : прогрессия
    """
    last_number = first_number + progression_length * step
    return list(range(first_number, last_number, step))


def get_progression_string(progression_list)
    """
    Получить строку из списка.

    Parameters:
        progression_list : список.

    Returns:
        string : строка
    """
    return ' '.join(map(str, progression_list))