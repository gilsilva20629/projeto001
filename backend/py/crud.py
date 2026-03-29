import mysql.connector
import os                #usada para pegar as variaveis de ambiente.
import hashlib
from py.object import User, Client, Product
import json
import base64
import urllib.parse		#usada para converter char escapados %xx em char normal.
from py.auth import genarateSecrets
import traceback 		#Imprimir o rastreamento do erro no except clausula.
import time

def start():

	#obtendo variaveis locais
	#HOST = os.getenv("HOST")
	USER = os.getenv("USER")
	
	#obtendo variaveis remotas railway.com
	MYSQLHOST = os.getenv("MYSQLHOST")
	MYSQLPORT = os.getenv("MYSQLPORT")
	MYSQLUSER = os.getenv("MYSQLUSER")
	MYSQLPASSWORD = os.getenv("MYSQLPASSWORD")
	MYSQLDATABASE = os.getenv("MYSQLDATABASE")
	DATABASE_URL = os.getenv("DATABASE_URL")

	try:
		if USER != "susan":			#variaveis remotas railway.com
			print("Ambiente: ", MYSQLHOST)
			mydb = mysql.connector.connect(
				host = os.getenv("MYSQLHOST"),
				port = os.getenv("MYSQLPORT"),
				user = os.getenv("MYSQLUSER"),
				password = os.getenv("MYSQLPASSWORD"),
				database = os.getenv("MYSQLDATABASE")
			)
			print("Connected in DB railway...")
		else:
			print("Ambiente: ", USER)
			mydb = mysql.connector.connect(
				host = "localhost",
				user = "root",
				password = "Nsg@2024",
				database ="ecommerce"
			)
			print("Connected in DB localhost...")

	except Exception as err:
		print(err, type(err))
		print("Erro: Não foi possivel conectar ao database!")
	
	mycursor = mydb.cursor()

	return mydb, mycursor

	'''
	mycursor.execute("SHOW TABLES")
	mycursor.execute("DROP TABLE usuario")
	results = mycursor.fetchall()
	print(results)
	
	# Exibir os resultados
	print(":----- via 'for' -----:")
	for linha in results:
		print(linha)

	# Fechar a conexão
	mycursor.close()
	mydb.close()

	#mydb.commit()
	'''

def quit(mydb, mycursor):
	mycursor.close()
	mydb.close()
	print("Closing DB...")

def exit(mydb, mycursor):
	mycursor.close()
	mydb.close()
	print("Closing DB...")

''' Deprecated (usar somente para testes

def command_extra(command=None):
	if command!=None :

		command = command.replace("\\", "")
		command = command.replace("\t", "")
		command = command.replace("\n", "")

		try:
			print("Testando split: ", command.split(";"), end="\n")
			command = command.split(";")
			print("Comandos limpos: ", command, end="\n")

			for c in command:
				mycursor.execute(c)

		except Exception as err:
			print("command extra falhou!")	
'''

''' Deprecated (usar somente para testes

def add_user_test(user, command_x=None):
	start()

	command_extra(command_x)

	sql = "INSERT INTO user(id, name, password, tipo) VALUES(%s, %s, %s)"
	values = (user.id, user.name, user.password, user.tipo)

	#sql = "INSERT INTO user(id, name, password, `tipo`) VALUES(%s, %s, %s, %s)"
	#values = (user.id, user.name, user.password, user.tipo)

	mycursor.execute(sql, values)
	mydb.commit()
	print(mycursor.rowcount, "Record Inserted.")
	exit()
'''

def auth(authorization:  str)-> dict | bool:
	#print(authorization.split(" ")[1])
	Bytes = bytes(authorization.split(" ")[1], 'utf-8')
	#print(Bytes)
	credentials = base64.b64decode(Bytes)
	#print(credentials, type(credentials))
	#print(urllib.parse.unquote(credentials), type( urllib.parse.unquote(credentials) ) )
	name, password = urllib.parse.unquote(credentials).split(":") #converte caracter escapado do tipo %xx para não escapado.
	#print(name, password)
	#mydb, mycursor = start()

	results = search_user(name)[0]
	#print(results)
	for row in results:
		if name in row:
			#print(r)
			#gerar hash do password
			#h = hashlib.sha256()
			#h.update(password.encoded())
			#h.hexdigest()
			user_id = row[3]

			if password == (row[1])[0:16] :
				token = genarateSecrets()
				add('session', user_id=user_id, token=token, expires="session", max_age=3600)

				return {'token': token, 'expires': 'session', 'max_age': 3600}
			else:
				return False
		else:
			return False

