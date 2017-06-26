<h1>Proyecto Desarrollo Web<h1>
 
<h2>Página “Ruta del Vino”<h2>
<h2>Hugo Riquelme, Carlos Fuentes, Javier Lau”<h2>
<h3>Introducción<h3>

Ruta del vino es una empresa chilena que proporciona servicios de tour por el Valle de Colchagua, en el que se ofrecen paseos guiados por sus viñas, lugares de fabricación, sitios de interés y terrenos cercanos. Esta empresa no solo ofrece tours guiados, también cuenta con servicio de comida y alojamiento para poder relajarse unos días en el valle.
<h3>Nuestro proyecto<h3>

Construiremos la página “www.LaRutaDelVino.cl” utilizando las herramientas de Django y Vagrant para poder realizar el backend de la página, y para el frontend, utilizaremos HTML5, Bootstrap, CSS3 y Jquery para diseñar la vista de la página.

La página web cuenta con un sistema de registro de usuarios, en donde los clientes deberán registrarse para poder utilizar los servicios, posee un catálogo y un carro de compra para que el cliente pueda seleccionar varios productos y pagarlos todos de una vez. Se cuenta con varias secciones para categorizar los productos, además de accesos a rápidos a teléfonos y correos de contacto. También se cuenta con un usuario administrador, quien manejara los datos y funcionalidades de la página.

<h3>instrucciones de instralación</h3>

descargue o clone el archivo almacenado en github, una dez descargado, coloque los archivos descargados dentro de una carpeta de proyecto de django. si no tiene una carpeta con un proyecto iniciado, puede dirigirse a <a href="https://github.com/mcantillana/unab_install_django/blob/master/README.md">https://github.com/mcantillana/unab_install_django/blob/master/README.md</a> para realizar la instalacion adecuadamente.

una vez dentro del proyecto, abrimos nuestro entorno virtual de vagrant, con el comando "vagrant ssh". una vez listo, nos dirigiremos a la carpeta donde se aloja nuestro proyecto en el entorno virtual e iniciamos el servidor con el comando "python manage.py runserver 0.0.0.0:8080"(RECORDAR LEER EL ARCHIVO REQUERIMENTS.TXT para instalar todas las aplicaciones necesarias, caso contrario no correra el servidor).

se iniciara nuestro servidor y nos dirigiremos a nuestra pagina web, en el localhost 127.0.0.1:8080.

la pagina contiene funcionalidades hechas completamente en django, ademas de poseer la adaptación correcta del framework bootstrap. tenemos un super usuario, el cual podra agregar panoramas. cada panorama se reflejará en la vista principal Indexview, en el caso de la template, nos referiremos a ella como "index.html". cuando damos click a alguno de estos panoramas, la pagina nos mostrará la vista con el template detalle.html, el cual nos indicará el detalle de nuestro panorama, su contenido, y precio. cada template esta adecuado a las funciones que nos entrega django, como la carga de nuestros archivos static y nuestras imagenes, ademas de poseer herencia de paginas gracias a los bloques y archivos de carga para extender nuestro template principal y ahorrar una gran cantidad de lineas de codigo.


