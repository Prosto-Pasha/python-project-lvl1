"""Логика игры 'Арифметическая прогрессия'."""

from random import randint

from brain_games import common_proc


def get_round(length_of_progression):
    """
    Получить текст вопроса и правильный ответ для очередного раунда.

    Parameters:
        length_of_progression : integer, количество цифр в прогрессии.

    Returns:
        tuple : кортеж с двумя элементами. Строка с вопросом и число - правильный ответ.
    """
    max_first_number = 20  # Максимальное значение первого числа в прогрессиии
    first_number = randint(1, max_first_number)  # Первое число в прогрессии от 1 до 20
    max_step = 10  # Максимальный шаг прогрессии
    step = randint(1, max_step)  # Шаг прогрессии от 1 до 10
    last_number = first_number + length_of_progression * step  # Последнее число в прогрессии
    lucky_index = randint(1, length_of_progression) - 1  # Индекс загадываемого числа
    progression_list = list(range(first_number, last_number, step))
    correct_answer = progression_list[lucky_index]  # Правильный ответ
    progression_list[lucky_index] = '..'  # Скрываем правильный ответ
    question_text = ' '.join(map(str, progression_list))  # Преобразуем список в строку
    return (question_text, correct_answer)


def start_game(user_name):
    """
    Игра 'Арифметическая прогрессия'.

    Parameters:
        user_name : строка, имя игрока.
    """
    number_of_correct_answers = 0  # Счётчик правильных ответов
    number_of_rounds = 3  # Число раундов игры, необходимое для победы
    length_of_progression = randint(5, 10)  # Длина прогрессии от 5 до 10 чисел
    while number_of_correct_answers < number_of_rounds:  # Если правильных ответов меньше трёх, то продолжаем игру
        question_text, correct_answer = get_round(length_of_progression)
        common_proc.ask_question(question_text)  # Задаём вопрос пользователю
        user_answer = common_proc.find_answer('integer')  # Узнаём ответ пользователя
        number_of_correct_answers += common_proc.check_answer(user_answer, correct_answer, user_name)
    if number_of_correct_answers == 3:  # Поздравим пользователя при трёх правильных ответах
        common_proc.greet_user(user_name)