def cadUser(name: str, password: str, tipo: str, address: str, contact: str, command_x=None)-> bool:
	mydb, mycursor = start()
	try:
		#command_extra(command_x)

		usuario = User(name, password, tipo, address, contact)
		sql = "INSERT INTO user(name, password, tipo, address, contact) VALUES(%s, %s, %s, %s, %s)"
		values = (usuario.name, usuario.password, usuario.tipo, usuario.address, usuario.contact)

		mycursor.execute(sql, values)
		mydb.commit()
		print(mycursor.lastrowid, mycursor.rowcount,  "Record Inserted")
		print("fetch: ", mycursor.fetchall(), len(mycursor.fetchall()), type(mycursor.fetchall()))
		# fetchone(), fectchmany(size), fetchall()
		''' 
		Método			Descrição
		fetchone()		Retorna a próxima linha do resultado da consulta como uma tupla começando da primeira. Se não houver mais linhas, retorna None.
		fetchmany(size)	Retorna o número especificado de linhas (definido por size) do resultado da consulta como uma lista de tuplas. Se não houver mais linhas, retorna o que estiver disponível.
		fetchall()		Retorna todas as linhas do resultado da consulta como uma lista de tuplas. Este é o método que você mencionou.
		'''
		
		return True

	except Exception as error:
		print("query falhou!", error, type(error))
		return False
	exit(mydb, mycursor)

def cadClient(name, address, contact):
	mydb, mycursor = start()
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
	try:
		#command_extra(command_x)

		cliente = Client(name, address, contact)
		sql = "INSERT INTO client(id, name, address, contact) VALUES(%s, %s, %s, %s)"
		values = (cliente.id, cliente.name, cliente.address, cliente.contact)

		mycursor.execute(sql, values)
		mydb.commit()
		print("Reg. n°: ", mycursor.lastrowid, mycursor.rowcount,  "Record Inserted")
		print("fetch: ", mycursor.fetchall(), len(mycursor.fetchall()), type(mycursor.fetchall()))
		# fetchone(), fectchmany(size), fetchall()
		''' 
		Método			Descrição
		fetchone()		Retorna a próxima linha do resultado da consulta como uma tupla começando da primeira. Se não houver mais linhas, retorna None.
		fetchmany(size)	Retorna o número especificado de linhas (definido por size) do resultado da consulta como uma lista de tuplas. Se não houver mais linhas, retorna o que estiver disponível.
		fetchall()		Retorna todas as linhas do resultado da consulta como uma lista de tuplas. Este é o método que você mencionou.
		'''
		
		return True

	except Exception as error:
		print("query falhou!", error, type(error))
		return False
	exit(mydb, mycursor)

def cadProductBatch():
	mydb, mycursor = start()

	data = ""
	with open(file="./cache/products.txt", mode="r", encoding="utf-8") as file: 
	# com 'with' abre e fecha o arquivo automaticamente(forma segura).
		data = json.loads(file.read())

	name = ""
	category = ""
	unit = "und"
	stock = ""
	price = ""
	sku = ""
	itemsList = data['products']
	for i in itemsList:
		name = i['title']
		category = i['category']
		stock = i['stock']
		price = i['price']
		sku = i['sku']
	
		try:
			produto = Product(name, category, unit)
			sql = "INSERT INTO product(name, category, unit, stock, price, sku) VALUES(%s, %s, %s, %s, %s, %s)"
			values = (produto.name, produto.category, produto.unit, stock, price, sku)
			mycursor.execute(sql, values)
			mydb.commit()
			print("Reg. n°: ", mycursor.lastrowid, mycursor.rowcount,  "Record Inserted.")
			#print("fetch: ", mycursor.fetchall(), len(mycursor.fetchall()), type(mycursor.fetchall()))
			# fetchone(), fectchmany(size), fetchall()
			
			#Método			Descrição
			#fetchone()		Retorna a próxima linha do resultado da consulta como uma tupla começando da primeira. Se não houver mais linhas, retorna None.
			#fetchmany(size)	Retorna o número especificado de linhas (definido por size) do resultado da consulta como uma lista de tuplas. Se não houver mais linhas, retorna o que estiver disponível.
			#fetchall()		Retorna todas as linhas do resultado da consulta como uma lista de tuplas. Este é o método que você mencionou.
			
			#return True

		except Exception as error:
			print("Falha ao cadastrar produto!", error, type(error), traceback.print_exc())
			#return False

	exit(mydb, mycursor)

