document.addEventListener('DOMContentLoaded', startApp);

function startApp(){
    removeElement();
    addElement();
}

function removeElement(){
    const friendsRemove = document.querySelectorAll('.button.delete');
    friendsRemove.forEach(element => {
        element.addEventListener('click', () => {
            element.classList.remove('delete');
            element.classList.add('addfriend');
            element.textContent = 'Be friend';
            addElement();
        });
    });
}

function addElement(){
    const friendsAdd = document.querySelectorAll('.button.addfriend');
    friendsAdd.forEach(element => {
        element.addEventListener('click', () => {
            element.classList.remove('addfriend');
            element.classList.add('delete');
            element.textContent = 'Delete';
            removeElement();
        });
    });
}