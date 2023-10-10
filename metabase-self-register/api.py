from fastapi import FastAPI, Request
import requests
import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

# Variaveis
metabase_url="http://200.137.215.27:3000"
usuario_admin="wdsmarques@gmail.com"
senha_admin="wandersondsm123"

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configurar o diretório de arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar o diretório de templates HTML usando Jinja2Templates
templates = Jinja2Templates(directory="templates")

@app.get('/self-register')
async def self_register_new_user(first_name: str, last_name: str, email: str):
    # Recuperando sessao no Metabase
    print('Recuperando sessão no Metabase')
    metabase_session_response = requests.post(url=metabase_url + "/api/session", json={'username': usuario_admin, 'password': senha_admin})
    metabase_session_id = metabase_session_response.json()['id']
    
    # Criando usuario no Metabase
    print(f'Criando usuário no Metabase', first_name, last_name, email)
    metabase_create_user_response = requests.post(url=metabase_url + "/api/user", json={"first_name": first_name, "last_name": last_name, "email": email}, headers={"X-Metabase-session": metabase_session_id})
    
    conteudo_retorno_criacao = metabase_create_user_response.json()
    
    return conteudo_retorno_criacao
    
    
@app.get('/register-page', response_class=HTMLResponse)
async def get_register_page(request: Request):
    return templates.TemplateResponse("self-register.html", {"request": request, "url_metabase": os.environ.get('url_metabase')})