def cadImgBatch():
	mydb, mycursor = start()

	data = ""
	with open(file="./cache/products.txt", mode="r", encoding="utf-8") as file: 
	# com 'with' abre e fecha o arquivo automaticamente(forma segura).
		data = json.loads(file.read())

	name = ""
	url = ""
	itemsList = data['products']
	for i in itemsList:
		name = i['title']
		url = i['images'][0]
		#print(name)
	
		try:
			mycursor.execute('SELECT * FROM product WHERE name="{0}"'.format(name))
			product_id = mycursor.fetchall()[0][0]
			
			sql = "INSERT INTO product_img(product_id, url) VALUES(%s, %s)"
			values = (product_id, url)
			mycursor.execute(sql, values)
			mydb.commit()
			print("Reg. n°: ", mycursor.lastrowid, mycursor.rowcount,  "Record Inserted.")
			
        
            #print("fetch: ", mycursor.fetchall(), len(mycursor.fetchall()), type(mycursor.fetchall()))
            # fetchone(), fectchmany(size), fetchall()

            #Método			Descrição
            #fetchone()		Retorna a próxima linha do resultado da consulta como uma tupla começando da primeira. Se não houver mais linhas, retorna None.
            #fetchmany(size)	Retorna o número especificado de linhas (definido por size) do resultado da consulta como uma lista de tuplas. Se não houver mais linhas, retorna o que estiver disponível.
            #fetchall()		Retorna todas as linhas do resultado da consulta como uma lista de tuplas. Este é o método que você mencionou.

            #return True

		except Exception as error:
			print("Falha ao cadastrar produto!", error, type(error), traceback.print_exc())
			#return False

	exit(mydb, mycursor)

def cadProduct(product_name: str, category: str, unit: str)-> bool:
	mydb, mycursor = start()
	try:
		
		produto = Product(product_name, category, unit)
		sql = "INSERT INTO product(name, category, unit, stock, price) VALUES(%s, %s, %s, %s, %s)"
		values = (produto.name, produto.category, produto.unit, product.stock, product.price)
		mycursor.execute(sql, values)
		mydb.commit()
		print("Reg. n°: ", mycursor.lastrowid, mycursor.rowcount,  "Record Inserted.")
		#print("fetch: ", mycursor.fetchall(), len(mycursor.fetchall()), type(mycursor.fetchall()))
		# fetchone(), fectchmany(size), fetchall()

		#Método			Descrição
		#fetchone()		Retorna a próxima linha do resultado da consulta como uma tupla começando da primeira. Se não houver mais linhas, retorna None.
		#fetchmany(size)	Retorna o número especificado de linhas (definido por size) do resultado da consulta como uma lista de tuplas. Se não houver mais linhas, retorna o que estiver disponível.
		#fetchall()		Retorna todas as linhas do resultado da consulta como uma lista de tuplas. Este é o método que você mencionou.
		
		
		return True
	except Exception as error:
		print("Falha ao cadastrar produto!", error, type(error))
		return False

	exit(mydb, mycursor)


