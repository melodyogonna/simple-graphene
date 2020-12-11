# standard libraries

# third-party dependencies
import graphene

# local packages
from simple_graphql.schemas.user_schema import User
from simple_graphql.mutations.mutatate_user import CreateUser


class Query(graphene.ObjectType):
    """Basic GraphQL Schema definition"""

    users = graphene.Field(User)

    @staticmethod
    def resolve_users(root, info):
        return User(name="melody", email="meldl@jdj.lld")


class Mutate(graphene.ObjectType):
    """GraphQL Mutations"""

    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutate)
