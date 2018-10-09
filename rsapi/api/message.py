import tornado.web
import tornado.websocket
import tornado.escape
import helper
import re
import json

class Handler(tornado.web.RequestHandler):
    async def get(self):
        try:
            name = self.get_argument("name")
            message = self.get_argument("msg")
        except:
            return self.send_error(400)

        websocket = await tornado.websocket.websocket_connect("ws://localhost/ws")
        await websocket.write_message("msg {} {}".format(name, message))
        msg = await websocket.read_message()
        websocket.close()
        self.write(helper.success({"response":msg}))

    def write_error(self, status_code, **kwargs):
        self.finish(helper.error(status_code, self._reason))
