from flask import Flask, request, send_from_directory
from flask_cors import CORS
from py import crud as CDB
import json
import os


app = Flask(__name__)
CORS(app)  # Isso permite CORS para todas as rotas

'''
Cross-Origin Resource Sharing (CORS) - HTTP | MDN - MDN Web Docs
O padrão Cross-Origin Resource Sharing trabalha adicionando novos cabeçalhos HTTP
que permitem que os servidores descrevam um conjunto de origens que possuem permissão a ler uma informação usando o navegador.
'''


#<servidor WEB railway >#########################################
@app.route('/', methods=['GET'])
def home_page():
    return send_from_directory('../frontend', 'index.html')

@app.route('/cadastro.html', methods=['GET'])
def cadastro_page():
    return send_from_directory('../frontend', 'cadastro.html')

@app.route('/shopping.html', methods=['GET'])
def shop_page():
    return send_from_directory('../frontend', 'shopping.html')

#</servidor WEB railway >#########################################

@app.route('/auth', methods=['POST'])
def auth():
	# ------------ Recepcao do request----------------
	'''
	application/x-www-form-urlencoded
	multipart/form-data
	text/plain
	text/html; charset=utf-8
	application/json
	'''
	resposta = ""
	if request.headers["Content-Type"] == "application/x-www-form-urlencoded" :
		authorization = request.headers['Authorization']
		op_type = request.form["extra"]
		#name = request.form["name_user"]
		#password = request.form["password"]
		
	elif request.headers["Content-Type"] == "text/html; charset=utf-8" :
		authorization = request.headers['Authorization']
		#name = request.form.get("name_user")
		#password = request.form.get("password")
		op_type = request.form.get("extra")
		
	elif request.headers["Content-Type"] == "application/json" :
		authorization = request.headers['Authorization']
		#name = request.json.get("name_user")
		#password = request.json.get("password")
		op_type = request.json.get("extra")
		
	else:
		resposta = "content/media type do not supported: "+request.headers["Content-Type"]
		return resposta
		#print(resposta)
		
	# ------------ Executar Testes --------------------

	#print(request.json)
	#teste.outhers()
	
	''' exemplos de elementos do request
	print(request.method)
	print(request.status_code) 
	print(request.url)
	print(request.encoding)
	print(request.form)
	print(request.args)
	print(request.headers)
	print(request.data)
	print(request.content)
	print(request.json)
	print(request.text)
	print(request.auth)
	print(request.cookies)
	print(request.timeout)
	print(request.params)
	print(request.body)
	'''

	# ------------ Executar operacoes --------------------
	match op_type:
		case "1": #login
			resp = CDB.auth(authorization)
			resposta = {'status': 'authorized', 'status_code': '200'}
			if resp :
				for pair in resp.items():
					resposta.update({pair})
				resposta = json.dumps(resposta)
				print(resposta, type(resposta))
			else:
				resposta = json.dumps({'status': 'Unauthorized', 'status_code': '401' })
		case "2":
			pass

		case "_":
			resposta = False
			
	# ------------ Resposta --------------------------
	return resposta

@app.route("/cadastro", methods=['POST'])
def cadastros():

	# ------------ Recepcao do request----------------
	'''
	application/x-www-form-urlencoded
	multipart/form-data
	text/plain
	text/html; charset=utf-8
	application/json
	'''

	if request.headers["Content-Type"] == "application/x-www-form-urlencoded" : # Via formulario
		arg1 = request.form["arg1"]
		arg2 = request.form["arg2"]
		arg3 = request.form["arg3"]
		arg4 = request.form["arg4"]
		arg5 = request.form["arg5"]
		arg6 = request.form["arg6"]
		op_type = arg6
		resposta = "OK"

	elif request.headers["Content-Type"] == "text/html;charset=utf-8" :
		arg1 = request.form.get("arg1")
		arg2 = request.form.get("arg2")
		arg3 = request.form.get("arg3")
		arg4 = request.form.get("arg4")
		arg5 = request.form.get("arg5")
		arg6 = request.form.get("arg6")
		op_type = arg6
		resposta = "OK"

	elif request.headers["Content-Type"] == "application/json" :
		arg1 = request.json.get("arg1")
		arg2 = request.json.get("arg2")
		arg3 = request.json.get("arg3")
		arg4 = request.json.get("arg4")
		arg5 = request.json.get("arg5")
		arg6 = request.json.get("arg6")
		op_type = arg6
		resposta = "OK"

	elif request.headers["Content-Type"] == "text/plain;charset=UTF-8" :
		text = request.data.decode("utf-8")
		print("Formato text/plain: ", text)
		resposta = "content/media type do not supported: "+request.headers["Content-Type"]
	else:
		resposta = "content/media type do not supported: "+request.headers["Content-Type"]
		#print(resposta)
		

	# ------------ Executar Testes --------------------

	#print(request.json)
	#teste.outhers()
	

	''' 
	print(request.method)
	print(request.status_code) 
	print(request.url)
	print(request.encoding)
	print(request.form)
	print(request.args)
	print(request.headers)
	print(request.data)
	print(request.content)
	print(request.json)
	print(request.text)	X  Invalido!
	print(request.auth)
	print(request.cookies)
	print(request.timeuot)
	print(request.params)
	print(request.body)
	'''

	# ------------ Executar operacoes --------------------

	if resposta == "OK":
		match op_type:

			case "2.1": #Cadastro de usuario.
				name = arg1
				password = arg2
				tipo = arg3
				address = arg4
				contact = arg5

				r = CDB.cadUser(name, password, tipo, address, contact)
				if r :
					resposta = "OK"
				else:
					resposta = "NOK"

			case "2.2": # cadastro de cliente.
				name = arg1
				address = arg2
				contact = arg3

				r = CDB.cadClient(name, address, contact)
				if r :
					resposta = "OK"
				else:
					resposta = "NOK"

			case "2.3": # cadastro de produtos.
				product_name = arg1
				category = arg2
				unit = arg3

				r = CDB.cadProduct(product_name, category, unit)
				if r :
					resposta = "OK"
				else:
					resposta = "NOK"

			case "_":
					resposta = "op_type {op_type} invalid!"	

		return resposta
	else:
		return resposta

@app.route("/products", methods=["GET"])
def products():
	with open(file="./cache/products.txt", mode="r", encoding="utf-8") as file: 
	# com 'with' abre e fecha o arquivo automaticamente(forma segura).
	
		#return json.dumps(file.read())
		return file.read()

	'''
	file = open("./img/products.html", "r")
	response = file.read()
	file.close()
	return response
	'''

#def auth():

#def token():
	

if __name__ == '__main__':
	if os.getenv('HOME') == "/home/susan":
		app.run(host="127.0.0.1", port=5000 , debug=True)  # listen localhost
	else:
		app.run(host="0.0.0.0", port=5000 , debug=True)  # listen all ips
	