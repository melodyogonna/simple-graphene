import unittest

from snapshottest import TestCase
from graphene.test import Client

from simple_graphql.main import schema


class AddUserMutation(TestCase):
    def test_mutation_works(self):
        query_string = """
                mutation {
                    createUser(name:"melody") {
                        user {
                            name
                        }

                        ok
                    }
                }
            """

        s = Client(schema)
        result = s.execute(query_string)

        self.assertMatchSnapshot(result)


if __name__ == "__main__":
    unittest.main()
