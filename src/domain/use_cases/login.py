from src.entities.user import User, loadUser

def loginUser(user: User, data: dict, existUser, registerUser) -> User:
    user = loadUser(user, data)
    if not (user.verified or existUser(user)): registerUser(user)