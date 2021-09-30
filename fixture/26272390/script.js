document.getElementById("saludo").innerHTML = config.saludo + perfil.nombre;
document.getElementById("sitio").innerHTML = config.sitio[0] + "<small>" + config.sitio[1] + "</small>" + config.sitio[2]
document.getElementById("inicio").innerHTML = config.home;
document.getElementById("nombre").innerHTML = perfil.nombre;
document.getElementById("descripcion").innerHTML = perfil.descripcion;
document.getElementById("column1").innerHTML = config.color + "<br/>" + config.libro + "<br/>" + config.musica + "<br/>" + config.video_juego + "<br/>";
document.getElementById("column2").innerHTML = perfil.color + "<br/>" + perfil.libro + "<br/>" + perfil.musica + "<br/>" + perfil.video_juego + "<br/>";
document.getElementById("lenguajes").innerHTML = config.lenguajes;
document.getElementById("mis_lenguajes").innerHTML = perfil.lenguajes;
document.getElementById("contacto").innerHTML = config.email.replace("[email]",  "<a href=\"mailto:danielvieiucv@gmail.com\"> "+ perfil.email + "</a>");
document.getElementById("footer").innerHTML = config.copyRight;
document.getElementById("imagen").setAttribute("src",  perfil.imagen);