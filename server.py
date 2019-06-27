import os, json
from http.server import HTTPServer, BaseHTTPRequestHandler



def get_favorites():
    return []


def save_favorite(data):
    return 1


def to_json(x):
    return json.dumps(x).encode('utf-8')


def from_json(x):
    return json.loads(x.decode('utf-8'))


class MyServer(BaseHTTPRequestHandler):
    err_not_found = 'Not found'

    def list_favorites(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(to_json({'favorites': get_favorites()}))

    def add_favorite(self):
        try:
            id = save_favorite(from_json(self.rfile.read1()))
        except ValidationError:
            self.send_error(400)

            return

        self.send_response(201)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(to_json({'id': id}))

    def do_GET(self):
        if self.path == '/favorites':
            return self.list_favorites()

        return self.send_error(404)

    def do_POST(self):
        if self.path == '/favorites':
            return self.add_favorite()

        return self.send_error(404)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    server = HTTPServer(('localhost', port), MyServer)

    print("Server started at http://localhost:{}".format(port))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("Server stopped.")
