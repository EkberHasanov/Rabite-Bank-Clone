var opt = document.querySelector("#valyuta");
var precentage = document.querySelector("#precentage");
var mounths = document.querySelector("#mounth");
var inputMoney = document.querySelector("#start-money");
var currentObj;
var pr;
var time;
var start;
var m;

function check(a){
    let res = 0;
    if(a.target.matches(`#${currentObj.getAttribute("id")} option`)){
        let val = currentObj.options[currentObj.selectedIndex].value;
        res = val;    
    }
    return res;
}

function printRes(){
    start = parseInt(inputMoney.value);
    let result = time*start*pr/100;
    if(isNaN(result)){
        document.querySelector("#res1 p:last-child").textContent = "Wrong Input"
        document.querySelector("#res2 p:last-child").textContent = "" 
    }
    else{
        document.querySelector("#res1  p:last-child").textContent = `${result} ${m}`
        document.querySelector("#res2  p:last-child").textContent = `${start + result} ${m}`;
    }
    
}

opt.addEventListener("click",function(e){
    currentObj = this;
    m = check(e);
})


precentage.addEventListener("click",function(e){
    currentObj = this;
    let res = check(e);
    pr = parseInt(res);   
})

mounths.addEventListener("click",function(e){
    currentObj = this;
    let res = check(e);
    time = parseInt(res);
})

document.addEventListener("submit",function(e){
    e.preventDefault();
    printRes()
})


// mounths.addEventListener("click",function)
