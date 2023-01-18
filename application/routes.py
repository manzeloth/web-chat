import sys 
sys.path.insert(1,"web-chat/run.py")

from run import app
from flask import request, make_response
from flask import redirect, send_file
from flask import render_template

@app.route("/")
def main():
    
    return "HOLA AMIGUITOS"