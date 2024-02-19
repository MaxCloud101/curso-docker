# Taller 1: CI/CD con GitHub, CircleCI y DockerHub

1 Primero vamos a realizar un fork del repositorio, para tener el proyecto en nuestra cuenta de GitHub

<center>
<img src="img/fork1.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/fork2.png" style="width: 100%; max-width: 600px;">
</center>

2 Tenemos que crear nuestra cuenta en CircleCi y darle los permisos necesarios(En mi caso aparecen 2 por que en mi cuenta de GitHub tengo una organización, solo debería aparecerte una)

<center>
<img src="img/circleci1.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/circleci2.png" style="width: 100%; max-width: 600px;">
</center>

A continuación nos pide nuestra contraseña de github para confirmar la integración.

<center>
<img src="img/circleci3.png" style="width: 100%; max-width: 600px;">
</center>

Luego se nos mostrará la pantalla para crear un nuevo proyecto, colocamos el nombre del proyecto y vamos al paso 3 (Vamos a generar el ssh key)

<center>
<img src="img/circleci4.png" style="width: 100%; max-width: 600px;">
</center>

En caso te aparezca la siguiente pantalla y no la anterior, le das click en "Create Proyect"

<center>
<img src="img/circleci5.png" style="width: 100%; max-width: 600px;">
</center>

Aquí vas a selección Github y te mostrara la pantalla anteriormente vista

<center>
<img src="img/circleci6.png" style="width: 100%; max-width: 600px;">
</center>

3 Vamos a nuestra cuenta de AWS y vamos a crear un nuevo ambiente en AWS Cloud9. 

<center>
<img src="img/cloud9.png" style="width: 100%; max-width: 600px;">
</center>

Lazaremos el siguiente comando en la consola de Cloud9

```sh
$ ssh-keygen -t ed25519 -f ~/.ssh/project_key -C maxcloud@gmail.com
```

<center>
<img src="img/cloud9-1.png" style="width: 100%; max-width: 600px;">
</center>

Ahora verificamos que se haya generado la llave publica y privada (La llave publica termina en .pub)

<center>
<img src="img/cloud9-2.png" style="width: 600px;">
</center>

Revisamos el contenido de la llave privada

<center>
<img src="img/cloud9-3.png" style="width: 600px;">
</center>

Colocamos el contenido de la llave privada y los campos requeridos en la siguiente pantalla, y le damos click en "Create Project"

<center>
<img src="img/circleci-complete.png" style="width: 100%; max-width: 600px;">
</center>

Nuestro proyecto en CircleCi se ha configurado y se nos mostrara la siguiente pantalla

<center>
<img src="img/circleci-complete-2.png" style="width: 100%; max-width: 600px;">
</center>

4 Ahora para configurar la llave publica en nuestro repositorio en GitHub, vamos a la pestaña "Settings" de nuestro repositorio

<center>
<img src="img/github-conf1.png" style="width: 100%; max-width: 600px;">
</center>

Luego al menu lateral "Deploy keys"

<center>
<img src="img/github-conf2.png" style="width: 100%; max-width: 600px;">
</center>

A continuacion click en "Add deploy key"

<center>
<img src="img/github-conf3.png" style="width: 100%; max-width: 600px;">
</center>

Vamos a nuestro ambiente en cloud9 para ver el contenido de nuestra llave publica

<center>
<img src="img/github-conf4.png" style="width: 100%; max-width: 600px;">
</center>

Agregamos el contenido de la llave publica a nuestra "Deploy key" como se muestra en pantalla y le damos click en "Add key"

<center>
<img src="img/github-conf5.png" style="width: 100%; max-width: 600px;">
</center>

Nos requerirá nuestra contraseña, la colocamos y se mostrara la siguiente pantalla

<center>
<img src="img/github-conf6.png" style="width: 100%; max-width: 600px;">
</center>

5 Ahora vamos a configurar DockerHub, para ello creamos una cuenta en DockerHub, luego le damos click en "Create repository"

<center>
<img src="img/dockerhub-1.png" style="width: 100%; max-width: 600px;">
</center>

Colocamos el nombre "myapp" y le damos click en "Create" como se muestra en la imagen

<center>
<img src="img/dockerhub-2.png" style="width: 100%; max-width: 600px;">
</center>

6 Vamos a configurar las variables de entorno en nuestro proyecto en CircleCI. Para esto vamos a "Proyect settings"

<center>
<img src="img/circleci-config-1.png" style="width: 100%; max-width: 600px;">
</center>

En la siguiente pestaña le damos click en "add Environment Variable"

<center>
<img src="img/circleci-config-2.png" style="width: 100%; max-width: 600px;">
</center>

Aquí vamos a colocar nuestra primera variable de entorno (Tu ID de DockerHub)

<center>
<img src="img/circleci-config-3.png" style="width: 100%; max-width: 400px;">
</center>

Luego colocamos nuestra contraseña

<center>
<img src="img/circleci-config-4.png" style="width: 100%; max-width: 400px;">
</center>

7 Vamos a clonar nuestro repositorio a nuestro ambiente de AWS cloud9

<center>
<img src="img/circleci-config-5.png" style="width: 100%; max-width: 600px;">
</center>

En nuestro ambiente de cloud9 vamos a lanzar el siguiente comando:

```sh
$ git clone https://github.com/MaxCloud101/curso-docker.git
```

<center>
<img src="img/github-conf7.png" style="width: 100%; max-width: 600px;">
</center>

En el panel lateral observamos que se ha clonado correctamente nuestro proyecto.

8 Para disparar un build en CircleCI vamos a editar cualquier archivo y vamos a subir los cambios a nuestro repositorio en github.

Para ello lanzamos los siguientes comandos:

```sh
$ cd curso-docker/
$ git add README.md
$ git commit -m "Change README"
$ git push origin main
```

<center>
<img src="img/github-conf8.png" style="width: 100%; max-width: 600px;">
</center>

Vemos que se ha disparado un build solamente con el job de test

<center>
<img src="img/circleci7.png" style="width: 100%; max-width: 600px;">
</center>

Para dispar la construcción de una imagen Docker debemos crear un tag en el branch actual, para esto vamos a lanzar los siguientes comandos

```sh
$ git tag 1.1.0
$ git push --tags
```

<center>
<img src="img/github-conf9.png" style="width: 600px;">
</center>

Vemos en CircleCI que se ha generado otro build con dos jobs

<center>
<img src="img/circleci8.png" style="width: 100%; max-width: 600px;">
</center>

Ahora vamos a DockerHub y vemos que se realizado correctamente la construcción de nuestro contenedor

<center>
<img src="img/dockerhub-final.png" style="width: 100%; max-width: 600px;">
</center>

Si se han seguido todos los pasos correctamente debes tener configurado todo tu flujo de integración continua

Para mejorar la forma de trabajo para los desarrolladores se suele utilizar Gitflow, esta herramienta te va ayudar a facilitar la creación de ramas para nuevos desarrollo, despliegues a producción y resolución de Bugs.

Puedes encontrar la documentación de GitFlow aquí

https://www.atlassian.com/es/git/tutorials/comparing-workflows/gitflow-workflow

Al terminar este taller no te olvides eliminar todos los siguientes recursos.

- Eliminar el repositorio en DockerHub
- En CircleCi no hay forma de eliminar el proyecto, si deseas que desaparezca debes levantar un ticket de soporte. Pero puedes darle click y dejarlo como "Unfollow Project" para que no te envié ningún tipo de alerta

<center>
<img src="img/circlecifinal.png" style="width: 100%; max-width: 600px;">
</center>
