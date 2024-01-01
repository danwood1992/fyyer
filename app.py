from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fyyer:fyyer@fyyer-db:5432/fyyer'

db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    person = Person.query.first()
    print(person)
    if person:
        return f"{person}"  # This will use __repr__ implicitly
    else:
        return 'No person found!'

if __name__ == '__main__': 
   app.run(host="0.0.0.0", port=5125, debug=True)
