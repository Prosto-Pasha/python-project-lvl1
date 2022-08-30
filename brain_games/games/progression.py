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
    initial_term = randint(MIN_NUMBER, MAX_NUMBER)
    common_difference = randint(MIN_NUMBER, MAX_STEP)
    progression_list = get_progression(
        initial_term,
        progression_length,
        common_difference,
    )
    # Индекс загадываемого числа
    lucky_index = randint(MIN_NUMBER, progression_length) - 1
    correct_answer = str(progression_list[lucky_index])
    question_text = stringify(progression_list, lucky_index)
    return question_text, correct_answer


def get_progression(initial_term, progression_length, common_difference):
    """
    Получить арифметическую прогрессию.

    Parameters:
        initial_term : число, первый элемент прогрессии.
        progression_length : число, количество элементов в прогрессии.
        common_difference : число, шаг прогрессии

    Returns:
        список : прогрессия
    """
    last_number = initial_term + progression_length * common_difference
    return list(range(initial_term, last_number, common_difference))


def stringify(progression_list, lucky_index):
    """
    Получить строку из списка.

    Parameters:
        progression_list : список.
        lucky_index : integer, индекс элемента, который нужно скрыть.

    Returns:
        string : строка
    """
    # Скрываем правильный ответ
    progression_list[lucky_index] = '..'
    return ' '.join(map(str, progression_list))
