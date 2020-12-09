# standard library

# third-party libraries
from bottle import run, route

# local packages


@route("/graphql")
def graphQL():
    return "response"


run(host="localhost", port=5000, debug=True)
