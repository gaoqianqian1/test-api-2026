import pytest
import allure


@allure.feature("登录模块")
class TestLogin:

    @allure.story("登录接口")
    @pytest.mark.parametrize("username,password", [
        ("admin", "123456"),
        ("admin", "wrong"),
        ("", "123456"),
    ])
    def test_login(self, api_client, username, password):
        # 注意这里：不要传 BASE_URL，直接写 /post
        resp = api_client.post("/post", json={
            "username": username,
            "password": password
        })
        assert resp.status_code == 200
        assert resp.json()["json"]["username"] == username
        assert resp.json()["json"]["password"] == password
