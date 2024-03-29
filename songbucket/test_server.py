import unittest, os, time, random, subprocess, json
from http.client import HTTPConnection
from songbucket import db

env = os.environ.copy()
env["PORT"] = str(random.randint(10000, 65535))

# Start the server
process = subprocess.Popen(["python3", "."], env=env)

# Wait for the server to start
time.sleep(0.3)


class TestServer(unittest.TestCase):
    def setUp(self):
        db.reset()

        self.client = HTTPConnection("localhost", env["PORT"])

    def tearDown(self):
        self.client.close()

    def request(self, *args, **kwargs):
        self.client.request(*args, **kwargs)

        response = self.client.getresponse()

        return response.status, json.loads(response.read())

    def testStatic(self):
        self.client.request("GET", "/")

        response = self.client.getresponse()

        self.assertEqual(200, response.status)
        self.assertTrue(b'this comment helps us' in response.read())

        self.client.request("GET", "/index.html")

        response = self.client.getresponse()

        self.assertEqual(200, response.status)
        self.assertTrue(b'this comment helps us' in response.read())

    def testListFavorites(self):
        status, body = self.request("GET", "/favorites")

        self.assertEqual(200, status),
        self.assertEqual({"favorites": db.fixtures}, body)

    def testAddFavorite(self):
        request_body = json.dumps({"artist": "Seal", "song": "Crazy"}).encode("utf-8")
        status, body = self.request("POST", "/favorites", body=request_body)

        self.assertEqual(201, status),

        status, body = self.request("GET", "/favorites")

        self.assertEqual(200, status),
        self.assertEqual(
            {"favorites": db.fixtures + [{"artist": "Seal", "id": 5, "song": "Crazy"}]},
            body,
        )

    def test404(self):
        status, body = self.request("GET", "/no-such-route")

        self.assertEqual(404, status),
        self.assertEqual({"error": "Not found"}, body)

    def testInvalidJson(self):
        status, body = self.request("POST", "/favorites", body=b"bogus json")

        self.assertEqual(400, status),
        self.assertEqual({"error": "Invalid JSON in request body"}, body)

    def testInvalidArtist(self):
        status, body = self.request("POST", "/favorites", body=b'{"song": "Something"}')

        self.assertEqual(400, status),
        self.assertEqual({"error": "'artist' is a required parameter"}, body)

    def testInvalidSong(self):
        status, body = self.request(
            "POST", "/favorites", body=b'{"artist": "Something"}'
        )

        self.assertEqual(400, status),
        self.assertEqual({"error": "'song' is a required parameter"}, body)
