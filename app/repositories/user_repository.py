from uuid import UUID

from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError

try:
    from database import Engine, Session
    from models import User
    from schemas import UserCreate, UserGetOrCreate
    from utils import logger
except ImportError:
    from ..database import Engine, Session
    from ..models import User
    from ..schemas import UserCreate, UserGetOrCreate
    from ..utils import logger


class UserRepository:
    """
    Classe que lida com operações de banco de dados para o modelo User.
    """

    async def create(self, user: UserCreate) -> User:
        """
        Cria um novo usuário no banco de dados.

        Args:
            user (UserCreate): Os dados do usuário a serem criados.

        Returns:
            User: O usuário criado.
        """
        logger.debug(f'Iniciando a criação de um novo usuário: {user}')
        try:
            async with Session(Engine) as session:
                stmt = insert(User).returning(User).values(**user.model_dump())
                result = await session.scalars(stmt)
                usr = result.one()
                await session.commit()
                await session.refresh(usr)
            logger.info(
                f'Novo usuário criado com sucesso. ID: {usr.id}, Telegram ID: {usr.telegram_id}'
            )
            return usr
        except IntegrityError as err:
            logger.error(
                f'Falha ao criar usuário. Usuário com telegram_id({user.telegram_id}) já existe!'
            )
            raise err

    async def get(self, user_id: UUID) -> User | None:
        """
        Obtém um usuário pelo ID do usuário.

        Args:
            user_id (UUID): O ID do usuário a ser buscado.

        Returns:
            User | None: O usuário encontrado ou None se não encontrado.
        """
        logger.debug(f'Buscando usuário com ID: {user_id}')
        try:
            async with Session(Engine) as session:
                stmt = select(User).where(User.id == user_id)
                result = await session.execute(stmt)
                result = result.scalars().first()
            return result
        except Exception as err:
            logger.error(f'Erro ao buscar usuário com ID({user_id}): {err}')
            assert err

    async def get_by_telegram_id(self, telegram_id: int) -> User | None:
        """
        Obtém um usuário pelo ID do telegram.

        Args:
            telegram_id (int): O ID do telegram do usuário a ser buscado.

        Returns:
            User | None: O usuário encontrado ou None se não encontrado.
        """
        logger.debug(f'Buscando usuário com telegram_id: {telegram_id}')
        try:
            if telegram_id <= 0:
                return None

            async with Session(Engine) as session:
                stmt = select(User).where(User.telegram_id == telegram_id)
                result = await session.execute(stmt)
                result = result.scalars().first()
            return result
        except Exception as err:
            logger.error(
                f'Erro ao buscar usuário com telegram_id({telegram_id}): {err}'
            )
            raise err

    async def get_or_create(self, user: UserGetOrCreate) -> User:
        """
        Obtém um usuário pelo ID do usuário ou cria um novo se não encontrado.

        Args:
            user (UserGetOrCreate): Os dados do usuário a serem buscados ou criados.

        Returns:
            User: O usuário encontrado ou criado.
        """
        usr = None
        if user.id is not None:
            usr = await self.get(user.id)

        if usr is not None:
            logger.info('Usuário encontrado.')
            return usr

        usr = await self.get_by_telegram_id(user.telegram_id)

        if usr is not None:
            logger.info('Usuário encontrado.')
            return usr

        return await self.create(UserCreate(**user.model_dump()))
