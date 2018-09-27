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
