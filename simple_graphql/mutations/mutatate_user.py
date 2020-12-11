import graphene

from simple_graphql.schemas.user_schema import User


class CreateUser(graphene.Mutation):
    """Create User"""

    class Arguments:
        name = graphene.String()

    user = graphene.Field(User)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, name):
        user = User(name=name)
        ok = True
        return CreateUser(user=user, ok=ok)
