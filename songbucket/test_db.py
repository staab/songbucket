import unittest, subprocess
from songbucket import db


class TestDb(unittest.TestCase):
    def setUp(self):
        # Reset the database
        subprocess.run(["python3", "populate_db.py"])

    def testListFavorites(self):
        self.assertEqual(
            [
                {"artist": "Rebecca Black", "id": 1, "song": "Friday"},
                {"artist": "Sufjan Stevens", "id": 2, "song": "Friday"},
                {"artist": "Elvis", "id": 3, "song": "Blue Suede Shoes"},
                {
                    "artist": "Simon and Garfunkel",
                    "id": 4,
                    "song": "Feeling Groovy",
                }
            ],
            db.list_favorites(),
        )

    def testAddFavorite(self):
        db.add_favorite({"artist": "Seal", "song": "Crazy"})

        self.assertEqual(
            [
                {"artist": "Rebecca Black", "id": 1, "song": "Friday"},
                {"artist": "Sufjan Stevens", "id": 2, "song": "Friday"},
                {"artist": "Elvis", "id": 3, "song": "Blue Suede Shoes"},
                {
                    "artist": "Simon and Garfunkel",
                    "id": 4,
                    "song": "Feeling Groovy",
                },
                {"artist": "Seal", "id": 5, "song": "Crazy"}
            ],
            db.list_favorites(),
        )
