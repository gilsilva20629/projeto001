export function feedbackClear(){
	let feedback_user = window.document.getElementById("frm-user");
	let feedback_client = window.document.getElementById("frm-client");
	let feedback_product = window.document.getElementById("frm-product");
	feedback_user.textContent = "";
	feedback_client.textContent = "";
	feedback_product.textContent = "";
}

// javascript import falha caregado pelo protocolo file:// devido a CORS policy
// javascript import falha caregado pelo protocolo file:// devido a CORS policy
// javascript import falha caregado pelo protocolo file:// devido a CORS policy
// javascript import falha caregado pelo protocolo file:// devido a CORS policy
// javascript import falha caregado pelo protocolo file:// devido a CORS policy


function validateForm(event){
	event.preventDefault();	// Impede o envio imediato do formulário.
	feedbackClear();
	let form = event.target; // 'target' elemento que disparou o evento
	//console.log("Detalhes do evento: ", event, event.target);


	let url = "https://aprendendoapigithub-production.up.railway.app/cadastro";
	if (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1"){
		url = "http://127.0.0.1:5000/cadastro";
	}	
	console.log("hostname: ", window.location.hostname);
	console.log("url: ", url);

	let feedback_user = window.document.getElementById("frm-user");
	let feedback_client = window.document.getElementById("frm-client");
	let feedback_product = window.document.getElementById("frm-product");

	if (form.name == "form-user") {
		const user = window.document.getElementById("user").value;
		const password = window.document.getElementById("password").value;
		const tipo = window.document.getElementById("type").value;
		const op_type = window.document.getElementById("op_type_user").value;

		fetch(url, {
			method: "POST",
			headers: {
				"Access-Control-Allow-Origin": "no-cors",
				// "Access-Control-Allow-Origin": "*", // Use '*' para permitir todas as origens, se necessário
				"Content-Type": "application/json"
			},
			body: JSON.stringify({
				"arg1": user,
				"arg2": password,
				"arg3": tipo,
				"arg4": op_type
			})
		})
		.then(response => {
			if(!response.ok){
				throw new Error('Netwok: A resposta da rede não foi boa.');
			}

			return response.text();  // ou response.json() se a resposta for JSON.
		})
		.then(dados => {
			window.alert(dados);
			if(dados == "OK"){
				feedback_user.innerHTML = "O cadastro realizado com sucesso.";				
			}
		})
		.catch(error => {
			console.log("Log de erro: ", error, typeof error);
		});

	} else if (form.name == "form-client") {
		const name = window.document.getElementById("client").value;
		const address = window.document.getElementById("address").value;
		const contact = window.document.getElementById("contact").value;
		const op_type = window.document.getElementById("op_type_client").value;

		fetch(url, {
			method: "POST",
			headers: {
				"Access-Control-Allow-Origin": "no-cors",
        		// "Access-Control-Allow-Origin": "*", // Use '*' para permitir todas as origens, se necessário
				"Content-Type": "application/json"
			},
			body: JSON.stringify({
				"arg1": name,
				"arg2": address,
				"arg3": contact,
				"arg4": op_type
			})
		})
		.then(response => {
			if(!response.ok){
				throw new Error('Netwok: A resposta da rede não foi boa.');
			}
			return response.text();  // ou response.json() se a resposta for JSON.
		})
		.then(dados => {
			window.alert(dados);
			if(dados == "OK"){
				feedback_client.innerHTML = "O cadastro realizado com sucesso.";
			}
		})
		.catch(error => {
			console.log("Log de erro: ", error, typeof error);
		});

	}else if(form.name == "form-product"){
		const product_name = window.document.getElementById("product_name").value;
		const category = window.document.getElementById("category").value;
		const unit = window.document.getElementById("unit").value;
		const op_type = window.document.getElementById("op_type_product").value;

		fetch(url, {
			method: "POST",
			headers: {
				"Access-Control-Allow-Origin": "no-cors",
				// "Access-Control-Allow-Origin": "*", // Use '*' para permitir todas as origens, se necessário
				"Content-Type": "application/json"
			},
			body: JSON.stringify({
				"arg1": product_name,
				"arg2": category,
				"arg3": unit,
				"arg4": op_type
			})
		})
		.then(response => {
			if(!response.ok){ 
				throw new Error('Netwok: A resposta da rede não foi boa.');
			}

			return response.text();  // ou response.json() se a resposta for JSON.
		})
		.then(dados => {
			window.alert(dados);
			if(dados == "OK"){
				feedback_product.innerHTML = "O cadastro realizado com sucesso.";
				
			}
		})
		.catch(error => {
			console.log("Log de erro: ", error, typeof error);
		});

	}else{

		/*
		A TRY declaração define um bloco de código a ser executado (para tentar).

		A CATCH declaração define um bloco de código para lidar com qualquer erro.

		A FINALLY instrução define um bloco de código a ser executado independentemente do resultado.

		A THROW declaração define um erro personalizado.
		

		try{	
			console.log("Nome do formulario", form.name);
		}
		catch(err){
			console.log(err.message); 	// A CATCH declaração define um bloco de código para lidar com qualquer erro.
		}
		finally{
			// A FINALLY instrução define um bloco de código a ser executado independentemente do resultado.

			// throw new Error("Esse e um erro que eu criei agora")
		}
		*/
	};
}

