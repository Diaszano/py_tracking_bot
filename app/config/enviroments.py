"""
Este módulo é responsável pelo carregamento das variáveis de ambiente do sistema.

Ele contém funcionalidades para carregar e gerenciar as variáveis de ambiente,
simplificando e tornando mais flexível a configuração do sistema.
"""

from logging import INFO
from urllib.parse import ParseResult

from environs import Env
from marshmallow.validate import Length, Range

# Inicialização do ambiente
__env = Env(expand_vars=True, eager=False)
__env.read_env()

# Configurações das variáveis de ambiente relacionadas ao Telegram
with __env.prefixed('TELEGRAM_'):
    with __env.prefixed('API_'):
        TELEGRAM_API_ID: int = __env.int('ID', validate=Range(min=1))
        TELEGRAM_API_HASH: str = __env.str('HASH', validate=Length(min=10))
    with __env.prefixed('BOT_'):
        TELEGRAM_BOT_TOKEN: str = __env.str('TOKEN', validate=Length(min=10))
        TELEGRAM_BOT_NAME: str = __env.str('NAME', validate=Length(min=1))

# Configuração da URL do banco de dados
with __env.prefixed('DATABASE_'):
    DATABASE_URL: ParseResult = __env.url(
        'URL', schemes=['postgresql+asyncpg'], require_tld=False
    )

# Configuração do nível de log
with __env.prefixed('LOG_'):
    LOG_LEVEL: int = __env.log_level('LEVEL', INFO)

# Sela o ambiente após a leitura das variáveis de ambiente
__env.seal()
