"""Игра 'Проверка на чётность'."""

# !/usr/bin/env python3

from brain_games import common_proc
from brain_games.games import even_game as game


def main():
    """Запуск игры 'Проверка на чётность'."""
    common_proc.start_game(game)


if __name__ == '__main__':
    main()
