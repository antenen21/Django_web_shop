
/* ALL ELEMENTS
----------------------------------------------  */
const navbar = document.querySelector('.navbar-container');
const hamburger = document.querySelector('.hamburger-container');
const links = document.querySelector('.navbar-list');
const login = document.querySelector('.login-btn');

const menu = document.querySelector('.menu');
const main = document.querySelector('#main');
const header = document.querySelector('.header');
console.log(menu);




/* HIDE/SHOW  Hamburger Button
----------------------------------------------  */

/* break-point for show the hamburger menu */
let hamburgerPoint = 768;


/* create function */
function showHamburger() {
  hamburger.style.display = 'flex';
  links.style.display = 'none';
  login.style.display = 'none';
};

function hideHamburger() {
  hamburger.style.display = 'none';
  links.style.display = 'flex';
  login.style.display = 'flex';
};


 function showHideHamburger() {
  /* get width of the window */
  width = window.innerWidth;
  if (width < hamburgerPoint) {
    showHamburger();
  } else {
    hideHamburger();
  }
}
/* add eventListener  (BUG:is not triggered when reloaded!) */
window.addEventListener("resize", showHideHamburger);

/* add eventListener for reloading */
window.addEventListener("load", showHideHamburger);








/* Open/Close the Offcanvas Menu when the button is clicked
----------------------------------------------------------  */
  
function openMenu() {
  if (menu.style.display === 'flex') {
    menu.style.display = 'none';
  } else {
    menu.style.display = 'flex';
  }
}; 

hamburger.addEventListener('onclick', openMenu);



/* Function to close the Offcanvas when the button is clicked or the window is resized 
-------------------------------------------------------------------------------------*/

function closeOffcanvas() {
  menu.style.display = 'none';
}

main.addEventListener('click', closeOffcanvas);
window.addEventListener('resize', closeOffcanvas);


/* All Scroll animation 
------------------------------------------------------------*/
/* for pump animation */
const pump = document.querySelector('.overlay-pump')
const pumpContainer = document.querySelector('.pump-container')

/* for van animation */
const van = document.querySelector('.overlay-van')
const vanContainer = document.querySelector('.van-container')
const title = document.querySelector('.title')
console.log(title)

const observer = new IntersectionObserver((entries)=> {
    entries.forEach((entry) => {
        //console.log(entry)
        if (entry.isIntersecting) {
            entry.target.classList.add('show'),
            entry.target.classList.add('move-from-left');
            entry.target.classList.add('move-from-right');
        } else {
            entry.target.classList.remove('show');
        }
    });
});




const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el));