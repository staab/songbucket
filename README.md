# Server

The server is split into two parts: the data layer and the server layer. The data layer is implemented in `songbucket/db.py`, and defines database access methods, handling safe SQL queries and data validation by defining an interface for the rest of the app to use. The server layer is implemented in `songbucket/server.py`, and defines an HTTP handler that takes incoming requests and routes them to the right place (either api methods or static files), handling HTTP headers, body parsing, and status codes. The `__main__.py` ties this all together by creating a basic HTTP server using the handler we defined and listening on an HTTP port.

Note that this is a toy application; this shouldn't be used as a template for a production app, particularly the server. This is for security as well as performance reasons. Lots of good servers exist in the python ecosystem, most notably [Werkzeug](https://palletsprojects.com/p/werkzeug/).

## Setting up the database

The repository comes with a sqlite3 database pre-built with the app's schema. If you need to reset it, a `git checkout songbucket.db` should do the trick. If you would like to modify the schema or starting data, you can edit `populate_db.py`, and then run `python3 populate_db.py`.

## Running the server

This repository is set up as a python package, which means that you can start it with `python3 .`. If you would like to use a port other than 8080, you can do that using an _environment variable_, which is the standard way of separating configuration of your application from your code. That looks like this: `PORT=8999 python3 .`.

## Running tests

A quick test package is provided, which demonstrates how to use python's built-in `unittest` module. In this case, we make simple http requests against the server to check that it spits out the right data. Note that normally real http requests aren't used in testing since they slow things down significantly. To run the tests, execute `python3 -m unittest .`. This will automatically find all tests that are defined using unittest's `TestCase` class.
