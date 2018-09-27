import unittest
from credential import Credential

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
    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.account_type,"Twitter")
        self.assertEqual(self.new_credential.user_name,"carombithe")
        self.assertEqual(self.new_credential.password,"4321")

if __name__ == '__main__':
    unittest.main()          
