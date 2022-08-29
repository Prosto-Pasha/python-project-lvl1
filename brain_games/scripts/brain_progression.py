"""Игра 'Арифметическая прогрессия'."""

# !/usr/bin/env python3

from brain_games import engine
from brain_games.games import progression_game as game


def main():
    """Запуск игры 'Арифметическая прогрессия'."""
    engine.run(game)


if __name__ == '__main__':
    main()
