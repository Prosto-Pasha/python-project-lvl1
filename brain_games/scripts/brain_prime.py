"""Игра 'Простое ли число?'."""

# !/usr/bin/env python3

from brain_games import common_proc
from brain_games.games import prime_game as game


def main():
    """Запуск игры 'Простое ли число?'."""
    common_proc.start_game(game)


if __name__ == '__main__':
    main()
