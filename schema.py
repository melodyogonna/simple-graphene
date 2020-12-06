from graphene import ObjectType, String, Schema


class Query(ObjectType):
    """Basic GraphQL Schema definition"""

    def resolve_name(self, name):
        return name


schema = Schema(query=Query)
