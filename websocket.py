import json
from config import Constants
import tornado.websocket

class Handler(tornado.websocket.WebSocketHandler):
    # Note that self.comapp cannot be used since '=' in Python is only binding
    # not setting. Therefore binding a value in one instance doesn't transfer
    # to the next.
    clients = set()
    comapp = None

    def open(self):
        print("connection")
        if self.get_argument("auth", None) == Constants.WEBSOCKET_SECRET:
            Handler.comapp = self
        else:
            self.clients.add(self)

    def on_message(self, message):
        if self == Handler.comapp:
            uid, msg = json.loads(message)
            client = next((client for client in self.clients if id(client) == uid), None)
            if client:
                client.write_message(msg)
        else:
            if Handler.comapp:
                Handler.comapp.write_message(json.dumps([id(self), message]))
            else:
                self.write_message("COMAPP not available")

    def on_close(self):
        print("closed")
        if self == Handler.comapp:
            Handler.comapp = None
        else:
            self.clients.remove(self)

    def check_origin(self, origin):
        return True
