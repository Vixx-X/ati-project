document.addEventListener('DOMContentLoaded', deleteDetails);
const more = document.querySelectorAll('.morecontent');

more.forEach(input => {
    input.addEventListener('click', (e) => {
        const newInput = document.querySelector('.input-description');
        const longCard = e.target.parentElement.previousElementSibling;
        if(longCard.childElementCount < 4) {
            const clon = newInput.content.cloneNode(true);
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