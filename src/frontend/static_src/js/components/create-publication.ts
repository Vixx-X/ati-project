console.log("Hola mundo nenes desde create publication");

const handleFiles = function(event){
    let reader = new FileReader();
    let file = event.target.files[0]

    reader.onloadend  = function(){
        let preview = document.getElementById('preview');
        let new_Div = document.createElement("div")
            new_Div.setAttribute("class","create-publication-body-input-label")
        let new_img = document.createElement("img")
        new_img.src = reader.result
        new_Div.appendChild(new_img)
        preview.appendChild(new_Div)
    };

    reader.readAsDataURL(file)
}
let input_file = document.getElementById("file").addEventListener("change",handleFiles)