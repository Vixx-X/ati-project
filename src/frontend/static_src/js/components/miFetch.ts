function miFetch(...args) {
  return fetch(...args);
}
function handleClick() {
  console.log(miFetch("localhost:9021/api/post"));
}

document.getElementById("boton_edu")?.addEventListener("click", handleClick);
