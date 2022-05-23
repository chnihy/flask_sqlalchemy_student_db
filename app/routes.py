from app import app, db
from flask import Flask, render_template, url_for, flash, redirect, request
from app.models import Student
from app.forms import NewStudent

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Student': Student}

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/newstudent', methods=['GET', 'POST'])
def newstudent():
    form = NewStudent()
    if form.validate_on_submit():
        student = Student(student_name = form.student_name.data, 
						parent_name = form.parent_name.data,
						email = form.email.data,
						phone = form.phone.data,
						address = form.address.data)
        db.session.add(student)
        db.session.commit()
        flash('New Student: {} Added'.format(form.student_name.data))
        return redirect(url_for('students'))
    return render_template('newstudent.html', title='New Student', form=form)

@app.route('/students')
def students():
	students_query = Student.query
	return render_template('students.html', title="Students", students=students_query)

@app.route('/student')
def student():
    query = request.args['search']
    print(query)
    student_search = Student.query.filter_by(student_name=query)
    if student_search:
        return render_template('student.html', title="Student", student_search=student_search)
    else:
        return render_template('index.html')

@app.route('/delete', methods=["POST"])
def delete():
    """Remove student from db
    
    Keyword arguments:
    id  -- student.student_id
    Return: url_for('students')
    """
    # id = form.id.data
    student = Student.query.filter_by(id=request.form['id']).first()
    
    db.session.delete(student)
    db.session.commit()
    
    flash('Student: {} Deleted'.format(request.form['student_name']))
    
    return redirect(url_for('students'))