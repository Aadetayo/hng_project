from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import re

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///persons.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Marshmallow inside the app context
db = SQLAlchemy(app)
ma = Marshmallow(app)

# biodata model for the info of the person
class biodata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

# Define the biodata Schema for serialization
class biodataSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'age')

biodataSchemaInit = biodataSchema()
biodataSchemaInitMany = biodataSchema(many=True)

# ---------------- Routes for CRUD operations------------------
# add Entry route 
@app.route('/api/person', methods=['POST'])
def add_entry():
    data = request.json
    name = data.get('name', '').strip()
    age = data.get('age', None)

    if not name:
        return jsonify({'message': 'Invalid name'}), 400

    if age is not None and not isinstance(age, int):
        return jsonify({'message': 'Invalid age'}), 400

    new_entry = biodata(name=name, age=age)
    db.session.add(new_entry)
    db.session.commit()
    return biodataSchemaInit.jsonify(new_entry)


# Get entry route 
@app.route('/api/person', methods=['GET'])
def get_persons():
    all_persons = biodata.query.all()
    return biodataSchemaInitMany.jsonify(all_persons)

# Get entry via ID 
@app.route('/api/person/<int:id>', methods=['GET'])
def get_entry(id):
    getperson = biodata.query.get(id)
    if not getperson:
        return jsonify({'message': 'Person not found'}), 404
    return biodataSchemaInit.jsonify(getperson)

# Get entry via name@app.route('/api/person/<name>', methods=['PUT'])
@app.route('/api/person/<string:name>', methods=['GET'])
def get_entry_by_name(name):
    getperson = biodata.query.filter_by(name=name).first()
    if not getperson:
        return jsonify({'message': 'Person not found'}), 404
    return biodataSchemaInit.jsonify(getperson)


# Update entry via name
@app.route('/api/person/<string:name>', methods=['PUT'])
def update_person_by_name(name):
    putperson = biodata.query.filter_by(name=name).first()

    if not putperson:
        return jsonify({'message': 'Person not found'}), 404

    data = request.json
    name = data.get('name', '').strip()
    age = data.get('age', None)

    if not name:
        return jsonify({'message': 'Invalid name'}), 400

    if age is not None and not isinstance(age, int):
        return jsonify({'message': 'Invalid age'}), 400

    putperson.name = name
    putperson.age = age
    db.session.commit()
    return biodataSchemaInit.jsonify(putperson)

# Update entry via ID 
@app.route('/api/person/<int:id>', methods=['PUT'])
def update_person(id):
    putperson = biodata.query.get(id)

    if not putperson:
        return jsonify({'message': 'Person not found'}), 404

    data = request.json
    name = data.get('name', '').strip()
    age = data.get('age', None)

    if not name:
        return jsonify({'message': 'Invalid name'}), 400

    if age is not None and not isinstance(age, int):
        return jsonify({'message': 'Invalid age'}), 400

    putperson.name = name
    putperson.age = age
    db.session.commit()
    return biodataSchemaInit.jsonify(putperson)

@app.route('/api/person/<int:id>', methods=['DELETE'])
def delete_person(id):
    person = biodata.query.get(id)

    if not person:
        return jsonify({'message': 'Person not found'}), 404

    db.session.delete(person)
    db.session.commit()
    return biodataSchemaInit.jsonify(person)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=9000, debug=True)
