const openList = document.querySelector('.openList');
openList.addEventListener('click', openLeftMenu);

const closeList = document.querySelector('.closeList');
openList.addEventListener('click', openLeftMenu);
closeList.addEventListener('click', closeLeftMenu);

function openLeftMenu() {
    document.getElementById("leftMenu").style.display = "block";
    // document.getElementById("leftMenu").classList.add('sidebar-left-nav');
}

function closeLeftMenu() {
    document.getElementById("leftMenu").style.display = "none";
}