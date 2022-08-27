"""Логика игры 'Арифметическая прогрессия'."""

from random import randint

# Правила игры
RULES = 'What number is missing in the progression?'
MIN_PROGRESSION_NUMBER = 5  # Минимальная длина прогрессии
MAX_PROGRESSION_NUMBER = 10  # Максимальная длина прогрессии
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
    # Длина прогрессии
    length_of_progression = randint(
        MIN_PROGRESSION_NUMBER,
        MAX_PROGRESSION_NUMBER,
    )
    # Первое число в прогрессии
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    # Шаг прогрессии
    step = randint(MIN_NUMBER, MAX_STEP)
    # Последнее число в прогрессии
    last_number = first_number + length_of_progression * step
    # Индекс загадываемого числа
    lucky_index = randint(MIN_NUMBER, length_of_progression) - 1
    progression_list = list(range(first_number, last_number, step))
    # Правильный ответ
    correct_answer = progression_list[lucky_index]
    # Скрываем правильный ответ
    progression_list[lucky_index] = '..'
    # Преобразуем список в строку
    question_text = ' '.join(map(str, progression_list))
    return question_text, str(correct_answer)
