from flask import render_template, request, redirect, url_for
from models import User, TodoItem
import random
from base import app, db

@app.route('/')
def index():
    users = User.query.all()
    tasks = TodoItem.query.all()
    return render_template('index.html', users=users, tasks=tasks)

@app.route('/seed/<string:name>')
def seed_data(name):
    try:
        user = User(name=name, email=f"{name.lower()}@mail.com")
        db.session.add(user)
        db.session.commit()
        return f"User {name} added successfully."
    except Exception as e:
        return f"An error occurred: {str(e)}"



    
    


if __name__ == '__main__': 
   app.run(host="0.0.0.0", port=5125, debug=True)


