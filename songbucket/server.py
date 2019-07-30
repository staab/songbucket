import json
from http.server import BaseHTTPRequestHandler
from songbucket import db


class HTTPRequestHandler(BaseHTTPRequestHandler):

    # Utility functions

    def read_json(self):
        return json.loads(self.rfile.read1().decode("utf-8"))

    def send_json(self, status_code, body):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(body).encode("utf-8"))

    def serve_static_file(self):
        pass

    # Request handlers (aka controllers)

    def list_favorites(self):
        pass

    def add_favorite(self):
        pass

    # Method handlers and route matching

    def do_GET(self):
        if self.path == "/favorites":
            pass

        try:
            return self.serve_static_file()
        except FileNotFoundError as exc:
            pass

        raise Exception("Not found")

    def do_POST(self):
        if self.path == "/favorites":
            pass

        raise Exception("Not found")
