"""Игра 'Арифметическая прогрессия'."""

# !/usr/bin/env python3

from brain_games import common_proc
from brain_games.games import progression_game


def main():
    """Основная функция игры 'Арифметическая прогрессия'."""
    game_rules = 'What number is missing in the progression?'
    user_name = common_proc.welcome_user(game_rules)
    progression_game.start_game(user_name)


if __name__ == '__main__':
    main()
