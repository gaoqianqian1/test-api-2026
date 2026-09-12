import pytest
import allure
from conftest import BASE_URL


@allure.feature("登录模块-Mock环境")
@pytest.mark.mock
class TestLogin:

    @allure.story("登录接口")
    @pytest.mark.parametrize("username,password,expected_code", [
        ("admin", "123456", 0),  # 正常登录
        ("admin", "wrong", 401),  # 密码错误
    ])
    def test_login(self, api_client, username, password, expected_code):
        # 请求 Mock 接口
        resp = api_client.post("/api/login", json={
            "username": username,
            "password": password
        })
        assert resp.status_code == 200
        assert resp.json()["code"] == expected_code
