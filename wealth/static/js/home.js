let calculators_Mein=document.querySelector('#calculators_Mein');
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


// let showNavbar=document.querySelector('#showNavbar')
let showNavbar=document.querySelector('#showNavbarData')
let showNavbarMobile=document.querySelector('#showNavbarMobile');
showNavbar.addEventListener('click',function(){
    showNavbarMobile.style.display='block';
    })

let closeNavbarMobile=document.querySelector('#closeNavbarMobile');
closeNavbarMobile.addEventListener('click',function(){
    showNavbarMobile.style.display='none';
})