
/*-----------------------------------------------
|         SCROLL ANIMATIONS   ORIGINAL           |
------------------------------------------------*/


const van = document.querySelector('.overlay-van')
const vanContainer = document.querySelector('.van-container')

const observer = new IntersectionObserver((entries)=> {
    entries.forEach((entry) => {
        console.log(entry)
        if (entry.isIntersecting) {
            entry.target.classList.add('show'),
            entry.target.classList.add('move');
        } else {
            entry.target.classList.remove('show');
            
        }
    });
});


const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el));







