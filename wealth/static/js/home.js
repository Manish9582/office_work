let calculators_Mein=document.querySelector('#calculators_Mein');
console.log(calculators_Mein)
 let flag=0;
const showtoggalCal=()=>{
    if(flag==0){
        document.querySelector('#calculatorsDatas').classList.remove('hidden');
        flag=1;
    }
    else{
        document.querySelector('#calculatorsDatas').classList.add('hidden');
        flag=0;
    }
}