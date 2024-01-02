from flask import render_template, request, redirect, url_for
from models import User, TodoItem
import random
from base import app, db

@app.route('/')
def index():
    users = User.query.all()
    tasks = TodoItem.query.all()
    return render_template('index.html', users=users, tasks=tasks)

@app.route('/add-user', methods=['POST'])
def add_user():
    name = request.form.get('name')
    user = User(name=name, email=f"{name.lower()}@mail.com")
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/add-task', methods=['POST'])
def add_task():
    description = request.form.get('description')
    task = TodoItem(description=description)
    db.session.add(task)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/add-user/<string:name>')
def seed_user(name):
    try:
        user = User(name=name, email=f"{name.lower()}@mail.com")
        db.session.add(user)
        db.session.commit()
        return f"User {name} added successfully."
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
@app.route('/add-task/<string:description>')
def seed_task(description):
    try:
        task = TodoItem(description=description)
        db.session.add(task)
        db.session.commit()
        return f"Task {description} added successfully."
    except Exception as e:
        return f"An error occurred: {str(e)}"



    
    


if __name__ == '__main__': 
   app.run(host="0.0.0.0", port=5125, debug=True)


