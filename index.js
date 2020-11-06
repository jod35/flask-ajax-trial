let xHttp=new XMLHttpRequest();


const handleStateChange=()=>{
    if(xHttp.readyState == 4){
        if(xHttp.status == 200){
            alert(`The server replied with ${xHttp.responseText}`);
        }
    }
}

const startRequest=()=>{
    
    xHttp.onreadystatechange=handleStateChange();
    xHttp.open("GET","http://localhost:5000/");

    xHttp.send(null);



}

