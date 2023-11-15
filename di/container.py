import psycopg2
from dependency_injector import containers, providers
from requests import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.config import EnvConfig
from elite_core.features.sqlalchemy.repositories.abstract_repository import AbstractRepository
from modules.oanda.services.oanda_service import OandaService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    # region DB
    database_engine = providers.Singleton(
        create_engine,
        url=EnvConfig.DB_URL
    )

    pyscopg2_connection = psycopg2.connect(
        user="postgres",
        password=EnvConfig.DB_PASSWORD,
        host='127.0.0.1',
        port='5432',
        database=EnvConfig.DB_NAME,
    )

    psycopg2_cursor = pyscopg2_connection.cursor()

    repository_factory = providers.Factory(
        sessionmaker,
        bind=database_engine,
        class_=AbstractRepository
    )
    # end Region

    # region HTTP
    request_session_factory = providers.Factory(
        Session
    )
    # end Region

    # region Oanda
    oanda_service_session = request_session_factory()

    oanda_service = providers.Factory(
        OandaService,
        base_api_url=EnvConfig.OANDA_DEMO_API_URL,
        session=oanda_service_session,
    )
    # end Region
