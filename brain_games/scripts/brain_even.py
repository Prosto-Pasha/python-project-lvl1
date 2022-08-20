"""Игра 'Проверка на чётность'."""

# !/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.even_game import start_game


def print_hello():
    """
    Выводим приветствие. Знакомимся с игроком. И возвращаем его имя.

    Returns:
            string : player name
    """
    print('Welcome to Brain Games!')
    return welcome_user()


def main():
    """Основная функция игры 'Проверка на чётность'."""
    user_name = print_hello()
    start_game(user_name)


if __name__ == '__main__':
    main()
