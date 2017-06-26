<h1>Proyecto Desarrollo Web<h1>
 
<h2>P�gina �Ruta del Vino�<h2>

<h3>Introducci�n<h3>

Ruta del vino es una empresa chilena que proporciona servicios de tour por el Valle de Colchagua, en el que se ofrecen paseos guiados por sus vi�as, lugares de fabricaci�n, sitios de inter�s y terrenos cercanos. Esta empresa no solo ofrece tours guiados, tambi�n cuenta con servicio de comida y alojamiento para poder relajarse unos d�as en el valle.
<h3>Nuestro proyecto<h3>

Construiremos la p�gina �www.LaRutaDelVino.cl� utilizando las herramientas de Django y Vagrant para poder realizar el backend de la p�gina, y para el frontend, utilizaremos HTML5, Bootstrap, CSS3 y Jquery para dise�ar la vista de la p�gina.

La p�gina web cuenta con un sistema de registro de usuarios, en donde los clientes deber�n registrarse para poder utilizar los servicios, posee un cat�logo y un carro de compra para que el cliente pueda seleccionar varios productos y pagarlos todos de una vez. Se cuenta con varias secciones para categorizar los productos, adem�s de accesos a r�pidos a tel�fonos y correos de contacto. Tambi�n se cuenta con un usuario administrador, quien manejara los datos y funcionalidades de la p�gina.

<h3>instrucciones de instralaci�n</h3>

descargue o clone el archivo almacenado en github, una dez descargado, coloque los archivos descargados dentro de una carpeta de proyecto de django. si no tiene una carpeta con un proyecto iniciado, puede dirigirse a <a href="https://github.com/mcantillana/unab_install_django/blob/master/README.md">https://github.com/mcantillana/unab_install_django/blob/master/README.md</a> para realizar la instalacion adecuadamente.

una vez dentro del proyecto, abrimos nuestro entorno virtual de vagrant, con el comando "vagrant ssh". una vez listo, nos dirigiremos a la carpeta donde se aloja nuestro proyecto en el entorno virtual e iniciamos el servidor con el comando "python manage.py runserver 0.0.0.0:8080".

se iniciara nuestro servidor y nos dirigiremos a nuestra pagina web, en el localhost 127.0.0.1:8080.

la pagina contiene funcionalidades hechas completamente en django, ademas de poseer la adaptaci�n correcta del framework bootstrap. tenemos un super usuario, el cual podra agregar panoramas. cada panorama se reflejar� en la vista principal Indexview, en el caso de la template, nos referiremos a ella como "index.html". cuando damos click a alguno de estos panoramas, la pagina nos mostrar� la vista con el template detalle.html, el cual nos indicar� el detalle de nuestro panorama, su contenido, y precio. cada template esta adecuado a las funciones que nos entrega django, como la carga de nuestros archivos static y nuestras imagenes, ademas de poseer herencia de paginas gracias a los bloques y archivos de carga para extender nuestro template principal y ahorrar una gran cantidad de lineas de codigo.


