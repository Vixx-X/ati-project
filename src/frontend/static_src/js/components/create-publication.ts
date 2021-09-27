// function getExtension(filename: any) {
//   var parts = filename.split("/");
//   console.log(parts[parts.length - 1]);
//   return parts[parts.length - 1];
// }

// function isImage(filename: any) {
//   var ext = getExtension(filename);
//   switch (ext.toLowerCase()) {
//     case "jpg":
//     case "gif":
//     case "png":
//     case "jpeg":
//       //etc
//       return true;
//   }
//   return false;
// }

// function isVideo(filename: any) {
//   var ext = getExtension(filename);
//   switch (ext.toLowerCase()) {
//     case "mkv":
//     case "avi":
//     case "mp4":
//       // etc
//       return true;
//   }
//   return false;
// }

// function isAudio(filename: any) {
//   var ext = getExtension(filename);
//   switch (ext.toLowerCase()) {
//     case "mp3":
//       // etc
//       return true;
//   }
//   return false;
// }

// // if (window.File && window.FileList && window.FileReader) {

// //     var files = event.target.files; //FileList object
// //     var output = document.getElementById("result");

// //     for (var i = 0; i < files.length; i++) {
// //         var file = files[i];
// //         //Only pics
// //         if (!file.type.match('image')) continue;

// //         var picReader = new FileReader();
// //         picReader.addEventListener("load", function (event) {
// //             var picFile = event.target;
// //             var div = document.createElement("div");
// //             div.innerHTML = "<img class='thumbnail' src='" + picFile.result + "'" + "title='" + file.name + "'/>";
// //             output.insertBefore(div, null);
// //         });
// //         //Read the image
// //         picReader.readAsDataURL(file);
// //     }
// // } else {
// //     console.log("Your browser does not support File API");
// // }

// const handleFiles = function (event) {

//     if (window.File && window.FileList && window.FileReader) {

//         var files = event.target.files; //FileList object
//         var output = document.querySelector(".splide__list");

//         for (var i = 0; i < files.length; i++) {
            
//             var file = files[i];
//             console.log("Filename: " + file.name);
//             console.log("Type: " + file.type);
//             console.log("Size: " + file.size + " bytes");
//             var div = document.createElement("LI");
//             console.log('epa');
//             div.classList.add("create-publication-body-input-label");
//             div.classList.add("splide__slide");
//             div.classList.add("black");
//             let new_file;
//             if (file.type.match('image')) {
//                 new_file = document.createElement("img");
//             } else if (file.type.match('video')) {
//                 console.log('Videito')
//                 new_file = document.createElement("video");
//                 new_file.setAttribute("controls", true);
//             } else {
//                 new_file = document.createElement("audio");
//                 new_file.setAttribute("controls", true);
//             }
//             new_file.src = URL.createObjectURL(file)
//             new_file.classList.add("image-size");
//             div.appendChild(new_file)
//             output.appendChild(div);
            
//         }

//     } else {
//         console.log("Your browser does not support File API");
//     }
// }


// const inputFile = document.getElementById("file-upload-image-publication");
// inputFile?.addEventListener("change", handleFiles, false);
