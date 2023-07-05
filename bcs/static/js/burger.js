let menuToggle = document.getElementById('menuToggle');
let header = document.querySelector('header');

menuToggle.onclick = function() {
    header.classList.toggle('active')
}