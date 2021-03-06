from flask import Flask, request, jsonify, send_file
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api, Resource


app = Flask(__name__)
app.debug = True
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
api = Api(app)


class Customer(db.Model):
	__tablename__ = "customers"

	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(100))
	lastname = db.Column(db.String(100))

	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname

	@property 
	def to_json(self):
		return {
			"id": self.id,
			"firstname": self.firstname, 
			"lastname": self.lastname
		}

@app.route('/')
@app.route('/index')
def index():
	return jsonify(customers="/api/customers")

class CustomersResource(Resource):
	def get(self):
		customers = Customer.query.all()
		return jsonify({"customers": [c.to_json for c in customers] })


	def post(self):
		#use request parser?
		firstname = request.json['firstname']
		lastname = request.json['lastname']
		new_customer = Customer(firstname, lastname)
		db.session.add(new_customer)
		db.session.commit()

class CustomerResource(Resource):
	def put(self, id):
		customer = Customer.query.get(id)
		req = request.json['customer']
		customer.firstname = req['firstname']
		customer.lastname = req['lastname']
		db.session.commit()

	def delete(self, id):
		customer = Customer.query.get(id)
		db.session.delete(customer)
		db.session.commit()

if __name__ == '__main__':
	
	db.drop_all()
	db.create_all()

	api.add_resource(CustomersResource, '/api/customers', methods=['GET', 'POST'])
	api.add_resource(CustomerResource, '/api/customers/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])

	
	app.run()
	
