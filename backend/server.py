from http.server import BaseHTTPRequestHandler, HTTPServer
# import SocketServer
import json
import cgi
from app import run as run_app
import os


class Server(BaseHTTPRequestHandler):
    """Class to create a simple http server
    """

    def _set_headers(self):
        """Define http headers
        """
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers',
                         'Authorization, Content-Type')
        self.send_header('Access-Control-Allow-Methods',
                         'GET')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        if self.path == '/':
            self._set_headers()
            run_app()
            dir_path = os.path.dirname(os.path.realpath(__file__))
            with open(f'{dir_path}/exports/data.json', encoding='utf-8') as data_file:
                data = json.loads(data_file.read())

            with open(f'{dir_path}/exports/metrics.json', encoding='utf-8') as data_file:
                metrics = json.loads(data_file.read())

            response = {
                "data": data,
                "metrics": metrics
            }
            response = json.dumps(response)
            response = bytes(response, 'utf-8')
            self.wfile.write(response)


def run(server_class=HTTPServer, handler_class=Server, port=80):
    """Generates a simple http server

    Args:
        server_class (HTTPServer, optional): Defaults to HTTPServer.
        handler_class (Server, optional): Defaults to Server.
        port (int, optional): Defaults to 80.
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    print(f"Server listening on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
