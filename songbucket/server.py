import json
from http.client import HTTPConnection
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

    # Request handlers (aka controllers)

    def list_favorites(self):
        self.send_json(200, {"favorites": db.list_favorites()})

    def add_favorite(self):
        try:
            self.send_json(201, {"id": db.add_favorite(self.read_json())})
        except json.decoder.JSONDecodeError:
            self.send_json(400, {"error": "Invalid JSON in request body"})
        except db.ValidationError as exc:
            self.send_json(400, {"error": exc.args[0]})

    # Method handlers and route matching

    def do_GET(self):
        if self.path == "/favorites":
            return self.list_favorites()

        client = HTTPConnection("localhost", 3000)
        client.request('GET', self.path)

        response = client.getresponse()

        self.send_response(response.status)

        for key, value in response.getheaders():
            self.send_header(key, value)

        self.end_headers()
        self.wfile.write(response.read())

    def do_POST(self):
        print(self.path)
        if self.path == "/favorites":
            return self.add_favorite()

        return self.send_json(404, {"error": "Not found"})
