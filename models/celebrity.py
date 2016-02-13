from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, BigInteger, String, Boolean
from sqlalchemy.orm import relationship
from .base import Base


subject_director_table = Table('subjects_directors_association', Base.metadata,
    Column('subject_id', Integer, ForeignKey('subjects.id')),
    Column('celebrity_id', Integer, ForeignKey('celebrities.id'))
)

subject_playwright_table = Table('subjects_playwrights_association', Base.metadata,
    Column('subject_id', Integer, ForeignKey('subjects.id')),
    Column('celebrity_id', Integer, ForeignKey('celebrities.id'))
)

subject_actor_table = Table('subjects_actors_association', Base.metadata,
    Column('subject_id', Integer, ForeignKey('subjects.id')),
    Column('celebrity_id', Integer, ForeignKey('celebrities.id'))
)


class Celebrity(Base):
    __tablename__ = 'celebrities'

    id = Column(Integer, primary_key=True)
    douban_id = Column(String, unique=True)
    douban_url = Column(String)
    name = Column(String)
    name_en = Column(String)
    aliases = Column(String)
    aliases_en = Column(String)
    sex = Column(String)
    cover = Column(String)
    thumbnail_cover = Column(String)
    website = Column(String)
    gender = Column(String)
    birthday = Column(String)
    born_place = Column(String)
    family = Column(String)
    professions = Column(String)
    constellation = Column(String)
    photos = Column(String)
    thumbnail_photos = Column(String)
    imdb_number = Column(String)
    summary = Column(String)

    director_subjects = relationship("Subject",
        secondary=subject_director_table,
        backref='directors'
    )

    playwright_subjects = relationship("Subject",
        secondary=subject_playwright_table,
        backref='playwrights'
    )

    actor_subjects = relationship("Subject",
        secondary=subject_actor_table,
        backref='actors'
    )
