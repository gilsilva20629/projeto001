let idCount = 0;
export const pages = [];
export let currentPage = 0;
export function incrementCurrentPage(){
    currentPage++;
}

export function decrementCurrentPage(){
    currentPage--;
}

//pages.pop(); remove ultimo
//pages.shift(); remove primeiro
//let r=50, g=10, b=20;
//let backgroundColor = rgb(10,10,10);



export function createMain(){

    const main = window.document.createElement("main")
    main.id = idCount;
    main.name = "mainContainer";
    main.style = "border: 1px solid black; margin: 22px; padding: 10px;"; 
    // `background-color: ${backgroundColor};`; // Template String ${}
    idCount++;
    return main;
}

export function createStdDiv(){

    const div = window.document.createElement("div");
    div.style = "width:23.3%; height:300; border:1px solid black; margin:5px; padding:5px; display:inline-block;";
    div.className = "slot_prod";

	const img = window.document.createElement("img");
	img.src = "./img/generic.jpg";
	img.style.width = "100%";
	img.style.height = "200px";
	img.id = "img";
	//console.log(img);
	//div.img = img; // passo adicional nescessario porque img não tem src ou atributo relevante definido fazendo img retornar undefined
	div.appendChild(img);
	//console.log(div);

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

	const button = window.document.createElement("button");
	button.innerText = "add shopping cart";
	button.name = "add";
	button.id = "add";
	button.type = "button";
	button.onclick = function(event){
		window.addCart(event);
	};
	//button.addEventListener('click', function(event) {
	//window.addcart(event);
	//});

	div.appendChild(button);

    return div;
}

export function createHorDiv(){

    const div = window.document.createElement("div");
    div.id = idCount;
    div.className = "horizontal";
    div.style = "width:48%; height:300px; border: 1px solid black; margin:5px; padding:5px; display:inline-block;";
    idCount++;
    return div;
}

export function createVerDiv(){

    const div = window.document.createElement("div");
    div.id = idCount;
    div.className = "vertical";
    div.style = "width:31%; height:600px; border: 1px solid black; margin:5px; padding:5px; display:inline-block;";
    idCount++;
    return div;
}

export function createBlockDiv(){

    const div = window.document.createElement("div");
    div.id = idCount;
    div.className = "block";
    div.style = "width:90%; height:300px; border: 1px solid black; margin:5px; padding:5px;";
    idCount++;
    return div;
}

export function appendToBody(tag){
    window.document.body.appendChild(tag);
}

export function removeFromBody(tag){
    window.document.body.removeChild(tag);
}
    
export function appendMain(tag){
    window.document.querySelector("main").appendChild(tag);
}

export function mainFill(){
    appendMain(createBlockDiv());
    for(let i=0; i<2; i++){
        appendMain(createHorDiv());
    }
    for(let i=0; i<3; i++){
        appendMain(createVerDiv());
    }
    for(let i=0; i<4; i++){
        appendMain(createStdDiv());
    }
}

let id = 0;
export function StdDivFill(products){
    let count = 0;
    const divs = [];
    while(id < products.length-1 && count < 20){

        const div = createStdDiv();
        div.id = id;
                
        div.querySelector(`img[id="img"]`).src = products[id]["images"][0];
        div.querySelector(`small[id="title"]`).innerHTML = products[id]['title'];
        div.querySelector(`small[id="category"]`).innerHTML = "Category: " + products[id]['category'];
        div.querySelector(`small[id="price"]`).innerHTML = "R$ " + products[id]['price'];
        div.querySelector(`small[id="stock"]`).textContent = "Disponível: " + products[id]['stock'];
        //div.querySelector(`small[id="barcode"]`).innerHTML = products[id]['meta']['barcode'];
        //div.querySelector(`small[id="qrcode"]`).innerHTML = products[id]['meta']['qrCode'];
        //div.querySelector(`small[id="rating"]`).innerHTML = "Rating: " + products[id]['rating'];
        
        divs.push(div);
        count++;
        id++;
    }
    //console.log(divs);
    return divs;
}
export function nextPage(products){
    try {
        removeFromBody(window.document.getElementsByTagName('main')[0]);
        appendToBody(pages[currentPage+1]);
        currentPage++;
        window.document.getElementById('label').innerHTML = currentPage ;
        if(currentPage == 1){
            window.document.getElementById('previous').disabled = false;
        };
        
    } catch(err) {
        //console.log("Erro: ", err);
        //console.log("TipoErro: ", typeof err);
        //console.log(err.name);
        //removeFromBody(window.document.getElementsByTagName('main')[0])
        const main = createMain();
        appendToBody(main);
        const divs = StdDivFill(products);
        divs.forEach( (element) => {
            appendMain(element);
        });
        let t = pages.push(main);
        console.log(t);
        idCount++;
        currentPage++;
        window.document.getElementById('label').innerHTML = currentPage;
        if(currentPage == 1){
            window.document.getElementById('previous').disabled = false;
        };
        
    }
}

export function previousPage(){
    removeFromBody(window.document.getElementsByTagName('main')[0]);
    appendToBody(pages[currentPage-1]);
    currentPage--;
    window.document.getElementById('label').innerHTML = currentPage;
    if(currentPage == 0){
        window.document.getElementById('previous').disabled = true;
    };
}