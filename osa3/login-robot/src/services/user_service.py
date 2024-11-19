from entities.user import User
import re

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
        if not self.is_valid_username(username):
            # print("Invalid username")
            raise UserInputError("Invalid username")
        if not self.is_valid_password(password):
            # print("Invalid password")
            raise UserInputError("Invalid password")

    # Function to check if the username 
    def is_valid_username(self, username):
        # Regex for a valid username (3 or more letters)
        username_regex = r'[a-zA-Z]{3,}$'
        return re.match(username_regex, username)
    
    # Function to check if the password is valid
    def is_valid_password(self, password):
        # Regex for a valid password (8 or more characters, not just letters)
        password_regex = r'(?=.*[a-zA-Z])(?=.*\d).{8,}$'
        return re.match(password_regex, password)
