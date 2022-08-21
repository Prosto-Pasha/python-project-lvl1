"""Игра 'Проверка на чётность'."""

# !/usr/bin/env python3

from brain_games import common_proc
from brain_games.games import even_game


def main():
    """Основная функция игры 'Проверка на чётность'."""
    game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    user_name = common_proc.welcome_user(game_rules)
    even_game.start_game(user_name)


if __name__ == '__main__':
    main()
