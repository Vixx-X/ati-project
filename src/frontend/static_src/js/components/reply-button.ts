console.log("hola desde reply")

let output = document.getElementById("input-commnets");
let setOfButtons = document.querySelectorAll(".reply-button")

setOfButtons.forEach(element =>{
    element.addEventListener("click",(e)=>{
        let name = element.getAttribute("data")
        let message = "@" + name
        output.setAttribute("value",message)
    })
})