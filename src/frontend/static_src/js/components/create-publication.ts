function getExtension(filename: any) {
  var parts = filename.split("/");
  console.log(parts[parts.length - 1]);
  return parts[parts.length - 1];
}

function isImage(filename: any) {
  var ext = getExtension(filename);
  switch (ext.toLowerCase()) {
    case "jpg":
    case "gif":
    case "png":
    case "jpeg":
      //etc
      return true;
  }
  return false;
}

function isVideo(filename: any) {
  var ext = getExtension(filename);
  switch (ext.toLowerCase()) {
    case "mkv":
    case "avi":
    case "mp4":
      // etc
      return true;
  }
  return false;
}

function isAudio(filename: any) {
  var ext = getExtension(filename);
  switch (ext.toLowerCase()) {
    case "mp3":
      // etc
      return true;
  }
  return false;
}

const handleFiles = function (event) {
  let reader = new FileReader();
  var files = event.target.files;
  for (var i = 0; i < files.length; i++) {
    console.log("Filename: " + files[i].name);
    console.log("Type: " + files[i].type);
    console.log("Size: " + files[i].size + " bytes");
    if (
      !isImage(files[i].type) &&
      !isVideo(files[i].type) &&
      !isAudio(files[i].type)
    ) {
      alert("Invalid Format");
      return;
    }
  }
  if (isImage(files[0].type)) {
    console.log("Imagen sad");
    reader.onloadend = function () {
      let preview = document.querySelector(
        ".cont-create-publication-body-input-label"
      );
      let new_Div = document.createElement("div");
      new_Div.setAttribute("class", "create-publication-body-input-label");
      let new_img = document.createElement("img");
      new_img.src = reader.result;
      new_img.classList.add("image-size");
      new_Div.appendChild(new_img);
      preview.appendChild(new_Div);
    };
    reader.readAsDataURL(files[0]);
  } else if (isVideo(files[0].type)) {
    console.log("Videoooo");
    reader.onloadend = function () {
      let preview = document.querySelector(
        ".cont-create-publication-body-input-label"
      );
      let new_Div = document.createElement("div");
      new_Div.setAttribute("class", "create-publication-body-input-label");
      let new_vid = document.createElement("video");
      new_vid.src = reader.result;
      new_vid.autoplay = false;
      new_vid.classList.add("image-size");
      new_Div.appendChild(new_vid);
      preview.appendChild(new_Div);
    };
    reader.readAsDataURL(files[0]);
  }
};

let input_file = document
  .getElementById("file-upload-image-publication")
  ?.addEventListener("change", handleFiles);
