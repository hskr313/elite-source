from abc import ABC
from typing import Any, Dict, Optional
from requests import Session, Response, HTTPError
import urllib.parse

from elite_core.exceptions.http_exception import HttpResponseException

class HttpService(ABC):

    def __init__(self, base_api_url: str, session: Session) -> None:
        self.base_api_url = base_api_url
        self.session = session

    def _build_url(self, endpoint: str) -> str:
        return urllib.parse.urljoin(self.base_api_url, endpoint)

    def _handle_response(self, response: Response) -> Dict[str, Any]:
        try:
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            raise HttpResponseException(f"HTTP error occurred: {http_err}")
        except ValueError as json_err:
            raise HttpResponseException(f"JSON decode error: {json_err}")

    def _get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        full_url = self._build_url(url)
        response = self.session.get(full_url, params=params)
        return self._handle_response(response)

    def _post(self, url: str, body: Dict[str, Any]) -> Dict[str, Any]:
        full_url = self._build_url(url)
        response = self.session.post(full_url, json=body)
        return self._handle_response(response)

    def _patch(self, url: str, body: Dict[str, Any]) -> Dict[str, Any]:
        full_url = self._build_url(url)
        response = self.session.patch(full_url, json=body)
        return self._handle_response(response)

    def _put(self, url: str, body: Dict[str, Any]) -> Dict[str, Any]:
        full_url = self._build_url(url)
        response = self.session.put(full_url, json=body)
        return self._handle_response(response)

    def _delete(self, url: str, body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        full_url = self._build_url(url)
        response = self.session.delete(full_url, json=body)
        return self._handle_response(response)

    def close(self) -> None:
        self.session.close()

