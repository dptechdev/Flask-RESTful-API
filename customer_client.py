import requests

def _url(path):
	return 'http://localhost:5000/api' + path

def add_customer(firstname, lastname):
	return requests.post(_url('/customers'), json= {
		'firstname': firstname,
		'lastname': lastname,
		})

def get_customers():
	return requests.get(_url('/customers'))


def describe_customer(customer_id):
	return requests.get(_url('/customers/{:d}/'.format(customer_id)))



def update_customer(customer_id, firstname, lastname):
	url = _url('/customers/{:d}/'.format(customer_id))
	return requests.put(url, json={
		'firstname': firstname,
		'lastname': lastname,
		})


def delete_customer(customer_id):
	return requests.delete(_url('/customers/{:d}/'.format(customer_id)))

if __name__ == '__main__':
	add_customer("Libby", "Patton")
	add_customer("Derek", "Pauley")
	add_customer("Vicki", "Patton")