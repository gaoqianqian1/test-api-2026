from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

app = FastAPI()


# 定义请求体模型
class LoginData(BaseModel):
    username: str
    password: str


# 1. 模拟登录接口
@app.post("/api/login")
def login(data: LoginData):
    # 模拟后端校验逻辑
    if data.username == "admin" and data.password == "123456":
        return {"code": 0, "msg": "登录成功", "token": "mock-token-123"}
    else:
        return {"code": 401, "msg": "账号或密码错误"}


# 2. 模拟获取用户信息接口
@app.get("/api/user/info")
def get_user_info(authorization: str = Header(None)):
    if authorization == "mock-token-123":
        return {"code": 0, "data": {"username": "admin", "role": "tester"}}
    else:
        raise HTTPException(status_code=401, detail="Token无效")
