"""Основной модуль проекта."""

# !/usr/bin/env python3

from brain_games.cli import welcome_user


def print_hello():
    """Выводим приветствие."""
    print('Welcome to the Brain Games!')
    welcome_user()


def main():
    """Основная функция проекта."""
    print_hello()


if __name__ == '__main__':
    main()
