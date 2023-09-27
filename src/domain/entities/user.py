
class User:
    name: str
    email: str
    verified: bool

def loadUser(user: User, **data: dict) -> User:
    user.name = data['name']
    user.email = data['email']
    user.verified = data.get('verified', False)
    return user

def dumpUser(user: User) -> dict:
    return {
        'name': user.name,
        'email': user.email
    }