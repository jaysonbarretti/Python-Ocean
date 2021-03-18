from flask import Flask

app = Flask(__name__) #verifica o nome do app

from app import routes

