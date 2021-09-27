document.addEventListener('DOMContentLoaded', deleteDetails);
const more = document.querySelectorAll('.morecontent');
more.forEach(input => {
    input.addEventListener('click', (e) => {
        e.preventDefault();
        const longCard = e.target.parentElement.previousElementSibling;
        const number = longCard.childElementCount;
        const tag = longCard.parentElement.firstChild.getAttribute('for');
        if(number < 4) {
            const newId = `${tag}-${number + 1}`
            const htmlString = `<input id="${newId}" name="${newId}" type="text" value=""><button type="button"><img id="element${number + 1}" class="delete-content" loading="lazy" src="/static/img/icons/delete.svg" alt="Delete detail"></button> <label class="d-none" for="${newId}">Favorite ${tag}</label>`
            const clon = document.createElement('DIV');
            clon.classList.add('input-content');
            clon.innerHTML = htmlString;
            longCard.appendChild(clon);
            deleteDetails();
        }
    })
});

function deleteDetails(){
    const deleteInput = document.querySelectorAll('.delete-content');
    deleteInput.forEach(deleteElement => {
        deleteElement.addEventListener('click', (e) => {
            const inputRemove = e.target.parentElement.parentElement;
            inputRemove.remove();
        })
    });
}

// const newInput = document.createElement('');document.createElement()