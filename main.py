from flask import Flask
from flask_restful import Resource, Api
import webbrowser
import threading
import requests
from fastapi import FastAPI
import time

app = FastAPI()
@app.get('/')
def print_name():
    return requests.get('https://api.github.com/').json()