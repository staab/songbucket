import sqlite3, threading


pool = {}

def get_connection():
    thread_ident = threading.get_ident()

    if thread_ident not in pool:
        pool[thread_ident] = sqlite3.connect("songbucket.db")

    return pool[thread_ident]


class ValidationError(Exception):
    pass


def list_favorites():
    cursor = get_connection().cursor()
    cursor.execute("select * from favorites")
    columns = [x[0] for x in cursor.description]

    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def add_favorite(data):
    if not data.get("artist"):
        raise ValidationError("'artist' is a required parameter")

    if not data.get("song"):
        raise ValidationError("'song' is a required parameter")

    values = (data["artist"], data["song"])

    cursor = get_connection().cursor()

    try:
        cursor.execute("insert into favorites VALUES (null, ?, ?)", values)
        get_connection().commit()
    except sqlite3.IntegrityError:
        pass

    cursor.execute("select id from favorites where artist = ? and song = ?", values)

    return cursor.fetchone()[0]


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
