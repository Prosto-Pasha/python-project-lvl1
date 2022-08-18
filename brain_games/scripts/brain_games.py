#!/usr/bin/env python3

from brain_games.cli import welcome_user


def print_hello():
    print('Welcome to Brain Games!')
    welcome_user()

def main():
    print_hello()

if __name__ == '__main__':
    main()

