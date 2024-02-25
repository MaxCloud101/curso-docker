# Trabajando con volúmenes

Los volúmenes son el mecanismo para conservar los datos generados y utilizados por los contenedores Docker.

## Comandos mas importantes

#### docker volume create

Crea un nuevo volumen en el que los contenedores pueden consumir y almacenar datos. Si no se especifica un nombre, Docker genera un nombre aleatorio.

```sh
$ docker volume create [VOLUME]
```

#### docker volume ls

Lista los volúmenes

```sh
$ docker volume ls
```

#### docker volume rm

Elimina uno o mas volúmenes

```sh
$ docker volume rm [VOLUME...]
```
#### docker volume inspect

Devuelve información sobre un volumen.

```sh
$ docker volume inspect
```

## Montando volumenes en contenedores

#### Montamos un volumen en el contenedor
Podemos montar un volumen mientras arrancamos un containers, si el volumen no se creo previamente este se crea, el formato usado sera "-v VOLUME_NAME:CONTAINER_PATH"

```sh
docker run -v demo_volume:/app -p 8081:80 -d nginx
```

Podemos montar el mismo volumen en varios contenedores al mismo tiempo

#### Montamos con una carpeta del host en el contenedor

También podemos montar un volumen del contenedor y enlazarlo con una carpeta en el host, el formato usado sera "-v HOST_PATH:CONTAINER_PATH"

```sh
docker run -v /home/ec2-user/environment/max:/app -p 8080:80 -d nginx
```

## Eliminando todos los recursos creados

Si deseas eliminar rapidamente todos los recursos creados (containers, networks, images), utilizaras el siguiente comando

```sh
docker system prune -a
```

Si tambien quieres eliminar los volumenes, debes lanzar el siguiente comando

```sh
docker system prune -a --volumes
```
