from app.database.models import async_session
from app.database.models import User, Category, Item
from sqlalchemy import select


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.id == tg_id))

    if not user:
        session.add(User(id=tg_id))
        await session.commit()
