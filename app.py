"""from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {"id": 1, "name": "Omar", "email": "omarin@hotmail.com"},
    {"id": 2, "name": "Iris", "email": "iris@hotmail.com"},
    {"id": 3, "name": "Dylan", "email": "dylan@hotmail.com"},
]


@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)


@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    new_item['id'] = data[-1]['id'] + 1 if data else 1
    data.append(new_item)
    return jsonify(new_item), 201


@app.route('/item/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in data if item['id']== item_id),None)
    if item:
        updates = request.get_json()
        item.update(updates)
        return jsonify(item)
    return ('No encontrado', 404)


@app.route('/item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    data = [item for item in data if item['id'] != item_id]
    return ('respuesta', 204)

if __name__ == '__main__':
    app.run(debug=True)
    
"""

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mi_base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}
    
with app.app_context():
    db.create_all()
  
  
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])


@app.route('/items', methods=['POST'])
def create_item():
    new_item_data = request.get_json()
    new_item = Item(name=new_item_data['name'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201


@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    updated_data = request.get_json()
    item.name = updated_data['name']
    db.session.commit()
    return jsonify(item.to_dict()), 200


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
     item = Item.query.get_or_404(item_id)
     db.session.delete(item)
     db.session.commit()
     return ('', 204)

if __name__ == '__main__':
    app.run(debug=False)
    
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    calculo = celsius * 9/5 + 32
    return calculo

def fahrenheit_to_celsius(fahrenheit):
    calculo = (fahrenheit -32 )* 5/9
    
@app.route('/convert', methods = ['POST'])
def convert_temp():
    data = request.get_json()
    input_temp=data.get('temperature')
    
    if data['type'] == 'celsius':
        result = celsius_to_fahrenheit(input_temp)
        output_unit = 'fahrenheit'
    
    if data['type'] == 'fahrenheit':
        result = fahrenheit_to_celsius(input_temp)
        output_unit = 'celsius'
        
    return jsonify({"temperature": result, "unit": output_unit})


if __name__ == '__main__':
    app.run(debug=True)
    
"""