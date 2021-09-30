function get(object, key, default_value) {
  var result = object[key];
  return (typeof result !== "undefined") ? result : default_value;
}

async function miFetch(url,meta) {
  const element_csrf = document.querySelector("[data-csrf]")
  const csrf = element_csrf.getAttribute("data-csrf")
  if(meta.method.toUpperCase() !== "GET"){
    get(meta,"headers",csrf);
  }
  const response = await fetch(url,meta);
  const data = await response.json();
  element_csrf.setAttribute("data-csrf",data.csrf)
  return data
}
export default miFetch