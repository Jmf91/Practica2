Práctica 2: Aislamiento de una aplicación web usando jaulas.
===========================

En esta práctica, voy a aislar una pequeña aplicacion web basada en python en una jaula. Usaré el sistema operativo
ubuntu 12.10 "(quantal quetzal), con una arquitectura de 32 bits.

Creación de la jaula.
========================

Para crear la jaula recurrimos a la herramienta debootstrap, que permite enjaular un SO Debian (Ubuntu, Guadalinex, Debian) a 
través del siguiente comando:  "sudo debootstrap --arch=i386 quantal /home/jaulas/quantal/ http://archive.ubuntu.com/ubuntu". 
Como se puede observar, --arch=i386 indica que se va a instalar la jaula en 32 bits y que se instalará en la carpeta 
arriba mencionada.

![im1](https://dl.dropbox.com/s/zogv6ainvzro6nw/p1.png)

Configuración de la jaula.
=============================================
Posteriormente ejecutamos la jaula con la orden "sudo chroot /home/jaulas/quantal" y procedemos a configurar el sistema
a nuestro gusto. 

![im4](https://dl.dropbox.com/s/ghxg54rfwbuyhv3/p4.png)

  - Montamos el directorio /proc y cambiamos el idioma a español.
  
![im1](https://dl.dropbox.com/s/2wm0ohepa2o9odn/p3.png)

  - Instalamos librerias que vamos a necesitar a continuación, tal como python, o webpy.

![im1](https://dl.dropbox.com/s/4ytqaqvwzl5r2rl/p2.png)

Para instalar webpy, necesitamos descargarla de los repositorios de github. Para ello debemos instalar la aplicacion git
y acceder a la libreria webpy a través de ésta. Para ello usamos los siguientes comandos:
   - "sudo apt-get install git"
   - "git clone git://github.com/webpy/webpy.git"
   - En el directorio /webpy: "python setup.py install"
  
Ya tenemos instalada la libreria webpy.

Lanzar aplicación web.
======================================================

Una vez que tenemos todo preparado, escribimos en el editor de texto "vi" la aplicación web python que vamos a ejecutar 
en la jaula. Vamos a programar un simple hola mundo, tal como se muestra en esta imagen:

![im6](https://dl.dropbox.com/s/64k7mr6doli6yhu/p6.png)


Después de escribirla, guardamos con los comandos :wq y la ejecutamos con el siguiente comando: python holamundo.py. 
Obtenemos esta ejecución:


![im5](https://dl.dropbox.com/s/drhvijpl142zrnl/p5.png)


Estamos ejecutando la aplicación holamundo.py a través de una jaula.

Bibliografía
============================









http://rafinguer.blogspot.com.es/2010/10/aplicaciones-web-sencillas-con-python.html





