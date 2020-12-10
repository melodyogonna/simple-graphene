import graphene

from simple_graphql.schemas.user_schema import User


class Query(graphene.ObjectType):
    """Basic GraphQL Schema definition"""

    users = graphene.Field(User)

    @staticmethod
    def resolve_users(root, info):
        return User(name="melody", email="meldl@jdj.lld")


schema = graphene.Schema(query=Query)
