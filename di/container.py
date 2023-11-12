from dependency_injector import containers, providers
from requests import Session

from config.config import EnvConfig
from elite_core.features.sqlalchemy.repositories.elite_session import EliteSession
from modules.oanda.services.oanda_service import OandaService

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    env_config = providers.Singleton(EnvConfig)

    # region DB
    database_engine = providers.Singleton(
        create_engine, url=env_config().DB_URL
    )

    session_factory = providers.Factory(
        sessionmaker,
        bind=database_engine,
        class_=EliteSession
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
        base_api_url=env_config().OANDA_DEMO_API_URL,
        session=oanda_service_session,
    )
    # end Region
