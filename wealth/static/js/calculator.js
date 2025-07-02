const calculatorsDatas = document.querySelector('#calculatorsDatas');
function showtoggalCal() {
    let flag = 1;
    if (flag == 1) {
        calculatorsDatas.style.display = 'block';
        flag = 0;
    } else {
        calculatorsDatas.style.display = 'none';
    }
}

function toggleCalculator(calculatorId) {
    var calculator = document.getElementById(calculatorId);
    if (calculator.style.display === "none") {
        calculator.style.display = "block";
    } else {
        calculator.style.display = "none";
        console.log("Hellow")
    }
}


