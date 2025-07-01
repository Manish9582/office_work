// Toggle visibility of the main calculators container
const calculatorsDatas = document.querySelector('#calculatorsDatas');
function showtoggalCal() {
    let flag = 1;
    if (flag == 1) {
        calculatorsDatas.style.display === 'block';
        flag = 0;
    } else {
        calculatorsDatas.style.display === 'none';
    }
}
function toggleCalculator(calculatorId) {
    const calculator = document.getElementById(calculatorId);
    console.log(calculator)
    // calculator.style.display === 'block' ? 'none' : 'block';
}
