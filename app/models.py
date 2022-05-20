from app import app, db

class Student(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)
	student_name = db.Column(db.String(20))
	parent_name = db.Column(db.String(20), index=True)
	email = db.Column(db.String(120), index=True)
	# TODO formatting
	phone = db.Column(db.String(120), index=True)
	address = db.Column(db.String(120), index=True)

	def __repr__(self):
		return '<User {}>'.format(self.username)