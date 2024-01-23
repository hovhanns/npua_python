from flask import Flask, request, jsonify

app = Flask(__name__)

# Create operation

"""
curl -X POST http://127.0.0.1:5000/create -d {} -H 'Content-Type: application/json'
"""

@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    print(data)
    # Perform create operation here
    return jsonify({'message': 'Record created successfully'})

# Read operation
@app.route('/read', methods=['GET'])
def read():
    # Perform read operation here
    print(request.headers)
    return jsonify({'message': 'Records retrieved successfully'})

# Update operation
@app.route('/update', methods=['PUT'])
def update():
    data = request.get_json()
    # Perform update operation here
    return jsonify({'message': 'Record updated successfully'})

# Delete operation
@app.route('/delete', methods=['DELETE'])
def delete():
    data = request.get_json()
    # Perform delete operation here
    return jsonify({'message': 'Record deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
