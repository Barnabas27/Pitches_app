from ..models import Comment,User,Pitch
from app import db
import unittest

class PitchTest(unittest.TestCase):
    
    def setUp(self):
        self.user_Bush = User(username='Barbez',password='12345',email = 'b@gmail.com')
        self.new_pitch = Pitch(id =1,pitch_title ='Test',pitch_content='this is the pitch',category='interview',user = self.user_Bush, likes = 0,dislikes =0)
    
    def tearDown(self):
        User.query.delete()
        Pitch.query.delete()
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_title,'Test')
        self.assertEquals(self.new_pitch.pitch_content,'This is a test pitch')
        self.assertEquals(self.new_pitch.category,"interview")
        self.assertEquals(self.new_pitch.user,self.user_Bush)
        
    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)
        
    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitch(1)
        self.assertTrue(got_pitch is not None)
        
    