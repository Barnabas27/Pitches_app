import unittest
from app.models import user
# User = user.User

 class UserTest(unittest.Testcase):
     
     
     def setUp(self):
         self.new_user = User(password = '12345')
         
     def test_password_setter(self):
             self.assertTrue(self.new_user.password_secure is not None)
             
     def test_no_access_password(self):
         with self.assertTaises(AttributeError):
             self.new_user.password
     def test_password_verification(self):
         self.assertTrue(self.new_user.verify_password('12345'))
             
