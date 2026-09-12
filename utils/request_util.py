import requests
import logging

logger = logging.getLogger(__name__)


class ApiClient:
    def __init__(self, base_url, timeout=10):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def set_token(self, token):
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def get(self, path, params=None):
        url = f"{self.base_url}{path}"
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            logger.info(f"GET {url} status={response.status_code}")
            return response
        except Exception as e:
            logger.error(f"GET {url} error={e}")
            raise

    def post(self, path, json=None):
        url = f"{self.base_url}{path}"
        try:
            response = self.session.post(url, json=json, timeout=self.timeout)
            logger.info(f"POST {url} status={response.status_code}")
            return response
        except Exception as e:
            logger.error(f"POST {url} error={e}")
            raise