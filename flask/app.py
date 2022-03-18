from flask import Flask
from datetime import date
import socket
import requests
import os


def exchange_rate():
    '''Exchange rate data for KZT'''
    url = 'https://api.exchangerate-api.com/v4/latest/KZT'
    response = requests.get(url)
    data = response.json()['rates']
    exchange_table = ""
    for (k, v) in data.items():
        exchange_table += "<tr><td>{}</td><td>{}</td></tr>".format(k,v)

    return "<table>" + exchange_table + "</table>"


app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello, World!</h1><p>Container's ID: {}</p><p>Today's date: {}</p><p>Exchange rate data for KZT:</p>{}".format(socket.gethostname(), date.today(), exchange_rate())

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
