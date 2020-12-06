# standard library

# third-party libraries
from bottle import run, route
import graphene


@route("/graphql")
def graphQL():
    return "response"


run(host="localhost", port=5000)
