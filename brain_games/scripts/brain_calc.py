"""Игра 'Калькулятор'."""

# !/usr/bin/env python3

from brain_games import engine
from brain_games.games import calc_game as game


def main():
    """Запуск игры 'Калькулятор'."""
    engine.run(game)


if __name__ == '__main__':
    main()
