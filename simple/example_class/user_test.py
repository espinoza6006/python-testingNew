import unittest
from user import User

class UsertTest(unittest.TestCase):
    def test_user_talks(self):
        juan_object = User("Juan","j@j.com",23,"london street")
        ana_object = User("Ana","a@a.com",56,"other street")
        # print(juan_object)
        # print(juan_object.name)
        # print(juan_object.address)
        self.assertIsNotNone(juan_object)
        message = juan_object.talk()
        # print(message)
        self.assertIsNotNone(message)
        self.assertTrue(message.index('Juan')>=0)
        message_from_ana=ana_object.talk()
        # print(message_from_ana)
        self.assertTrue(message_from_ana.index('Ana')>=0)

    def test_user_says_its_address(self):
        pedro_object = User("Pedro","p@j.com",15,"london street 43")
        theadddress = pedro_object.saysAddress()
        # print(theadddress)
        self.assertTrue(theadddress.index("london")>=0)
        self.assertTrue(theadddress.index("Good morning")>=0)
        self.assertTrue(theadddress.index("43")>=0)

    def test_update_age(self):
        pedro_object = User("Pedro","p@j.com",15,"london street 43")
        pedro_object.updateAge(45)
        self.assertEqual(pedro_object.age,45)
        pedro_object.updateAge(-5)
        self.assertEqual(pedro_object.age,45)

    def test_send_email(self):
        # TDD
        self.assertTrue(True)
        self.assertTrue(True)
        self.assertTrue(True)
        self.assertTrue(True)
        self.assertTrue(True)
        self.assertTrue(True)

    # this comment is a test 
    # Hi Duygu this is a comment to test a pull request and to be worh as a team in a future.!! I hope you are learning    

if __name__ == '__main__':
    unittest.main()
