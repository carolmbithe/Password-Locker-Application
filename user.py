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
