import Splide from "@splidejs/splide";

// new Splide(".splide").mount();
const inputFile = document.getElementById("file-upload-image-publication");
const deleteFiles = document.querySelector("#delete-files");
const labelInfo = document.querySelector("#label-input");

const handleFiles = function (event) {
  if (window.File && window.FileList && window.FileReader) {
    labelInfo.classList.add("dissable");
    console.log(labelInfo);
    deleteFiles.classList.remove("dissable");
    deleteFiles.removeAttribute("disabled");
    console.log(deleteFiles);
    var files = event.target.files; //FileList object
    var output = document.querySelector(".splide__list");
    const mainContainer = document.querySelector(".container-styles");
    const splideAppear = document.querySelector("#splide-element");
    const dup = splideAppear.content.firstElementChild.cloneNode(true);
    const previewImage = document.querySelector(".container-upload-data");
    console.log(previewImage);

    mainContainer.replaceChild(dup, previewImage);
    const splide = new Splide(".splide").mount();

    for (var i = 0; i < files.length; i++) {
      var file = files[i];
      var div = document.createElement("LI");
      div.classList.add("create-publication-body-input-label");
      div.classList.add("splide__slide");
      div.classList.add("black");
      let new_file;
      if (file.type.match("image")) {
        new_file = document.createElement("img");
      } else if (file.type.match("video")) {
        new_file = document.createElement("video");
        new_file.setAttribute("controls", true);
      } else {
        new_file = document.createElement("audio");
        new_file.setAttribute("controls", true);
      }
      new_file.src = URL.createObjectURL(file);
      new_file.classList.add("image-size");
      div.appendChild(new_file);
      splide.add(div);
    }
  } else {
    console.log("Your browser does not support File API");
  }
};

deleteFiles?.addEventListener("click", (e) => {
  e.preventDefault();
  deleteFiles.setAttribute("disabled", "");
  const mainContainer = document.querySelector(".container-styles");
  const imageAppear = document.querySelector("#image-preview-element");
  const dup = imageAppear.content.firstElementChild.cloneNode(true);
  const splideElement = document.querySelector(".container-splide-data");
  mainContainer.replaceChild(dup, splideElement);
  deleteFiles.classList.add("dissable");
  labelInfo.classList.remove("dissable");
});

inputFile?.addEventListener("change", handleFiles, false);
