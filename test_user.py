import unittest
from user import User,Credential


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Caroline","1234")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case runs
        """
        User.user_names=[]

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Caroline")
        self.assertEqual(self.new_user.password,"1234")

    def test_save_user(self):
        """
        test case to see if the user name is saved into the user usernames
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_names),1)

    def test_save_multiple_users(self):
        """
        test_save_multiple_users to check if we can save multiple usernames to our user_names
        """
        self.new_user.save_user()
        test_user = User("Mary","1234")
        test_user.save_user()
        self.assertEqual(len(User.user_names),2)

    def test_user_exists(self):
        """
        test to check if we can return a Boolean if we cannot find the users
        """
        self.new_user.save_user()
        test_user=User("Mary","1234")
        test_user.save_user()

        user_exists = User.user_exist("Mary")
        self.assertTrue(user_exists)

class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behavioursself.
    Args:
        unittest.TestCase:TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test casesself.
        """
        self.new_credential = Credential("Twitter","carombithe","4321")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has runself.
        """

        Credential.credential_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.account_type,"Twitter")
        self.assertEqual(self.new_credential.user_name,"carombithe")
        self.assertEqual(self.new_credential.password,"4321")


    def test_save_credential(self):
        """
        test save credential test case to test if the contact object is saved into the credential_list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_credentials(self):
        """
        test_save_multiple_credentials to check if it can save multiple credentials objects to our credential_list
        """
        self.new_credential.save_credential()
        test_credential=Credential("Facebook","mumocarol","09876")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)



if __name__ == '__main__':
    unittest.main()
