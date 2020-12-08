from app.models import Comment,User,Pitch
from app import db
import unittest

class CommnentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_Barbez = User(username = 'Barbez',password = '12345',email = 'b@gmail.com')
        self.new_pitch = Pitch(id=1,pitch_title='Test',pitch_comment='This is a test pitch',category="interview",user = self.Barbez,likes = 0,dislikes=0)
        self.new_comment = Comment(id=1,comment = 'Test comment',user = self.user_Barbez, pitch = self.new_pitch)
        
    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        
    def test_check_instance_variable(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_Barbez)
        self.assertEquals9self.new_comment.pitch,self.new_pitch)