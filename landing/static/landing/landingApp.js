
/* ALL ELEMENTS
----------------------------------------------  */
const navbar = document.querySelector('.navbar-container');
const hamburger = document.querySelector('.hamburger-container');
const links = document.querySelector('.navbar-list');
const login = document.querySelector('.login-btn');

const menu = document.querySelector('.menu');
console.log(menu);




/* HIDE/SHOW  NAVBAR HAMBURGER
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

/* add eventListener  (BUG:is not triggered when reloaded!) */
window.addEventListener("resize", function() {
  /* get width of the window */
  width = window.innerWidth;
  if (width < hamburgerPoint) {
    showHamburger();
  } else {
    hideHamburger();
  }
});

/* add eventListener for reloading */
window.addEventListener("load", function() {
  width = window.innerWidth;
  if (width < hamburgerPoint) {
    showHamburger();
  } else {
    hideHamburger();
  }
});





/* COLLAPSE MENU FROM HAMBURGER ON CLICK
----------------------------------------------  */
  
function openMenu() {
  if (menu.style.display === 'flex') {
    menu.style.display = 'none';
  } else {
    menu.style.display = 'flex';
  }
}; 


hamburger.addEventListener('onclick', function() {
  openMenu();
});   




/* HIDE OFF-CANVAS WHEN BIGGER SIZE 
-----------------------------------------------*/

window.addEventListener("resize", function() {
  width = window.innerWidth;
  console.log("width: " + width);
  if (width > hamburgerPoint) {
    menu.style.display = 'none';
  }
});

/* add eventListener  (BUG:is not triggered when reloaded!) */
window.addEventListener("resize", (e) =>{
  width = window.innerWidth;
  if (width > hamburgerPoint) {
    
  }
});


/* Function to close the Offcanvas when the button is clicked 
-----------------------------------------------------------------*/
main = document.querySelector('#main');
header = document.querySelector('.header');

function closeOffcanvas() {
  menu.style.display = 'none';
}

main.addEventListener('click', function() {
  closeOffcanvas();
});
