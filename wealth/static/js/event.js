let leftNavbar = document.querySelector('#leftNavbar');
let showNavList = document.querySelector('#showNavList');
showNavList.addEventListener('click', () => {
    leftNavbar.style.display = 'block';
})
let hideNavbar = document.querySelector('#hideNavbar');
hideNavbar.addEventListener('click', () => {
    leftNavbar.style.display = 'none';
})

