import unittest
from user import User

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



if __name__ == '__main__':
    unittest.main()
