from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
#from app.models import Student


class NewStudent(FlaskForm):
	student_name = StringField('Student Name', validators=[DataRequired()])
	parent_name = StringField('Parent Name', validators=[DataRequired()])
	#TODO formatting
	email = StringField('Email', validators=[DataRequired(), Email()])
	phone = StringField('Phone Number', validators=[DataRequired()])
	address = StringField('Address')
	submit = SubmitField('Submit')

	#TODO validation
	'''def validate_username(self, username):
		student = Student.query.filter_by(student_name=student_name.data).first()
		if student is not None:
			raise ValidationError('Username taken! Please use a different username.')'''

	'''def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Email already taken! Please use a different email address.')'''