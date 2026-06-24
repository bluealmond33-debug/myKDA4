""" /login/

userid = 'user' -> 맞으면 로그인 성공 / 틀리면 로그인 실패
password '1234' -> 맞으면 로그인 성공 / 틀리면 비밀번호가 다릅니다. """


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Login(BaseModel):
    userid: str
    password: str

@app.post("/login/")
def read_login(login: Login) -> dict:
    a_id = "user"
    a_password = "1234"

    if login.userid == a_id and login.password == a_password:
        return {"message": "로그인 성공"}

    return {"error": "id 혹은 비밀번호가 다릅니다."}
    
