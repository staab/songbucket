import sqlite3

if __name__ == '__main__':
    db = sqlite3.connect('songbucket.db')

    db.execute("""
    DROP TABLE IF EXISTS favorites
    """)

    db.execute("""
    CREATE TABLE favorites (
        id integer not null primary key,
        artist text not null,
        song test not null,
        UNIQUE(artist, song)
    )
    """)

    db.execute("""
    INSERT INTO favorites (artist, song)
    VALUES
        ('Rebecca Black', 'Friday'),
        ('Sufjan Stevens', 'Friday'),
        ('Elvis', 'Blue Suede Shoes'),
        ('Simon and Garfunkel', 'Feeling Groovy')
    """)

    db.commit()
