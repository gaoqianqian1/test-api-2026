def assert_code(response, expected_code=0):
    """断言业务 code"""
    assert response.status_code == 200
    assert response.json().get("code") == expected_code


def assert_key(response, key):
    """断言返回 json 中包含某个 key"""
    assert key in response.json()