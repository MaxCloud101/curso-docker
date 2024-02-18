# Introducción

## 1 Introducción

Docker es un proyecto de código abierto que automatiza el despliegue de aplicaciones dentro de contenedores de software, proporcionando una capa adicional de abstracción y automatización de virtualización de aplicaciones en múltiples sistemas operativos.

El núcleo de Docker está formado por el motor Docker, un demonio de software de host único que permite crear y administrar contenedores. Antes de empezar a usar Docker, debes instalar el motor Docker en un host, ya sea una computadora de escritorio, portátil o un servidor.

Docker está escrito en el lenguaje de programación Go y aprovecha varias características del kernel de Linux para ofrecer su funcionalidad.

## 2 Arquitectura de Docker

Docker utiliza una arquitectura cliente-servidor. El cliente de Docker se comunica con el demonio Docker, que realiza el trabajo de crear, ejecutar y distribuir sus contenedores Docker. El cliente de Docker y el demonio pueden ejecutarse en el mismo sistema, o puede conectar un cliente Docker a un demonio Docker remoto. El cliente de Docker y el demonio se comunican mediante una API REST, a través de sockets UNIX o una interfaz de red.

<center>
<img src="img/docker-architecture.webp" style="width: 100%; max-width: 600px;">
</center>

### El demonio Docker

El demonio de Docker (dockerd) escucha las solicitudes de la API de Docker y administra objetos de Docker como imágenes, contenedores, redes y volúmenes. Un demonio también puede comunicarse con otros demonios para administrar los servicios de Docker.

### El cliente Docker

El cliente de Docker (docker) es la forma principal en que muchos usuarios de Docker interactúan con Docker. Cuando utiliza comandos como docker run, el cliente envía estos comandos a dockerd, quien los ejecuta. El comando Docker utiliza la API de Docker. El cliente Docker puede comunicarse con más de un demonio.

### Registro de Docker

Un registro de Docker almacena imágenes de Docker. Por ejemplo Docker Hub es un registro público que cualquiera puede usar y Docker busca imágenes en Docker Hub de forma predeterminada. También puedes utilizar tu propio registro privado.

Cuando utiliza los comandos docker pull o docker run, Docker extrae las imágenes necesarias de su registro configurado. Cuando utiliza el comando docker push, Docker envía su imagen a su registro configurado.

### Imágenes

Una imagen es una plantilla de solo lectura con instrucciones para crear un contenedor Docker. Usualmente, una imagen se basa en otra imagen, con alguna personalización adicional. Por ejemplo, puedes crear una imagen basada en la imagen de Ubuntu, pero con el servidor web Apache y tu aplicación, así como los detalles de configuración necesarios para que tu aplicación se ejecute.

Puedes crear tus propias imágenes o utilizar únicamente aquellas creadas por otros y publicadas en un registro. Para crear tu propia imagen, crea un Dockerfile con una sintaxis simple para definir los pasos necesarios para crear la imagen y ejecutala. 

### Contenedores

Un contenedor es una instancia ejecutable de una imagen. Puedes crear, iniciar, detener, mover o eliminar un contenedor mediante la API o CLI de Docker. Puedes conectar un contenedor a una o más redes, adjuntarle almacenamiento o incluso crear una nueva imagen basada en su estado actual.

De forma predeterminada, un contenedor está relativamente bien aislado de otros contenedores y de su máquina host. Puedes controlar qué tan aislados están de la red, el almacenamiento u otros subsistemas subyacentes de un contenedor con respecto a otros contenedores o de la máquina host.

Un contenedor se define por su imagen, así como por las opciones de configuración que le proporciona cuando lo crea o inicia. Cuando se elimina un contenedor, cualquier cambio en su estado que no esté almacenado en un almacenamiento persistente desaparece.
