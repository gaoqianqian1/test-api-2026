class LoginApi:
    def __init__(self, client):
        self.client = client

    def login(self, username, password):
        return self.client.post("/post", json={
            "username": username,
            "password": password
        })