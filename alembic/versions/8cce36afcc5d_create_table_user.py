"""create table user

Revision ID: 8cce36afcc5d
Revises:
Create Date: 2024-03-24 20:30:21.658126
"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '8cce36afcc5d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    Realiza a criação do migração da tabela do Usuário no banco de dados
    """
    op.create_table(
        'user',
        sa.Column(
            'id',
            sa.Uuid(),
            server_default=sa.text('gen_random_uuid()'),
            nullable=False,
            comment='Identificador único do usuário',
        ),
        sa.Column(
            'telegram_id',
            sa.BigInteger(),
            nullable=True,
            comment='ID do Telegram do usuário',
        ),
        sa.Column(
            'updated_at',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=False,
            comment='Última data de atualização dos dados',
        ),
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=False,
            comment='Data de criação dos dados',
        ),
        sa.PrimaryKeyConstraint('id'),
        comment='Armazena todos os usuários do sistema',
    )
    op.create_index(
        op.f('ix_user_telegram_id'), 'user', ['telegram_id'], unique=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """
    Realiza a remoção da tabela do usuário no banco de dados
    """
    op.drop_index(op.f('ix_user_telegram_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
