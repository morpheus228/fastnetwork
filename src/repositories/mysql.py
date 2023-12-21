import enum
from sqlalchemy import create_engine, BigInteger, String, Column, DateTime, ForeignKey, Boolean, Integer, Text, Float, Enum, JSON
from sqlalchemy.orm import declarative_base
from datetime import datetime

from config import Config


def get_mysql():
    config = Config.mysql
    uri = f"mysql+pymysql://{config.user}:{config.password}@{config.host}:{config.port}/{config.database}"
    return create_engine(uri)


Base = declarative_base()


class UserCondition(enum.Enum):
    NEW = 0
    INTRODUCTION_COMPLETED= 1
    PROFILE_CREATED = 2


class UserRequestStatus(enum.Enum):
    ACTIVE = 0
    AUTO_COMPLETED= 1
    USER_COMPLETED= 2
    DELETED = 3



class User(Base):
    __tablename__ = 'Users'

    id = Column(BigInteger, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    username = Column(String(100))
    is_visible = Column(Boolean, default=True)
    condition = Column(Enum(UserCondition))
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)


class UserProfile(Base):
    __tablename__ = 'UserProfiles'

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('Users.id', ondelete='CASCADE'))
    # поля профиля
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    is_deleted = Column(Boolean, default=False)


class UserRequest(Base):
    __tablename__ = 'UserRequests'

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('Users.id', ondelete='CASCADE'))
    text = Column(String(1024))
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    status = Column(Enum(UserRequestStatus))
    matches_count = Column(Integer)


class Recommendation(Base):
    __tablename__ = 'Recommendations'

    id = Column(BigInteger, primary_key=True)
    request_id = Column(BigInteger, ForeignKey('UserRequests.id', ondelete='CASCADE'))
    profile_id = Column(BigInteger, ForeignKey('UserProfiles.id', ondelete='CASCADE'))
    score = Column(Float)
    is_selected = Column(Boolean, default=False)
    is_viewed = Column(Boolean, default=False)
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)


class ProfileEmbedding(Base):
    __tablename__ = 'ProfileEmbeddings'

    profile_id = Column(BigInteger, ForeignKey('UserProfiles.id', ondelete='CASCADE'), primary_key=True)
    embedding = Column(Float)