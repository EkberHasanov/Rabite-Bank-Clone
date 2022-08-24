
// var shareBtn = document.querySelector(".fancybox-close-small");
// shareBtn.addEventListener('click', () => {
//     console.log("Clicked");
//     document.querySelector(".share-box ").classList.add("opacity-0");
// });


var height = $('#main-header').height();

$(window).scroll(() => {
    if ($(this).scrollTop() > height + 40){
        $('#main-header').addClass('fixed');
        // $('#main-header').parent('div').removeClass('container');
        $('#main-header').parent('div').addClass('container-fluid');
        // $('#main-header').children('div').addClass('container');
        $(".main-bottom-header").addClass("none");
    }
    else{
        $('#main-header').removeClass('fixed');
        // $('#main-header').parent('div').addClass('container');
        $('#main-header').parent('div').removeClass('container-fluid');
        // $('#main-header').children('div').removeClass('container');
        $(".main-bottom-header").removeClass("none");
    };
});

$(".main-search-btn").focusin(() => {
    if ($(".main-search").hasClass("active")){
        console.log("active");
    }
    else{
        $(".main-search").addClass("active");
        console.log("active");
    };
});
$(".main-search").focusout(() => {
    $(".main-search").removeClass("active");
});



var totalCredit = document.querySelector("#total-credit");
var creditPercent = document.querySelector("#credit_last_percent");
var monthlyPayment = document.querySelector("#monthly_payment");

const sliderValue1  = document.querySelector(".slider-text-path");
const inputSlider1 = document.querySelector("#customRange1");
inputSlider1.oninput = (() => {
    var month = parseInt(inputSlider1.value);
    var credit = parseInt(inputSlider2.value);
    var percent = parseInt(inputSlider3.value);
    sliderValue1.textContent = month;
    totalCredit.textContent = (credit + (month/12 * (credit*percent)/100)).toFixed(2);
    creditPercent.textContent = (month/12 * (credit*percent)/100).toFixed(2);
    monthlyPayment.textContent = ((credit + (month/12 * (credit*percent)/100))/month).toFixed(2);
});
const sliderValue2  = document.querySelector(".text-path2");
const inputSlider2 = document.querySelector("#customRange2");
inputSlider2.oninput = (() => {
    var month = parseInt(inputSlider1.value);
    var credit = parseInt(inputSlider2.value);
    var percent = parseInt(inputSlider3.value);
    sliderValue2.textContent = credit;
    totalCredit.textContent = (credit + (month/12 * (credit*percent)/100)).toFixed(2);
    creditPercent.textContent = (month/12 * (credit*percent)/100).toFixed(2);
    monthlyPayment.textContent = ((credit + (month/12 * (credit*percent)/100))/month).toFixed(2);
});

const sliderValue3  = document.querySelector(".text-path3");
const inputSlider3 = document.querySelector("#customRange3");
inputSlider3.oninput = (() => {
    var month = parseInt(inputSlider1.value);
    var credit = parseInt(inputSlider2.value);
    var percent = parseInt(inputSlider3.value);
    sliderValue3.textContent = percent;
    totalCredit.textContent = (credit + (month/12 * (credit*percent)/100)).toFixed(2);
    creditPercent.textContent = (month/12 * (credit*percent)/100).toFixed(2);
    monthlyPayment.textContent = ((credit + (month/12 * (credit*percent)/100))/month).toFixed(2);
});


var scrollEventHandler = function(){
    window.scroll(0, window.pageYOffset)
}


var exchange_value_val = document.querySelector("#exchange_value_val");
console.log(exchange_value_val.selectIndex);

var euro_get = document.querySelector("#euro_get");
var usd_get = document.querySelector("#usd_get");
var euro_sale = document.querySelector("#euro_sale");
var usd_sale = document.querySelector("#usd_sale");
var exchange_input = document.querySelector(".exchange-input");
const exchange_value = document.querySelector(".exchange_value");
console.log(exchange_value_val.selectedIndex);
exchange_input.oninput = (() => {
    if (exchange_value_val.selectedIndex == "1"){
        console.log(exchange_input.value);
        console.log(usd_get.textContent);
        if (exchange_input.value == "" ){
            exchange_value.textContent = "";
        }
        else{

            exchange_value.textContent = (parseInt(exchange_input.value) * parseFloat(usd_get.textContent)).toFixed(2);
        }
    }
});


function valueGetSale(){
    var val = document.querySelector("#getSaleVal").value;
    console.log(val);
    if (val == "1"){
        exchange_input.oninput = (() => {
            if (exchange_value_val.selectedIndex == "0"){
                console.log(exchange_input.value);
                console.log(usd_get.textContent);
                if (exchange_input.value == "" ){
                    exchange_value.textContent = "";
                }
                else{
        
                    exchange_value.textContent = (parseInt(exchange_input.value) * parseFloat(euro_get.textContent)).toFixed(2);
                }
            }
            if (exchange_value_val.selectedIndex == "1"){
                console.log(exchange_input.value);
                console.log(usd_get.textContent);
                if (exchange_input.value == "" ){
                    exchange_value.textContent = "";
                }
                else{
        
                    exchange_value.textContent = (parseInt(exchange_input.value) * parseFloat(usd_get.textContent)).toFixed(2);
                }
            }
        });
    }

    if (val == "2"){
        exchange_input.oninput = (() => {
            if (exchange_value_val.selectedIndex == "0"){
                console.log(exchange_input.value);
                console.log(usd_get.textContent);
                if (exchange_input.value == "" ){
                    exchange_value.textContent = "";
                }
                else{
        
                    exchange_value.textContent = (parseInt(exchange_input.value) * parseFloat(euro_sale.textContent)).toFixed(2);
                }
            }
            if (exchange_value_val.selectedIndex == "1"){
                console.log(exchange_input.value);
                console.log(usd_get.textContent);
                if (exchange_input.value == "" ){
                    exchange_value.textContent = "";
                }
                else{
        
                    exchange_value.textContent = (parseInt(exchange_input.value) * parseFloat(usd_sale.textContent)).toFixed(2);
                }
            }
        });
    }
}


