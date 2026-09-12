import pytest
from utils.request_util import ApiClient

# 先用公开的 httpbin 测试框架连通性
BASE_URL = "https://httpbin.ceshiren.com"
# BASE_URL = "http://127.0.0.1:8000"


@pytest.fixture(scope="session")
def api_client():
    return ApiClient(base_url=BASE_URL)
