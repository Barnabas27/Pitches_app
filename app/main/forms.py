from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,ValidationError,PasswordField,ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import User


class PitchForm(FlaskForm):
     pitch_title = StringField('Pitch title',validators=[Required()])
     pitch_category = SelectField('Pitch Category',choices= [('Select category','Select category'),('pickup_lines','pickup_lines'),('interview_pitch','interview_pitch'),('product_pitch','product_pitch'),('promotion_pitch','promotion_pitch')],validators=[Required()])
     pitch_comment = TextAreaField('Your pitch:')
     submit = SubmitField('Submit')
    


    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:',validators = [Required()])
    submit = SubmitField('Submit')