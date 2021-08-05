console.log("Hola mundo nenes desde create publication");

const handleFiles = function(event){
    let reader = new FileReader();
    reader.onload = function(){
        let preview = document.getElementById('preview');
        let new_Div = document.createElement("div")
        new_Div.setAttribute("class","create-publication-body-input-label")
        let new_img = document.createElement("img")
        console.log(reader.result[0])
        new_img.src = reader.result[0]
        new_img.setAttribute("style","width:150px;");
        new_Div.appendChild(new_img)
        preview.appendChild(new_Div)
    };
    reader.readAsDataURL(event.target.files[0])
}
let input_file = document.getElementById("file").addEventListener("change",handleFiles)