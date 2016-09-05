from flask.ext.wtf import Form
from wtforms import (StringField,TextAreaField,BooleanField,TextAreaField,
	SubmitField,SelectField)
from wtforms.validators import Length,Required,Email,Regexp
from ..models import Role,User
from wtforms import ValidationError
from flask.ext.pagedown.fields import PageDownField

class EditProfileForm(Form):
	name = StringField('Real name',validators=[Length(0,64)])
	location = StringField('Location',validators=[Length(0,64)])
	about_me = TextAreaField('About me')
	submit = SubmitField('Submit')


class EditProfileAdminForm(Form):
	email = StringField('Email',validators=[Required(),Length(1,64),Email()])
	username = StringField('Username',validators=[Required(),Length(1.64),
		Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'Usernames must hava only letters,'
			'numbers,dots or underscores')])
	confirmed = BooleanField('Confirmed')
	role = SelectField('Role',coerce=int)
	name = StringField('Real name',validators=[Length(0,64)])
	location = StringField('Location',validators=[Length(0.64)])
	about_me = TextAreaField('About me')
	submit = SubmitField('Submit')
	#init role and add  user 
	def __init__(self,user,*args,**kwargs):
		super(EditProfileAdminForm,self).__init__(*args,**kwargs)
		self.role.choices = [(role.id,role.name)
							for role in Role.query.order_by(Role.name).all()]
		self.user8 = user

	#check the email is changed?  and whether the emai and user name already exitst
	def validata_email(self,field):
		if field.data != self.user.email and User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')
	def validate_username(self,field):
		if field.data != self.user.username and User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already in use.')



class PostForm(Form):

	#body = TextAreaField('What\'s on your mind?',validators=[Required()])
	body = PageDownField("What's on your mind?",validators=[Required()])
	submit = SubmitField('Submit')



