from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
import os
import socket

app = Flask(__name__)

client = MongoClient('mongodb', 27017)
db = client.tododb

@app.route("/")
def hello():
    html = "<h3>Hello, world</h3>" \
           "<b>Use docker composer for flask and Mongo<br/>" \
           "<b>Hostname:</b> {hostname}<br/>" 
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)