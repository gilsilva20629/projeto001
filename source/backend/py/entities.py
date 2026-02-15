import random
import hashlib
import uuid


symbol = "abcdefghijklmnopqrstuvxywz0123456789_!@#$%&" # [0:25] [26:35] [36:42]
tipos = ["normal", "manager", "admin"]
pesos = [0.9,0.09,0.01]


def genarate_info_user_test():
	name = ""
	password = ""


	for i in range(16):
		#generate name
		for j in random.choice(symbol[0:25]):
			name += j

		#generate password
		for j in random.choice(symbol):
			password += j
	
	#enconding password
	h = hashlib.sha256()
	h.update(password.encode())
	password_hash = password + "." + h.hexdigest()
	

	return name, password_hash

'''
print(genarate_info_user())
name, password, tipo = genarate_info_user()
print(name)
print(password)
print(tipo)
'''


class User():

	def __init__(self, name:str, password:str, tipo:str):
		#self.id = random.randint(1,10000)
		self.id = str(uuid.uuid4())
		self.name = name
		self.password = password
		self.tipo = tipo
		#self.tipo_teste = random.choices(tipos, weights=pesos, k=1)[0]

class Client():
	
	'''
		CREATE TABLE client(
			id varchar(36),
			name varchar(16),
			address varchar(32),
			contact varchar(32),
			client_id int NOT NULL AUTO_INCREMENT,
			user_id int,
			PRIMARY KEY (client_id),
			FOREIGN KEY (user_id) REFERENCES user(user_id)
			);
	'''
	
	def __init__(self, name:str, address:str, contact:str):
		self.id = str(uuid.uuid4())
		self.name = name
		self.address = address
		self.contact = contact

class Product():

	def __init__(self, name: str, category: str, unit: str):
		self.id = str(uuid.uuid4())
		self.name = name
		self.category = category
		self.unit = unit