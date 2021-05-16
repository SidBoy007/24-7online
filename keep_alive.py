from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Your ID is now Active 24/7! Coded By SIDBOY !!!!!!!!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
