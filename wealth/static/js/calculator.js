const calculatorsDatas = document.querySelector('#calculatorsDatas');
let flag = 1;
function showtoggalCal() {
    if (flag == 1) {
        calculatorsDatas.style.display = 'block';
        flag = 0;
    } else {
        calculatorsDatas.style.display = 'none';
        flag = 1;
    }
}

function toggleCalculator(calculatorId) {
    var calculator = document.getElementById(calculatorId);
    if (calculator.style.display === "none") {
        calculator.style.display = "block";
    } else {
        calculator.style.display = "none";

    }
}


