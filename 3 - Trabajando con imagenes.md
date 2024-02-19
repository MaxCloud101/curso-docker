# Trabajando con imágenes

Una imagen de Docker es una plantilla de solo lectura que define al contenedor. La imagen contiene el código que se ejecutará, incluida cualquier definición para cualquier biblioteca o dependencia que el código necesite.

## 1 Principales comandos

Para poder trabajar con las imágenes utilizaremos el comando docker de la siguiente forma "docker image [comando]"

#### docker image pull

Permite descargar una imagen de un registro

```sh
$ docker image pull NAME[:TAG]
```

El siguiente comando es equivalente

```sh
$ docker pull NAME[:TAG|@DIGEST]
```

Ejemplo de uso:

Deseamos descargar la imagen oficial de python, para ello nos dirigimos a docker hub en la siguiente url https://hub.docker.com/_/python

Si deseamos descargar la imagen de python con la etiqueta 3.12.1 lanzamos el siguiente comando:

```sh
$ docker pull python:3.12.1
```

También podemos hacerlo mediante el digesto

```sh
 $ docker pull python@sha256:a3d69b8412f7068fd060ccc7e175825713d5a767e1e14753e75bce6f746c8a7e
 ```

#### docker image push

Este comando permite subir las imágenes en el registro de Docker Hub o AWS ECR.

```sh
$ docker image push [OPTIONS] NAME[:TAG]
```

En secciones posteriores de este curso cubriremos con mas detalle este comando

#### docker image inspect

Muestra información detallada sobre una o más imágenes.

```sh
$ docker image inspect [IMAGE...]
```

#### docker image ls

Este comando mostrará todas las imágenes de nivel superior, su repositorio, etiquetas y su tamaño.

 ```sh
$ docker image ls
```

Para ver los digestos lanzaremos el siguiente comando

```sh
$ docker image ls --digests
```

Para ver todas las imágenes incluyendo las capas intermedias usaremos

```sh
$ docker image ls --all
```

#### docker rm

Para eliminar una o mas imágenes corremos el comando

```sh
$ docker image rm [IMAGE...]
```
