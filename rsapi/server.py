import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.template
import websocket
import api.world
import bootstrap

class Handler(tornado.web.RequestHandler):
    async def get(self):
        self.write(await bootstrap.bootstrap({
            "authentication": r"login=function\([^,)]+,[^,)]+,[^,)]+,[^,)]+\)",
            "ready": r"ready=function\(\)\{return [^.&]+\.ready\(\)}",
            "user": r"isFriend=function[^{]+{r", #matches twice
            "message": r"11,[^:]+:17,"
        }))

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/ws", websocket.Handler),
        (r"/world", api.world.Handler),
        (r"/bootstrap.js", Handler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(80)
    tornado.ioloop.IOLoop.instance().start()
