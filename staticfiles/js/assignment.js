const tabs = document.querySelectorAll('.tab-btn')
const contents = document.querySelectorAll('.content')

var line = document.querySelector('.line');
line.style.width = tabs[0].offsetWidth + 'px';
line.style.left = tabs[0].offsetLeft +'px';
tabs.forEach((tab, index) => {
    tab.addEventListener('click', (e) => {
        tabs.forEach(tab => {
            tab.classList.remove('active')
        });
        tab.classList.add('active')

        var line = document.querySelector('.line');
        line.style.width = e.target.offsetWidth + 'px';
        line.style.left = e.target.offsetLeft + 'px';

        contents.forEach(content => {content.classList.remove('active')});
        contents[index].classList.add('active');
    });
});
