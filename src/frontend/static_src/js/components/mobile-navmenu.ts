console.log("Hola mundo desde maobile")
function showDetails() {
    document.getElementById("details").setAttribute("class", "active-content");
    document.getElementById("tab-details").setAttribute("class", "active-tab");
    document.getElementById("publication").setAttribute("class", "");
    document.getElementById("tab-publication").setAttribute("class", "");
    console.log('hola')
}

function showPublication() {
    document.getElementById("publication").setAttribute("class", "active-content");
    document.getElementById("tab-publication").setAttribute("class", "active-tab");
    document.getElementById("details").setAttribute("class", "");
    document.getElementById("tab-details").setAttribute("class", "");
}

document.getElementById("buttonDetails").addEventListener("click", showDetails);
document.getElementById("buttonPublication").addEventListener("click", showPublication);