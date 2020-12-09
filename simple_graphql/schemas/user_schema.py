from graphene import ObjectType, String, Int


class UserSchema(ObjectType):
    """Schema for user information"""

    name = String()
    email = String()

