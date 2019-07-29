
def get_connection():
    pass


def list_favorites():
    pass


def add_favorite(data):
    pass


# Admin utils

fixtures = [
    {"artist": "Rebecca Black", "id": 1, "song": "Friday"},
    {"artist": "Sufjan Stevens", "id": 2, "song": "Casimir Pulaski Day"},
    {"artist": "Elvis", "id": 3, "song": "Blue Suede Shoes"},
    {"artist": "Simon & Garfunkel", "id": 4, "song": "The 59th Street Bridge Song"},
]


def drop_schema():
    get_connection().execute("DROP TABLE IF EXISTS favorites")


def create_schema():
    get_connection().execute(
        """
        CREATE TABLE favorites (
            id integer not null primary key,
            artist text not null,
            song test not null,
            UNIQUE(artist, song)
        )
        """
    )


def insert_fixtures():
    for favorite in fixtures:
        add_favorite(favorite)

    get_connection().commit()


def reset():
    drop_schema()
    create_schema()
    insert_fixtures()
