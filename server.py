"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
# from Tkinter import Text, END

class S(BaseHTTPRequestHandler):

    filepath = "/Users/hakonhukkelas/programmering/ntnu/test.json"
    # to_print_to = Text()
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        f = open(self.filepath)
        self._set_headers()
        self.wfile.write("<html><body>%s</body></html>" % "".join(f.readlines()))
        f.close()
        # S.to_print_to.insert(END,"GET from: %s \n" % self.client_address[0])

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
    # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        f = open(self.filepath,'w')
        f.write(post_data)
        f.close()
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")


class Server:

    def start(self, server_class=HTTPServer, handler_class=S, port=80):
        port = 8888
        server_address = ('', port)
        self.httpd = server_class(server_address, handler_class)
        self.httpd.serve_forever()
        print 'Starting httpd...'
    
    def stop(self):
        self.httpd.server_close()

if __name__ == "__main__":
  s = Server()
  s.start()


