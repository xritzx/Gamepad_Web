import cherrypy
from Pages.page_routes import Pages
from pynput.keyboard import Key, Controller

pad = Controller()

class Main():
    @cherrypy.expose
    def index(self):
        return Pages().homepage
    @cherrypy.expose
    def up(self):
        pad.press(Key.up)
        self.last = 'up'
        return "OK"
    @cherrypy.expose
    def down(self):
        pad.press(Key.down)
        self.last = 'down'
        return "OK"
    @cherrypy.expose
    def left(self):
        pad.press(Key.left)
        self.last = 'left'
        return "OK"
    @cherrypy.expose
    def right(self):
        pad.press(Key.right)
        self.last = 'right'
        return "OK"
    @cherrypy.expose
    def stop(self):
        pad.release(Key.up) if self.last=='up' else pad.release(Key.down) if self.last=='down' else pad.release(Key.left) if self.last=='left' else pad.release(Key.left)
        return "OKK"        

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(Main())
