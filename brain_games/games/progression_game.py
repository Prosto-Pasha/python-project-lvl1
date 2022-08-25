"""Логика игры 'Арифметическая прогрессия'."""

from random import randint

# Правила игры
RULES = 'What number is missing in the progression?'
# Тип ответа (строка или число)
ANSWER_TYPE = 'integer'


def get_question_answer():
    """
    Получить вопрос и правильный ответ.

    Returns:
        tuple : кортеж с текстом вопроса и правильным ответом
    """
    length_of_progression = randint(5, 10)  # Длина прогрессии от 5 до 10 чисел
    question_text, correct_answer = get_round(length_of_progression)
    return (question_text, correct_answer)


def get_round(length_of_progression):
    """
    Получить текст вопроса и правильный ответ для очередного раунда.

    Parameters:
        length_of_progression : integer, количество цифр в прогрессии.

    Returns:
        tuple : кортеж с двумя элементами.
            Строка с вопросом и число - правильный ответ.
    """
    # Максимальное значение первого числа в прогрессиии
    max_first_number = 20
    max_step = 10  # Максимальный шаг прогрессии
    # Первое число в прогрессии от 1 до 20
    first_number = randint(1, max_first_number)
    step = randint(1, max_step)  # Шаг прогрессии от 1 до 10
    # Последнее число в прогрессии
    last_number = first_number + length_of_progression * step
    # Индекс загадываемого числа
    lucky_index = randint(1, length_of_progression) - 1
    progression_list = list(range(first_number, last_number, step))
    correct_answer = progression_list[lucky_index]  # Правильный ответ
    progression_list[lucky_index] = '..'  # Скрываем правильный ответ
    # Преобразуем список в строку
    question_text = ' '.join(map(str, progression_list))
    return (question_text, correct_answer)
