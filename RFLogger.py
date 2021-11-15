import requests

ROBOT_LISTENER_API_VERSION = 2
LISTENER_SERVER = "http://localhost:5696/"

def start_suite(name, attributes):
    send(None, "clear")

def log_message(message):   
    send(f"{message['level']} {message['message']}".encode('utf-8'), "log")

def send(body, endpoint):
    requests.post(LISTENER_SERVER + endpoint, data = body)
