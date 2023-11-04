import asyncio
import aiohttp
import re
from more_itertools import chunked
import requests
from datetime import datetime
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME


CHUCK_SIZE: int = 10
PG_DSN = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

total = requests.get('https://swapi.dev/api/people/').json()['count']


engine = create_async_engine(PG_DSN)
Base = declarative_base()


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)  # ID персонажа
    birth_year = Column(String)
    eye_color = Column(String)
    films = Column(String)
    gender = Column(String)
    hair_color = Column(String)
    height = Column(String)
    homeworld = Column(String)
    mass = Column(String)
    name = Column(String)
    skin_color = Column(String)
    species = Column(String)
    starships = Column(String)
    vehicles = Column(String)


async def get_people(session, people_id):
    result = await session.get(f'https://swapi.dev/api/people/{people_id}')
    return await result.json()


async def get_names(session, url_list, field_name):
    r = []
    for url in url_list:
        result = await session.get(url)
        res = await result.json()
        r.append(res[field_name])
    return r


async def get_name(session, url, field_name):
    result = await session.get(url)
    res = await result.json()
    return res[field_name]


async def get_homeworld_name(session, url):
    with await session.get(url) as response:
        return await response.json()


async def main():
    async with engine.begin() as conn:  # создание соединения
        await conn.run_sync(Base.metadata.create_all)  # создание таблиц
        await conn.commit()
    async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with aiohttp.ClientSession() as web_session:
        for chunk_id in chunked(range(1, total + 1), CHUCK_SIZE):
            coros = [get_people(web_session, i) for i in chunk_id]
            result = await asyncio.gather(*coros)

            # --- запись данных в БД ---
            people_list = []
            for item in result:
                films = await get_names(web_session, item.get('films', []), 'title')
                species = await get_names(web_session, item.get('species', []), 'name')
                starships = await get_names(web_session, item.get('starships', []), 'name')
                vehicles = await get_names(web_session, item.get('vehicles', []), 'name')
                planet = await get_name(web_session, item.get('homeworld'), 'name')
                people_list.append(People(
                    id=int(re.search('\d+', item.get('url', '0')).group(0)),
                    birth_year=item.get('birth_year'),
                    eye_color=item.get('eye_color'),
                    films=', '.join(films),
                    gender=item.get('gender'),
                    hair_color=item.get('hair_color'),
                    height=item.get('height'),
                    homeworld=planet,
                    mass=item.get('mass'),
                    name=item.get('name'),
                    skin_color=item.get('skin_color'),
                    species=','.join(species),
                    starships=','.join(starships),
                    vehicles=','.join(vehicles)
                ))

            async with async_session_maker() as orm_session:
                orm_session.add_all(people_list)
                await orm_session.commit()


start = datetime.now()
asyncio.run(main())
end = datetime.now()
print(end - start)
