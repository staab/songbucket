import sqlite3


connection = sqlite3.connect("songbucket.db")


class ValidationError(Exception):
    pass


def get_favorites():
    cursor = connection.cursor()
    cursor.execute("select * from favorites")
    columns = [x[0] for x in cursor.description]

    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def save_favorite(data):
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
