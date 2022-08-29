"""Игра 'Простое ли число?'."""

# !/usr/bin/env python3

from brain_games import engine
from brain_games.games import prime_game as game


def main():
    """Запуск игры 'Простое ли число?'."""
    engine.run(game)


if __name__ == '__main__':
    main()
