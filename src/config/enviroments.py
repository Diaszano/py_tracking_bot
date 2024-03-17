"""
This module is responsible for loading system environment settings.

It provides functionalities to load and manage environment settings, allowing for easy and flexible system configuration.
"""
from environs import Env
from marshmallow.validate import Length, Range

__env = Env(expand_vars=True)
__env.read_env()

TELEGRAM_API_ID: int = __env.int('TELEGRAM_API_ID', validate=Range(min=1))
TELEGRAM_API_HASH: str = __env.str('TELEGRAM_API_HASH', validate=Length(min=10))
TELEGRAM_BOT_TOKEN: str = __env.str(
    'TELEGRAM_BOT_TOKEN', validate=Length(min=10)
)



if __name__ == '__main__':
    print(TELEGRAM_API_ID, type(TELEGRAM_API_ID))
    print(TELEGRAM_API_HASH, type(TELEGRAM_API_HASH))
    print(TELEGRAM_BOT_TOKEN, type(TELEGRAM_BOT_TOKEN))
