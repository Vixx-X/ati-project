const inputProfile = document.querySelector("#file-upload-profile");
const imageProfile = document.querySelector(".user-icon img");
inputProfile?.addEventListener("change", (e) => {
  const reader = new FileReader();
  const selectedFile = e.target.files[0];
  reader.onload = function (event) {
    imageProfile.setAttribute("src", event.target.result.toString());
  };
  reader.readAsDataURL(selectedFile);
});

const inputBanner = document.querySelector("#file-upload-baner");
const imageBanner = document.querySelector(".section-header");
inputBanner?.addEventListener("change", (e) => {
  const reader = new FileReader();
  const selectedFile = e.target.files[0];
  reader.onload = function (event) {
    imageBanner.setAttribute(
      "style",
      `--bg-image: url(${event.target.result.toString()})`
    );
  };
  reader.readAsDataURL(selectedFile);
});

// const inputMedia = document.querySelector('#file-upload-image-publication');
// const publicationUpload = document.querySelector('.create-publication-body-input-label');
// const oldChild = publicationUpload.firstElementChild;
// const newImage = document.createElement('IMG');

// inputMedia.addEventListener('change', (e) => {
//     console.log(publicationUpload);
//     console.log(oldChild);
//     const reader = new FileReader();
//     const selectedFile = e.target.files[0]
//     reader.onload = function (event) {
//       newImage.setAttribute(
//         "src",
//         event.target.result.toString()
//       );
//       newImage.classList.add('image-size');
//       publicationUpload.replaceChild(newImage, oldChild)
//     };
//     reader.readAsDataURL(selectedFile);
// })
