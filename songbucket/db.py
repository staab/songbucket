import sqlite3


connection = sqlite3.connect("songbucket.db")


class ValidationError(Exception):
    pass


def list_favorites():
    cursor = connection.cursor()
    cursor.execute("select * from favorites")
    columns = [x[0] for x in cursor.description]

    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def add_favorite(data):
    if not data.get("artist"):
        raise ValidationError("'artist' is a required parameter")

    if not data.get("song"):
        raise ValidationError("'song' is a required parameter")

    values = (data["artist"], data["song"])

    cursor = connection.cursor()

    try:
        cursor.execute("insert into favorites VALUES (null, ?, ?)", values)
        connection.commit()
    except sqlite3.IntegrityError:
        pass

    cursor.execute("select id from favorites where artist = ? and song = ?", values)

    return cursor.fetchone()[0]


# Admin utils

fixtures = [
    {"artist": "Rebecca Black", "id": 1, "song": "Friday"},
    {"artist": "Sufjan Stevens", "id": 2, "song": "Friday"},
    {"artist": "Elvis", "id": 3, "song": "Blue Suede Shoes"},
    {"artist": "Simon and Garfunkel", "id": 4, "song": "Feeling Groovy"},
]


def drop_schema():
    connection.execute("DROP TABLE IF EXISTS favorites")


def create_schema():
    connection.execute(
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

    connection.commit()


def reset():
    drop_schema()
    create_schema()
    insert_fixtures()
