// let divPapaSearch = document.getElementsByClassName("search-main-container")[0]
// let inputSearch = divPapaSearch.getElementsByTagName("input")[0]
// let output = document.getElementsByClassName("container-friends")[0]
// let parraNumber = document.getElementsByClassName("number")[0]

// const ArrayProfile = [
//     {name:"Vittorio",
//     img:""},
//     {name:"Eduardo",
//     img:""},
//     {name:"Daniel",
//     img:""},
//     {name:"Gabriela",
//     img:""},
//     {name:"Pepe",
//     img:""},
//     {name:"Jualian",
//     img:""}
// ]

// function filter(){
//     let texto_b = inputSearch.value.toLowerCase()
//     output.innerHTML = ""
//     parraNumber.textContent= ""
//     let num = 0
//     for (let elemento of ArrayProfile) {
//         let nombre = elemento.name.toLowerCase()
//         if (nombre.indexOf(texto_b) !== -1) {
//             num += 1
//             output.innerHTML += `
//             <div class="cont-element-friend-list ">
//                 <div class="user-icon basic">
//                     <a href="/user/2/">
//                         <picture>
//                             <source srcset="/static/img/users/26838989.webp" type="image/webp">
//                             <source srcset="/static/img/users/26838989.png" type="image/png">
//                             <img loading="lazy" src="/static/img/users/26838989.png" alt="">
//                         </picture>
//                     </a>
//             </div>
//             <div class="cont-element-friend-list-description">
//                 <p class="element_friend_list_user">${elemento.name}</p>
//                 <p class="element_friend_list_commun_friends">35</p>
//             </div>
//             <div class="cont-element-friend-button">
//                 <button class="button primary text-uppercase fw-bold">
//                     Be Friends
//                 </button>
//             </div>
//             </div>`
//         }
//     }
//     console.log(num)
//     parraNumber.textContent= num.toString();
// }
    
// inputSearch.addEventListener("keyup",filter)
// filter()
const initSearch =  (element:any) => {
    const term = element.dataset.term;
    const url = element.dataset.url;
    const input = element.dataset.input;
    const inputElement = document.querySelector(input);
    inputElement?.addEventListener("input",(()=>{
        const value = inputElement.value;
        element.setAttribute("href",`${url}?${term}=${value}`)
    }))
}


const dataSearch = document.querySelectorAll("[data-search]");
for(const element of dataSearch){
    initSearch(element);
}