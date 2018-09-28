class User:
    """
    A class that generates new instances for users
    """
    def __init__(self,user_name,password):
        """
        a method to define properties of our object
        Args:
            user_name: New user username.
            password : New user password.
        """
        self.user_name=user_name
        self.password=password
    user_names = []

    def save_user(self):
        """
        save_user method saves user objects into the user_names
        """
        User.user_names.append(self)

    @classmethod
    def user_exist(cls,user_name):
        """
        Method that checks if a user exists from the user_names
        """
        for user in cls.user_names:
            if user.user_name == user_name:
                return True

        return False

class Credential:
    """
    Class that generates new instances of Credential
    """
    def __init__(self,account_type,user_name,password):
        """
        __init__ method that helps us define properties of our objects
             Args:
        account_type:The type of account_type
        user_name:The username for that account .
        password:password for that account.

        self variable represents the instance of the object
        """
        self.account_type = account_type
        self.user_name = user_name
        self.password = password

    credential_list = []

    def save_credential(self):
        """
        save_credential method saves credential objects into the credential_list
        """
        Credential.credential_list.append(self)