def search_user(name=None, user_id=None, tipo=None):
	mydb, mycursor = start()
	n = []
	u = []
	t = []
	#response = []
	if name == None and user_id == None and tipo == None :
		exit(mydb, mycursor)
		return "Ivalid parameters!"
	else:
		#mycursor.execute(f"SELECT * FROM user WHERE name={name}")
		#results = mycursor.fetchall()
		mycursor.execute("SELECT * FROM user")
		results = mycursor.fetchall()

		#print(results, type(results))

		#for i in results:
		#	print(i)

		#for i in mycursor:, type(results
		#	print(i[1], i[4], i[3], type(i[1]), type(i[4]), type(i[3]))

		
		if name is not None:
			#print(f"name: __________ __________ __________ {name}")
			for i in results:
				if name in i[0] :
					#print(i)
					n.append(i)
		
		if user_id is not None:
			#print(f"user_id: __________ __________ __________ {user_id}")
			for i in results:
				if user_id == i[3] :
					#print(i)
					u.append(i)
		
		if tipo is not None:
			#print(f"tipo: __________ __________ __________ {tipo}")
			for i in results:
				if tipo == i[2] :
					#print(i)
					t.append(i)
	#response.extend()
	exit(mydb, mycursor)
	return n, u, t

		
def list_users(command_x=None):
	mydb, mycursor = start()
	command_extra(command_x)
	mycursor.execute("SELECT user_id, name, tipo FROM user")
	results = mycursor.fetchall()
	
	return results
	exit(mydb, mycursor)


def remove(u_id, command_x=None):
	mydb, mycursor = start()
	command_extra(command_x)
	mycursor.execute(f"DELETE FROM user WHERE user_id={u_id}")
	mydb.commit()
	print(mycursor.rowcount, "Record(s) Deleted.")
	exit(mydb, mycursor)


def add(table: str, **data):
	""" Add data into the tables.
	
		Está função pretende substituir: cadUser, cadproduct, cadClient
		ou qualquer outro metodo de gravacão de dados em tabelas do database.
	"""
	try:
		mydb, mycursor = start()
		sql = "INSERT INTO {0} ({1}) VALUES ({2})".format(table,
			", ".join(str(key) for key in data.keys()) ,
			", ".join(str('%s') for value in data.values())
		)

		values = list(data.values())

		print("Preview SQL: ", sql, values)
		mycursor.execute(sql, values)
		mydb.commit()
		print("Row:", mycursor.lastrowid, mycursor.rowcount, "Record Inserted.")
		exit(mydb, mycursor)
		return True
	except Exception as error :
		print("Query falhou! Verifique se a tabela, os campos e valores são compativéis.\n",
		error, '\n', error.args, '\n', type(error), '\n', type(error).__name__, '\n', str(error), '\n', )
		traceback.print_exc()  # Imprime o rastreamento do erro
		exit(mydb, mycursor)
		return False
	exit(mydb, mycursor)

def productsToCache():
	mydb, mycursor = start()
	sql = "SELECT * FROM product JOIN product_img ON product.product_id=product_img.product_id ORDER BY product.product_id"
	mycursor.execute(sql)
	result = mycursor.fetchall()
	#print(result)

	products = []
	for t in result:
		template = {
			'id': '',
			'name': '',
			'category': '',
			'umb': '',
			'stock': '',
			'price': '',
			'sku': '',
			'image': ''
		}

		for i in t:
			index = t.index(i)
			match index :
				case 0:
					template['id']=i
					#template.update({'id': i})
				case 1:
					template['name']=i
				case 2:
					template['category']=i
				case 3:
					template['umb']=i
				case 4:
					template['stock']=i
				case 5:
					template['price']=i
				case 6:
					template['sku']=i
				case 7:
					#print("No match!")
					continue
				case 8:
					#print("No match!")
					continue
				case 9:
					template['image']=i
				case _:
					print("No there are any match!")
					break

		products.append(template)
		print(template)

	#data = time.time()
	directory = "/home/susan/programacao/projeto001/backend/cache/"
	with open(directory+"bd_products.txt", "w") as file:
		file.write( json.dumps(products, indent=4, separators=(',',':'), sort_keys=False) ) #sort_keys parameter to specify if the result should be sorted or not
	

