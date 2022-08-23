"""Игра 'Простое ли число?'."""

# !/usr/bin/env python3

from brain_games import common_proc
from brain_games.games import prime_game


def main():
    """Основная функция игры 'Простое ли число?'."""
    game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    user_name = common_proc.welcome_user(game_rules)
    prime_game.start_game(user_name)


if __name__ == '__main__':
    main()
