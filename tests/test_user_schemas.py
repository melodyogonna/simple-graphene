# standard libraries
import unittest

# third-party dependencies
from graphene.test import Client

# local packages
from simple_graphql.schema import schema


class ExecuteQueriesOnSimpleSchemea(unittest.TestCase):
    def test_querying(self):
        client = Client(schema)
        excuted = client.execute("{ users { name } }")

        expected_response = {"data": {"users": {"name": "melody"}}}

        self.assertEqual(excuted, expected_response)


if __name__ == "__main__":
    unittest.main()
