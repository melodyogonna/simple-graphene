from graphene import ObjectType, String, Int


class User(ObjectType):
    """Schema for user information"""

    name = String()
    email = String()
