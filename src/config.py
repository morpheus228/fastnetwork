from dataclasses import dataclass
import os

from dotenv import load_dotenv


@dataclass
class MYSQLConfig:
    host: str
    password: str
    user: str
    database: str
    port: str


@dataclass
class MongoConfig:
    host: str
    password: str
    user: str
    database: str
    port: str


@dataclass
class OpenAIConfig:
    token: str


@dataclass
class ProxyConfig:
    url: str


@dataclass
class Config:
    proxy: ProxyConfig
    openai: OpenAIConfig
    mysql: MYSQLConfig
    mongo: MongoConfig

    @classmethod
    def set(cls, path: str = '.env'):
        load_dotenv(path)

        cls.mysql = MYSQLConfig(
            host=os.getenv('MYSQL_HOST'),
            password=os.getenv('MYSQL_PASSWORD'),
            user=os.getenv('MYSQL_USER'),
            database=os.getenv('MYSQL_DATABASE'),
            port=os.getenv('MYSQL_PORT'))
        
        cls.openai = OpenAIConfig(
            token=os.getenv('OPENAI_TOKEN'))
        
        cls.proxy = ProxyConfig(
            url=os.getenv('PROXY_URL'))
        
        cls.mongo = MongoConfig(
            host=os.getenv('MONGO_HOST'),
            password=os.getenv('MONGO_PASSWORD'),
            user=os.getenv('MONGO_USER'),
            database=os.getenv('MONGO_DATABASE'),
            port=os.getenv('MONGO_PORT')
        )