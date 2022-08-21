"""Игра 'Калькулятор'."""

# !/usr/bin/env python3

from brain_games import common_proc
from brain_games.games import calc_game


def main():
    """Основная функция игры 'Калькулятор'."""
    game_rules = 'What is the result of the expression?'
    user_name = common_proc.welcome_user(game_rules)
    calc_game.start_game(user_name)


if __name__ == '__main__':
    main()
