from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta

from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key="test")

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users_db = {
    "testuser": {
        "username": "testuser",
        "hashed_password": pwd_context.hash("testpassword")
    }
}

oauth_google = OAuth()
oauth_google.register(
    name='google',
    client_id="",
    client_secret="",
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

oauth_github = OAuth()
oauth_github.register(
    name='github',
    client_id="",
    client_secret="",
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username not in users_db:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    if form_data.username != users_db[form_data.username]["username"]:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    if not pwd_context.verify(form_data.password, users_db[form_data.username]["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token_data = {"sub": users_db[form_data.username]["username"], "exp": expire}
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": token, "token_type": "bearer"}

@app.get("/protected")
def protected_route(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {"message": f"Hello {username}"}

class RegisterRequest(BaseModel):
    username: str
    password: str

@app.post("/register")
def register(data: RegisterRequest):
    if data.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = pwd_context.hash(data.password)
    users_db[data.username] = {
        "username": data.username,
        "hashed_password": hashed_password,
    }
    return {"message": "User registered successfully"}

@app.get("/auth/google")
async def login_via_google(request: Request):
    redirect_uri = "http://localhost:8000/auth/google/callback"

    return await oauth_google.google.authorize_redirect(request, redirect_uri)

@app.get("/auth/google/callback")
async def auth_google_callback(request: Request):
    token = await oauth_google.google.authorize_access_token(request)

    user = dict(token)["userinfo"]

    return {"email": user.get("email"), "name": user.get("name")}

@app.get("/auth/github")
async def login_via_github(request: Request):
    redirect_uri = request.url_for('auth_github_callback')
    return await oauth_github.github.authorize_redirect(request, redirect_uri)

@app.get("/auth/github/callback")
async def auth_github_callback(request: Request):
    token = await oauth_github.github.authorize_access_token(request)
    user_resp = await oauth_github.github.get('user', token=token)
    user = user_resp.json()
    return {"name": user.get("name")}
