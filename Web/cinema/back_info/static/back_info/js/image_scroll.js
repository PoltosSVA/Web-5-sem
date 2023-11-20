const questionLeft = document.querySelector('#question_left');
const questionRight = document.querySelector('#question_right');
const text = document.querySelector('#text');
const question_central = document.querySelector('#question_central');

window.addEventListener('scroll',()=>{
    let value = scrollY;
    questionLeft.style.left = `-${value/0.7}px`
    questionRight.style.left = `${value/0.7}px`
    text.style.bottom = `-${value}px`;
    question_central.style.height = `${window.innerHeight - value}px`
})

