"""Знакомимся с игроком и приветствуем его."""

import prompt


def welcome_user():
    """
    Знакомимся с игроком и приветствуем его.

    Returns:
            string : player name
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name
