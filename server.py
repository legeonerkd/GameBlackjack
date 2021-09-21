from flask import Flask, render_template, Blueprint
from flask_sockets import Sockets
from card import Card
import json

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def root():
    return render_template('example.html')

@app.route('/cards')
def give_cards():
    cards = [
        Card('K', 'H'), 
        Card('J', 'D'), 
        Card('A', 'D'), 
        Card('Q', 'H'), 
        Card('A', 'S'), 
        Card('A', 'C'),
    ] 
    # "{'suit': 'H', 'value': '2'}" 
    # [{}, {}, {}]
    cards = [card.__dict__ for card in cards]
    return json.dumps(cards)

#JSON JavaScript Object Notation
if __name__ == "__main__":
    app.run()
    # from gevent import pywsgi
    # from geventwebsocket.handler import WebSocketHandler
    # server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    # server.serve_forever()