export function createDiv(){
	const div = window.document.createElement("div");
    div.style = "width:23.5%; height:300; border:1px solid black; margin:5px; padding:5px; display:inline-block;";
    div.className = "slot_prod";

	const img = window.document.createElement("img");
	img.src = "./generic.jpg";
	img.style.width = "100%";
	img.style.height = "200px";
	img.id = "img";
	console.log(img);
	//div.img = img; // passo adicional nescessario porque img não tem src ou atributo relevante definido fazendo img retornar undefined
	div.appendChild(img);
	console.log(div);

	const p = window.document.createElement("p");

	const title_small = window.document.createElement("small");
	title_small.id = "title";
	const category_small = window.document.createElement("small");
	category_small.id = "category";
	const price_small = window.document.createElement("small");
	price_small.id = "price";
	const stock_small = window.document.createElement("small");
	stock_small.id = "stock";
	const barcode_small = window.document.createElement("small");
	barcode_small.id = "barcode";
	const qrcode_small = window.document.createElement("small");
	qrcode_small.id = "qrcode";
	const rating_small = window.document.createElement("small");
	rating_small.id = "rating";
	
	p.appendChild(title_small);
	p.appendChild(window.document.createElement("br"));
	p.appendChild(category_small);
	p.appendChild(window.document.createElement("br"));
	p.appendChild(price_small);
	p.appendChild(window.document.createElement("br"));
	p.appendChild(stock_small);
	p.appendChild(window.document.createElement("br"));
	p.appendChild(barcode_small);
	p.appendChild(window.document.createElement("br"));
	p.appendChild(qrcode_small);
	p.appendChild(window.document.createElement("br"));
	p.appendChild(rating_small);
	p.appendChild(window.document.createElement("br"));

	div.appendChild(p);

    return div;
}


export async function carregarProdutos(){
	let url = "https://aprendendoapigithub-production.up.railway.app/products";
	if (window.location.hostname == "localhost" || window.location.hostname == "127.0.0.1"){
		url = "http://127.0.0.1:5000/products";
	}


	let resposta = null;
	let dados = null;

	try{
		
		resposta  = await fetch(url, {method: "GET"});
		if (!resposta.ok) {
            throw new Error(`HTTP error! status: ${resposta.status}`);
        }

		dados = await resposta.json();
		//console.log(dados["products"]);
		
	}
	catch( error ){
		console.error("Error: ", error, "Msg: ", error.message);
	}
	finally{
		// A FINALLY instrução define um bloco de código a ser executado independentemente do resultado.

		// throw new Error("Esse e um erro que eu criei agora")
	}

	return dados ? dados["products"] : []; 	// usando condicional ternario
}


// declaracao "export" habilita para import via <script type="module>.
//você não pode usar a palavra-chave default mais de uma vez em um único módulo.
export default validateForm;

