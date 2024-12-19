from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
employees = [
    {'id': 1, 'name': 'Harry', 'department': 'HR'},
    {'id': 2, 'name': 'John', 'department': 'IT'},
    {'id': 3, 'name': 'Mary', 'department': 'Marketing'}
]

# Get all Employee Data
@app.route('/employees', methods=['GET'])
def get_employees():
    return employees

# Get a specific Employee by ID
@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    for employee in employees:
        if employee['id']== employee_id:
            return employee

    return {'error':'Employee not found'}

# Create an Employee
@app.route('/employees', methods=['POST'])
def create_employee():
    new_employee={'id':len(employees)+1, 'name':request.json['name'], 'department':request.json['department']}
    employees.append(new_employee)
    return new_employee

# Update an Employee
@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    for employee in employees:
        if employee['id']==employee_id:
            employee['name']=request.json['name']
            employee['department']=request.json['department']
            return employee 
    return {'error':'Employee not found'}

# Delete an Employee
@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    for employee in employees:
        if employee['id']==employee_id:
            employees.remove(employee)
            return {"data":"Employee Deleted Successfully"}

    return {'error':'Employee not found'}

# Run the flask App
if __name__ == '__main__':
    app.run(debug=True)