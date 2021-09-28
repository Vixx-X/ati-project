var rad = document.querySelectorAll('input[name="personalization"]');
for (let i = 0; i < 2; i++) {
    rad[i].addEventListener('change', function() {
        if (i===1) {
            document.body.classList.add('darkmode');
            rad[0].removeAttribute("checked"); 
            rad[1].setAttribute('checked', 'checked');
        }else{
            document.body.classList.remove('darkmode');
            rad[1].removeAttribute('checked');
            rad[0].setAttribute('checked', 'checked');
        }
    });
}