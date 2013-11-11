Práctica 2: Aislamiento de una aplicación web usando jaulas.
===========================

En esta práctica, voy a aislar una pequeña aplicacion web en una jaula. Usaré el sistema operativo
ubuntu 12.10 "(quantal quetzal), con una arquitectura de 32 bits.

Creación de la jaula
========================

Para crear la jaula recurrimos a la herramienta debootstrap, que permite enjaular un SO Debian (Ubuntu, Guadalinex, Debian) a 
través del siguiente comando:  "sudo debootstrap --arch=i386 quantal /home/jaulas/quantal/ http://archive.ubuntu.com/ubuntu". 
Como se puede observar, --arch=i386 indica que se va a instalar la jaula en 32 bits y que se instalará en la carpeta 
arriba mencionada.

![im1](https://dl.dropbox.com/s/zogv6ainvzro6nw/p1.png)

Posteriormente ejecutamos la jaula con la orden "sudo chroot /home/jaulas/quantal" y procedemos a configurar el sistema
a nuestro gusto. 

  - Montamos el directorio /proc y cambiamos el idioma a español.
  - Instalamos librerias que vamos a necesitar a continuación, tal como python, o web-python.


![im1](https://dl.dropbox.com/s/4ytqaqvwzl5r2rl/p2.png)

![im1](https://dl.dropbox.com/s/2wm0ohepa2o9odn/p3.png)





