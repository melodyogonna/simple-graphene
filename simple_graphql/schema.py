from graphene import ObjectType, String, Schema

from simple_graphql.schemas.user_schema import UserSchema


class Query(ObjectType):
    """Basic GraphQL Schema definition"""

    users = UserSchema()

    def resolve_users(self, info):
        return users


schema = Schema(query=Query)
