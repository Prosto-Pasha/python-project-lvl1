"""Игра 'Наибольший общий делитель'."""

# !/usr/bin/env python3

from brain_games import engine
from brain_games.games import gcd_game as game


def main():
    """Запуск игры 'Наибольший общий делитель'."""
    engine.run(game)


if __name__ == '__main__':
    main()
