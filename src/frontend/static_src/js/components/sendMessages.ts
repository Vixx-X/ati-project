const send = document.querySelector('.send-message button');
const listChats = document.querySelectorAll('.cont-listaAmigos .cont-element-friend-list');
const actual = document.querySelector('.cont-listaAmigos .cont-element-friend-list')

actual.classList.add('pressed');
const content = actual.querySelector('.element_friend_list_user');
console.log(content.textContent);
const changeChat = document.querySelector('.main-chat');
const changeName = changeChat.querySelector('.element_friend_list_user');
changeName.textContent = content.textContent;


send.addEventListener('click', sendMessage);

function sendMessage(){
    const input = send.previousElementSibling;
    const content = input.value;
    if (content === ""){alert('El mensaje está vacio'); return;}
    const template = document.querySelector('.chat.reply');
    const message = template.cloneNode(true);
    const nodeContent = message.querySelector('.cont-chat p');
    nodeContent.textContent = content;
    const time = message.querySelector('.cont-chat-description p');
    var d = new Date();
    time.textContent = `${d.getHours()} : ${d.getMinutes()}`;
    document.querySelector('.messages').appendChild(message);
}

listChats.forEach(elementChat => {
    elementChat.addEventListener('click', () => {
        const prevChat = document.querySelector('.pressed');
        prevChat.classList.remove('pressed');
        elementChat.classList.add('pressed');
        const content = elementChat.querySelector('.element_friend_list_user');
        console.log(content.textContent);
        const changeChat = document.querySelector('.main-chat');
        const changeName = changeChat.querySelector('.element_friend_list_user');
        changeName.textContent = content.textContent;
    });
});