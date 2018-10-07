import tornado.web
import tornado.websocket
import tornado.escape
import helper
import re
import json

class Handler(tornado.web.RequestHandler):
    async def post(self):
        try:
            data = tornado.escape.json_decode(self.request.body)
            assert isinstance(data, list)
            assert len(data) <= 200
            assert all(isinstance(name, str) for name in data)
            assert all(not re.match(r"[^a-z0-9_ ]", name, re.IGNORECASE) for name in data)
            # Check 12 str length
        except:
            return self.send_error(400)

        websocket = await tornado.websocket.websocket_connect("ws://localhost/ws")
        await websocket.write_message(json.dumps(data))
        msg = await websocket.read_message()
        websocket.close()
        self.write(helper.success({"users":msg}))

    def write_error(self, status_code, **kwargs):
        self.finish(helper.error(status_code, self._reason))
