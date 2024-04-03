import hashlib
import tomllib


with open('.password_salt', 'r') as file:
    PASSWORD_SALT = file.read().strip()


with open('config.toml', 'r') as config_file:
    users = tomllib.loads(config_file.read())


def get_hashsum(password: str) -> str:
    hashsum = hashlib.sha256(
            (password + PASSWORD_SALT).encode()
            ).hexdigest()
    return hashsum


__all__ = [
        'users',
        'get_hashsum'
        ]
