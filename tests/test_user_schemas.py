# standard libraries
import unittest

# third-party dependencies
from snapshottest import TestCase
from graphene.test import Client

# local packages
from simple_graphql.main import schema


class ExecuteQueriesOnSimpleSchemea(TestCase):
    def test_querying(self):
        client = Client(schema)
        excuted = client.execute("{ users { name } }")

        self.assertMatchSnapshot(excuted)


if __name__ == "__main__":
    unittest.main()
