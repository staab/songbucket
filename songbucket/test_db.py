import unittest, subprocess
from songbucket import db


class TestDb(unittest.TestCase):
    def setUp(self):
        db.reset()

    def testListFavorites(self):
        self.assertEqual(db.fixtures, db.list_favorites())

    def testAddFavorite(self):
        db.add_favorite({"artist": "Seal", "song": "Crazy"})

        self.assertEqual(
            db.fixtures + [{"artist": "Seal", "id": 5, "song": "Crazy"}],
            db.list_favorites(),
        )
