const sendC = document.querySelector('.send-message button');
sendC.addEventListener('click', sendComments);

function sendComments(){
    // Cambiar foto y nombre de acuerdo a usuario.
    const input = sendC.previousElementSibling;
    const content = input.value;
    if (content === ""){alert('El mensaje está vacio'); return;}
    const template = document.querySelector('.item.left');
    const message = template.cloneNode(true);
    const nodeContent = message.querySelector('.cont-chat p');
    nodeContent.textContent = content;
    const time = message.querySelector('.cont-chat-description p');
    var d = new Date();
    time.textContent = `${d.getHours()} : ${d.getMinutes()}`;
    document.querySelector('.list-comments').appendChild(message);
}