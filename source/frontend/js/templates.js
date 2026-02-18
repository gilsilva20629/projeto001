let idCount = 0;
//let stringBackgroundColor = '#901010';
//let numberBackgroundColor = Number(stringBackgroundColor);


export function createMain(){

    const main = window.document.createElement("main")
    main.id = idCount;
    main.name = "mainContainer";
    main.style = "border: 1px solid black; margin: 22px padding: 10px;";
    idCount++;
    //numberBackgroundColor+50;
    //stringBackgroundColor = toString(numberBackgroundColor);
    return main;
}

export function createStdDiv(){

    const div = window.document.createElement("div");
    div.id = idCount;
    div.className = "standard";
    div.style = "width:23%; height:300px; border: 1px solid black; margin:5px; padding:5px; display:inline-block;";
    idCount++;
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