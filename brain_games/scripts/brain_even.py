"""Игра 'Проверка на чётность'."""

# !/usr/bin/env python3

from brain_games import engine
from brain_games.games import even as game


def main():
    """Запуск игры 'Проверка на чётность'."""
    engine.run(game)


if __name__ == '__main__':
    main()
