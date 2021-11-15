import requests

class RFLogger:
    ROBOT_LISTENER_API_VERSION = 2
    LISTENER_SERVER = "http://localhost:5696/"

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self

    def _start_suite(self, name, attributes):
        self._send(None, "clear")

    def _log_message(self, message):   
        self._send(f"{message['level']} {message['message']}".encode('utf-8'), "log")
    
    def _send(self, body, endpoint):
        requests.post(self.LISTENER_SERVER + endpoint,
                      data = body
        )
