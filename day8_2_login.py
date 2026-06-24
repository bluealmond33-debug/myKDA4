""" /login/

userid = 'user' -> 맞으면 로그인 성공 / 틀리면 로그인 실패
password '1234' -> 맞으면 로그인 성공 / 틀리면 비밀번호가 다릅니다. """


from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# CORS 설정 (React에서 접근 가능하도록)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    
