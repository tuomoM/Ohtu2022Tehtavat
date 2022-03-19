from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        user = self._user_repository.find_by_username(username)
        if user!=None:
            raise UserInputError("User with username already exists")
        if len(username)<3:
            raise UserInputError("Too short username")
        if len(password)< 4:
            raise UserInputError("Too short password")
        if password.isalpha():
            raise UserInputError("Only alphabets")


        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
