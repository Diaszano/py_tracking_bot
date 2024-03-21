"""
This module is responsible for loading system environment settings.

It provides functionalities to load and manage environment settings, allowing for easy and flexible system configuration.
"""
from logging import INFO
from urllib.parse import ParseResult

from environs import Env
from marshmallow.validate import Length, Range

__env = Env(expand_vars=True, eager=False)
__env.read_env()

with __env.prefixed('TELEGRAM_'):
    with __env.prefixed('API_'):
        TELEGRAM_API_ID: int = __env.int('ID', validate=Range(min=1))
        TELEGRAM_API_HASH: str = __env.str('HASH', validate=Length(min=10))
    with __env.prefixed('BOT_'):
        TELEGRAM_BOT_TOKEN: str = __env.str('TOKEN', validate=Length(min=10))
        TELEGRAM_BOT_NAME: str = __env.str('NAME', validate=Length(1))

with __env.prefixed('DATABASE_'):
    DATABASE_URL: ParseResult = __env.url(
        'URL', schemes=['postgresql+asyncpg'], require_tld=False
    )

with __env.prefixed('LOG_'):
    LOG_LEVEl: int = __env.log_level('LEVEL', INFO)

__env.seal()

if __name__ == '__main__':
    print(TELEGRAM_API_ID, type(TELEGRAM_API_ID))
    print(TELEGRAM_API_HASH, type(TELEGRAM_API_HASH))
    print(TELEGRAM_BOT_TOKEN, type(TELEGRAM_BOT_TOKEN))
    print(DATABASE_URL, type(DATABASE_URL))
