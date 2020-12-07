import unittest
from models import user
User = user.User

 class UserTest(unittest.Testcase):
     
     def setUp(self):
         self.new_user = User(1,'Barbez','barbez@gmail.com','I am he','profile_pic path','12345')
         
         def test_instance(self):
             self.assertTrue(isinstance(self.new_user,User))
             
if __name__ == '__main__':
    unittest.main()