// Main elements for mouse movement animation 
const card = document.querySelector('.card');
const container = document.querySelector('.container');


// Items to popout or animate on the moving card
const title = document.querySelector('.title');
const circle = document.querySelector('.circle');
const heatpump = document.querySelector('.heatpump img');
const purchase = document.querySelector('.purchase button');
const info = document.querySelector('.info h3');
const sizes = document.querySelector('.sizes');





         /* Moving animation event and add an event (e) to the function

            making a variable xAxis, storing inside the whole innerWidth of the window
            and dividing it by 2 to get the center of the window.

            making a variable yAxis, storing inside the whole innerHeight of the window
            and dividing it by 2 to get the center of the window.

            minus the e.pageX to get the center of the card
            minus the e.pageY to get the center of the card

            The effect is to strong so we divide the wrapped math (window.innerWidth / 2 - e.pageX) by 25 or less. (the less it's divided by the more the effect is strong) */


container.addEventListener('mousemove', (e) => {
    /* console.log(e.pageX, e.pageY); */
    let xAxis = (window.innerWidth / 2 - e.pageX) / 25;
    let yAxis = (window.innerHeight / 2 - e.pageY) / 25;
    card.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
});

        /* It looks  weird so we need to add a transform-style: preserve-3d to the   card class in the css file */




         /* When we leave the card we want to animate it back to the center
            Normaly we would do this with transition: ease 0.3s; in css but it's not working because it's apllied all the time because of the mousemove event and we want it to be applied only when we leave the card



            So we basically gona add an event listener and put the transition to the container class when we enter to "NONE" and add it when we leave the container.
            So we leave, animate it, when we enter, not animate it. */



// ANIMATIONS when IN and OUT
//Animation in
container.addEventListener('mouseenter', (e) => {
    // For transition ease-out when entering container
    card.style.transition = 'none';
    // Popout when entering
    heatpump.style.transform = 'translateZ(150px) rotatex(0deg)';
    title.style.transform = 'translateZ(120px)';
    info.style.transform = 'translateZ(140px)';
    sizes.style.transform = 'translateZ(120px)';
    purchase.style.transform = 'translateZ(100px)';
});

// Animate Out
container.addEventListener('mouseleave', (e) => {
    // For transition ease-out when leaving the container
    card.style.transform = `rotateY(0deg) rotateX(0deg)`;
    card.style.transition = 'ease 0.5s';

    // Popback when leaving
    heatpump.style.transform = 'translateZ(0px)';
    title.style.transform = 'translateZ(0px)';
    info.style.transform = 'translateZ(0px)';
    sizes.style.transform = 'translateZ(0px)';
    purchase.style.transform = 'translateZ(0px)';
});



// Button active animation
const buttons = document.querySelector('.sizes button');
const sizeButton1 = document.querySelector('.btn-1');
const sizeButton2 = document.querySelector('.btn-2');
const sizeButton3 = document.querySelector('.btn-3');

console.log(sizeButton1, sizeButton2, sizeButton3);



// add/remove  class with added event
// Button 1
sizeButton1.addEventListener('mouseover', (e) => {
    sizeButton1.classList.add('active');
});
sizeButton1.addEventListener('mouseout', (e) => {
    sizeButton1.classList.remove('active');
});

// Button 2
sizeButton2.addEventListener('mouseover', (e) => {
    sizeButton2.classList.add('active');
});
sizeButton2.addEventListener('mouseout', (e) => {
    sizeButton2.classList.remove('active');
});

// Button 3
sizeButton3.addEventListener('mouseover', (e) => {
    sizeButton3.classList.add('active');
});
sizeButton3.addEventListener('mouseout', (e) => {
    sizeButton3.classList.remove('active');
});
