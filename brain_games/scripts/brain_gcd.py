"""Игра 'Наибольший общий делитель'."""

# !/usr/bin/env python3

from brain_games import common_proc
from brain_games.games import gcd_game as game


def main():
    """Запуск игры 'Наибольший общий делитель'."""
    common_proc.start_game(game)


if __name__ == '__main__':
    main()
