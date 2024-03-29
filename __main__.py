import os
from http.server import ThreadingHTTPServer
from songbucket.server import HTTPRequestHandler


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    server = ThreadingHTTPServer(("localhost", port), HTTPRequestHandler)

    print("Server started at http://localhost:{}".format(port))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("Server stopped.")
