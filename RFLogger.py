import requests

ROBOT_LISTENER_API_VERSION = 2
LISTENER_SERVER = "http://localhost:5696/"

def start_suite(name, attributes):
    send('clear', None)

def start_keyword(name, attributes):
    type = attributes['type']
    status = attributes['status']

    if type == 'KEYWORD' and not status == 'NOT RUN':
        send('log', f"Keyword: {name}")

def log_message(message):   
    send('log', f"{message['level']} : {message['message']}")

def send(endpoint, body):
    requests.post(LISTENER_SERVER + endpoint, data = body.encode('utf-8') if body else body)
