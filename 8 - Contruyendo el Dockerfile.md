# Contruyendo el Dockerfile

Un Dockerfile es un archivo o documento de texto simple que incluye una serie de instrucciones que se necesitan ejecutar de manera consecutiva para cumplir con los procesos necesarios para la creación de una nueva imagen.

## 1 Estructura

El dockerfile puede contener los siguinetes elementos:

FROM: Permite especificar la imagen base.

MAINTAINER: Especifique el autor de una imagen.

RUN: Ejecute comandos de compilación

WORKDIR: Cambiar directorio de trabajo.

COPY: Copiar archivos y directorios.

ADD: Agregue archivos y directorios locales o remotos.

EXPOSE: Describe en qué puertos escucha tu aplicación.

VOLUME: Crea un volumen para montar.

ENV: Establece variables de entorno.

ARG: Utilice variables de tiempo de construcción.

ENTRYPOINT: Especifica el ejecutable predeterminado.

CMD: Especifique comandos predeterminados.

## 2 Ejemplo

Vamos a posicionarnos en la carpeta flaskapp dentro de este repositorio. Luego vamos a lanzar el siguiente comando para empezar la construccion del contenedor

```sh
$ docker build -t myapp .
```

Una vez que el build fue exitoso, vamos a lanzar el contenedor

```sh
$ docker run -p 8000:8000 myapp
```
