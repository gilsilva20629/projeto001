import mysql.connector
import os                #usada para ppegar as variaveis de ambiente.
import hashlib
from .entities import User, Client, Product


def start():

	#obtendo variaveis locais
	#HOST = os.getenv("HOST")
	USER = os.getenv("USER")
	print("Ambiente: ", USER)

	#obtendo variaveis remotas railway.com
	MYSQLHOST = os.getenv("MYSQLHOST")
	MYSQLPORT = os.getenv("MYSQLPORT")
	MYSQLUSER = os.getenv("MYSQLUSER")
	MYSQLPASSWORD = os.getenv("MYSQLPASSWORD")
	MYSQLDATABASE = os.getenv("MYSQLDATABASE")
	DATABASE_URL = os.getenv("DATABASE_URL")

	try:
		if USER != "susan":			#variaveis remotas railway.com
			mydb = mysql.connector.connect(
				host = os.getenv("MYSQLHOST"),
				port = os.getenv("MYSQLPORT"),
				user = os.getenv("MYSQLUSER"),
				password = os.getenv("MYSQLPASSWORD"),
				database = os.getenv("MYSQLDATABASE")
			)
			print("Connected in DB railway...")
		else:
			mydb = mysql.connector.connect(
				host = "localhost",
				user = "root",
				password = "Nsg@2024",
				database ="db_teste01"
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


def quit():
	mycursor.close()
	mydb.close()

def exit():
	mycursor.close()
	mydb.close()

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
def login(name:  str, password: str, command_x=None)-> bool:
	start()
	#command_extra(command_x)

	results = search_user(name)[0]

	for r in results:
		if name in r:

			#gerar hash do password
			#h = hashlib.sha256()
			#h.update(password.encoded())
			#h.hexdigest()

			if password == (r[2])[0:16] :
				return True
			else:
				return False
	exit()


def cadUser(name: str, password: str, tipo: str, command_x=None)-> bool:
	mydb, mycursor = start()
	try:
		#command_extra(command_x)

		usuario = User(name, password, tipo)
		sql = "INSERT INTO user(id, name, password, tipo) VALUES(%s, %s, %s, %s)"
		values = (usuario.id, usuario.name, usuario.password, usuario.tipo)

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
	exit()

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
	exit()

def cadProduct(product_name: str, category: str, unit: str)-> bool:
	mydb, mycursor = start()
	try:
		
		produto = Product(product_name, category, unit)
		sql = "INSERT INTO product(id, name, category, unit) VALUES(%s, %s, %s, %s)"
		values = (produto.id, produto.name, produto.category, produto.unit)
		mycursor.execute(sql, values)
		mydb.commit()
		print("Reg. n°: ", mycursor.lastrowid, mycursor.rowcount,  "Record Inserted,", "fetch: ", mycursor.fetchall(), len(mycursor.fetchall()), type(mycursor.fetchall()))
		#print("fetch: ", mycursor.fetchall(), len(mycursor.fetchall()), type(mycursor.fetchall()))
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

	exit()

def search_user(name=None, user_id=None, tipo=None, command_x=None):
	mydb, mycursor = start()
	#command_extra(command_x)

	n = []
	u = []
	g = []

	if name == None and user_id == None and tipo == None :
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
				if name in i[1] :
					#print(i)
					n.append(i)
		
		if user_id is not None:
			#print(f"user_id: __________ __________ __________ {user_id}")
			for i in results:
				if user_id == i[4] :
					#print(i)
					u.append(i)
		
		if tipo is not None:
			#print(f"tipo: __________ __________ __________ {tipo}")
			for i in results:
				if tipo == i[3] :
					#print(i)
					g.append(i)
		
	
	return n, u, g
	exit()
		
def list_users(command_x=None):
	mydb, mycursor = start()
	command_extra(command_x)
	mycursor.execute("SELECT user_id, name, tipo FROM user")
	results = mycursor.fetchall()
	
	return results
	exit()

def remove(u_id, command_x=None):
	mydb, mycursor = start()
	command_extra(command_x)
	mycursor.execute(f"DELETE FROM user WHERE user_id={u_id}")
	mydb.commit()
	print(mycursor.rowcount, "Record(s) Deleted.")
	exit()


