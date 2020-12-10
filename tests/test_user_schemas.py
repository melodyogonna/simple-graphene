# standard libraries
import unittest

# third-party dependencies

# local packages
from simple_graphql.schema import schema


class ExecuteQueriesOnSimpleSchemea(unittest.TestCase):
    def test_querying(self):

        excuted = schema.excute("{ users { name } }")
        print(excuted)

        expected_response = {"data": {"users": []}}

        self.assertEqual(excuted, expected_response)


if __name__ == "__main__":
    unittest.main()
