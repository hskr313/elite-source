from abc import ABC, abstractmethod
from typing import TypeVar, Any, Dict

from requests import Session

from elite_core.features.http.http_service import HttpService


class AbstractExchangeService(HttpService, ABC):
    def __init__(self, base_api_url: str, session: Session):
        super().__init__(base_api_url, session)

    @abstractmethod
    def get_pairs(self) -> Dict[str, Any]:
        pass
