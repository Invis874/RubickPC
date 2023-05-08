const open_model = document.getElementById('btn');
const close = document.getElementById('close');
const modal = document.getElementById('modal-okno');

const open_model_1 = document.getElementById('btn-1');
const close_1 = document.getElementById('close-1');
const modal_1 = document.getElementById('modal-okno-1');

const open_model_2 = document.getElementById('btn-2');
const close_2 = document.getElementById('close-2');
const modal_2 = document.getElementById('modal-okno-2');

open_model_2.addEventListener('click', function(){
    modal_2.classList.add('active');
})

close_2.addEventListener('click', ()=>{
    modal_2.classList.remove('active');
})


open_model_1.addEventListener('click', function(){
    modal_1.classList.add('active');
})

close_1.addEventListener('click', ()=>{
    modal_1.classList.remove('active');
})

open_model.addEventListener('click', function(){
    modal.classList.add('active');
})

close.addEventListener('click', ()=>{
    modal.classList.remove('active');
})
