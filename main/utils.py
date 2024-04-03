from argparse import ArgumentParser
import hashlib
import tomllib
from getpass import getpass


with open('.password_salt', 'r') as file:
    PASSWORD_SALT = file.read().strip()


with open('users.toml', 'r') as config_file:
    users = tomllib.loads(config_file.read())


def get_hashsum(password: str) -> str:
    """
    Подсаливает и преобразует строку с паролем в хэш-сумму

    @password: str - пароль от пользователя
    """
    hashsum = hashlib.sha256(
            (password + PASSWORD_SALT).encode()
            ).hexdigest()
    return hashsum


def add_new_user():
    """
    Утилитарная функция позволяющая зарегестрировать нового пользователя.
    В базу пользователей будет сохранено имя и хэш-сумма пароля
    """
    username = input('Введите имя пользователя:')
    password = getpass('Введите имя пользователя:', )
    password_hashsum = get_hashsum(password)
    with open('users.toml', 'a') as file:
        file.write(f"{username} = \"{password_hashsum}\"")


parser = ArgumentParser(
    prog='Журнал обращений',
    description='Выводит журнал обращений в виде сайта. Включает себя логин и базу данных')

parser.add_argument('-n', '--new_user',
                    action='store_true',
                    help='Добавить нового пользователя')                   

__all__ = [
        'users',
        'get_hashsum',
        'add_new_user'
        ]
