// document.addEventListener('DOMContentLoaded', startApp);

// function startApp(){
//     removeElement();
//     addElement();
// }

// function removeElement(){
//     const friendsRemove = document.querySelectorAll('.button.delete');
//     friendsRemove.forEach(element => {
//         element.addEventListener('click', () => {
//             element.classList.remove('delete');
//             element.classList.add('addfriend');
//             element.textContent = 'Be friend';
//             addElement();
//         });
//     });
// }

// function addElement(){
//     const friendsAdd = document.querySelectorAll('.button.addfriend');
//     friendsAdd.forEach(element => {
//         element.addEventListener('click', () => {
//             element.classList.remove('addfriend');
//             element.classList.add('delete');
//             element.textContent = 'Delete';
//             removeElement();
//         });
//     });
// }
import miFetch from "./miFetch"

async function RemoveElement(element:any){
    const url = element.target.getAttribute("data-url");
    const meta = {
        method: 'DELETE',
    }
    const data = await miFetch(url,meta)
    alert(data)
};
async function AddElement(element:any){
    const url = element.target.getAttribute("data-url");
    const meta = {
        method: 'POST',
    }
    const data = await miFetch(url,meta)
    alert(data)
};

const buttonActionElementFriendList = document.querySelectorAll("[data-ButtonActionFriendList]");
for(const element of buttonActionElementFriendList){
    if(element.getAttribute("data-action")=="Add"){
        element.addEventListener("click",AddElement)
    }
    if(element.getAttribute("data-action")=="Delete"){
        element.addEventListener("click",RemoveElement)
    }
}