from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Comment,User,Pitch
from .forms import CommentForm,UpdateProfile,UpdateProfile
from flask_login import login_required, current_user
from .. import db,photos
# import markdown2

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches = Pitch.query.filter_by(user_id = user_id).all()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,pitches=pitches)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitch/new_pitch',methods = ['GET','POST'])
@login_required
def new_pitch():
    pitch = PitchForm()
    if pitch.validate_on_submit():
        title = pitch.pitch_title.data
        category = pitch.pitch_category.data
        yourPitch = pitch.pitch_comment.data
        
        new_pitch = Pitch(pitch_title = title,pitch_category = category, pitch_comment = yourPitch,user = current_user)
        
        new_pitch.save_pitch()
        return redirect (url_for('.index'))
    title = 'New Pitch'
    return render_template('new_pitch.html',title = title,pitchform = pitch)

@main.route('/category/pickup_lines', methods = ['GET','POST'])
def displaypickup_linesCategory():
    pickup_linesPitches = Pitch.get_pitches('pickup_lines')
    return render_template ('category/pickup_lines.html',pickup_linesPitches = pickup_linesPitches)

@main.route('/category/interview', methods = ['GET','POST'])
def displayinterviewCategory():
    interviewPitches = Pitch.get_pitches('interview')
    return render_template ('category/interview.html',interviewPitches = interviewPitches)

@main.route('/category/product', methods = ['GET','POST'])
def displayproductCategory():
    productPitches = Pitch.get_pitches('product')
    return render_template ('category/product.html',productPitches = productPitches)

@main.route('/category/promotion', methods = ['GET','POST'])
def displaypromotionCategory():
    promotionPitches = Pitch.get_pitches('promotion')
    return render_template ('category/promotion.html',promotionPitches = promotionPitches)

@main.route('/about')
def about():
    return render_template('about.html',title = 'About')