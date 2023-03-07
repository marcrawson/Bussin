from http.server import BaseHTTPRequestHandler, HTTPServer
from perceptron import *


class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Send a response back to the client with an index.html file as the response body
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('public/index.html', 'rb') as file:
                response = file.read()
                self.wfile.write(response)
        elif self.path == '/style.css':
            # Serve a stylesheet file
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            with open('public/style.css', 'rb') as file:
                response = file.read()
                self.wfile.write(response)

        elif self.path == '/script.js':
            # Serve a stylesheet file
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            with open('public/script.js', 'rb') as file:
                response = file.read()
                self.wfile.write(response)
        
        elif self.path.startswith('/AI'):
            obj = {}
            if ('?' not in self.path):
                self.send_error(400)
                return

            url_request = self.path.split('?')[1]
            for x in url_request.split('&'):
                key_val = x.split('=')
                obj[key_val[0]] = key_val[1]
            print(obj)
            # Serve a stylesheet file
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            response = 'Bus #26 will likely be late to stop id 100919 on ' + obj['date'] + '.'
            self.wfile.write(response.encode())

        else:
            # Send a 404 error response for any other URL path
            self.send_error(404)

def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()