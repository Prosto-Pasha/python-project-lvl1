"""Игра 'Арифметическая прогрессия'."""

# !/usr/bin/env python3

from brain_games import common_proc
from brain_games.games import progression_game as game


def main():
    """Запуск игры 'Арифметическая прогрессия'."""
    common_proc.start_game(game)


if __name__ == '__main__':
    main()
