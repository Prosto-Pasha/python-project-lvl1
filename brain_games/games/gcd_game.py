"""Логика игры 'Наибольший общий делитель'."""

from random import randint

from brain_games import common_proc


def euqlid_gcd(number1, number2):
    """
    Определяем наибольший общий делитель чисел number1 и number2 по методу Евклида.

    Parameters:
        number1 : число, первый параметр.
        number2 : число, второй параметр.

    Returns:
        integer : число, наибольший общий делитель чисел number1 и number2
    """
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 %= number2
        else:
            number2 %= number1
    return number1 + number2


def start_game(user_name):
    """
    Игра 'Наибольший общий делитель'.

    Parameters:
        user_name : строка, имя игрока.
    """
    number_of_correct_answers = 0  # Счётчик правильных ответов
    number_of_rounds = 3  # Число раундов игры, необходимое для победы
    while number_of_correct_answers < number_of_rounds:  # Если правильных ответов меньше трёх, то продолжаем игру
        max_number = 150  # Максимальное число
        number1 = randint(0, max_number)  # Случайное целое число от 1 до 150
        number2 = randint(0, max_number)  # Случайное целое число от 1 до 150
        question_text = '{0} {1}'.format(number1, number2)
        common_proc.ask_question(question_text)  # Задаём вопрос пользователю
        user_answer = common_proc.find_answer('integer')  # Узнаём ответ пользователя
        correct_answer = euqlid_gcd(number1, number2)  # Вычисляем правильный ответ
        if common_proc.compare_answers(user_answer, correct_answer):  # Сравниваем ответ игрока и правильный ответ
            print('Correct!')
            number_of_correct_answers += 1  # Увеличиваем счётчик правильных ответов
        else:
            common_proc.wrong_answer_report(user_answer, correct_answer)  # Сообщим о неправильном ответе
            print("Let's try again, {0}!".format(user_name))
            break  # Завершаем игру при неправильном ответе
    if number_of_correct_answers == 3:  # Поздравим пользователя при трёх правильных ответах
        common_proc.greet_user(user_name)
