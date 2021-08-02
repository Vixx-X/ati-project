function redirect(e : Event) {
    e.preventDefault();
    window.location.href = "/user/search";
    // console.log(e.target.parentNode.dataset);
}
document.getElementById("button-search").addEventListener("click", redirect);