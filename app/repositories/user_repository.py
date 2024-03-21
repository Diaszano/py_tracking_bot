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
    async def create(self, user: UserCreate) -> User:
        logger.debug(f'Inicinado a criação de um novo usuario: {user}')
        try:
            async with Session(Engine) as session:
                stmt = insert(User).returning(User).values(**user.model_dump())
                result = await session.scalars(stmt)
                usr = result.one()
                await session.commit()
                await session.refresh(usr)
            logger.info(
                f'Criado com sucesso novo usuário com ID({usr.id}) e telegram_id({usr.telegram_id})'
            )
            return usr
        except IntegrityError as err:
            logger.error(
                f'Usuário com telegram_id({user.telegram_id}) já existe!'
            )
            raise err

    async def get(self, id: UUID) -> User | None:
        logger.debug(f'Buscando um usuário com id: {id}')
        try:
            async with Session(Engine) as session:
                stmt = select(User).where(User.id == id)
                result = await session.execute(stmt)
                result = result.scalars().first()
            return result
        except Exception as err:
            logger.error(
                f'Ocorreu um erro ao tentar buscar o usuario com id({id}): {err}'
            )
            assert err

    async def get_by_telegram_id(self, telegram_id: int) -> User | None:
        logger.debug(f'Buscando um usuário com telegram_id: {telegram_id}')
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
                f'Ocorreu um erro ao tentar buscar o usuario com telegram_id({telegram_id}): {err}'
            )
            raise err

    async def get_or_create(self, user: UserGetOrCreate) -> User:
        usr = None
        if user.id is not None:
            usr = await self.get(id=user.id)

        if usr is not None:
            return usr

        usr = await self.get_by_telegram_id(user.telegram_id)

        if usr is not None:
            return usr

        return await self.create(UserCreate(**user.model_dump()))
