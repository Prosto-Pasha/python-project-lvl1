"""Игра 'Наибольший общий делитель'."""

# !/usr/bin/env python3

from brain_games import common_proc
from brain_games.games import gcd_game


def main():
    """Основная функция игры 'Калькулятор'."""
    game_rules = 'Find the greatest common divisor of given numbers.'
    user_name = common_proc.welcome_user(game_rules)
    gcd_game.start_game(user_name)


if __name__ == '__main__':
    main()
