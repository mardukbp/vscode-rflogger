import requests

ROBOT_LISTENER_API_VERSION = 2
LISTENER_SERVER = "http://localhost:5696/"
INDENT = 4*" "
depth = 0

def keyword_was_run(attributes):
    type = attributes['type']
    status = attributes['status']

    return type == 'KEYWORD' and not status == 'NOT RUN'


def start_suite(name, attributes):
    send('clear', None)


def start_keyword(name, attributes):
    global depth

    if keyword_was_run(attributes):
        send('log', f"Keyword: {name}")
        depth += 1


def end_keyword(name, attributes):
    global depth

    if keyword_was_run(attributes):
        depth -= 1


def log_message(message):   
    send('log', f"{message['level']} : {message['message']}")


def send(endpoint, body):
    data = (depth*INDENT + body).encode('utf-8') if body else body
    requests.post(LISTENER_SERVER + endpoint, data)
