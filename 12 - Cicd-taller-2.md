# Taller 1: CI/CD con AWS CodeCommit, AWS CodeBuild, AWS CodePipeline y AWS ECR

1 Vamos a crear nuestro repositorio en AWS CodeCommit

<center>
<img src="img/codecommit1.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/codecommit2.png" style="width: 100%; max-width: 600px;">
</center>

Clonaremos nuestro repositorio en nuestro ambiente en Cloud9

```sh
$ git clone https://git-codecommit.us-west-2.amazonaws.com/v1/repos/MaxCloud
```

<center>
<img src="img/codecommit3.png" style="width: 100%; max-width: 600px;">
</center>

A continuación vamos a copiar la carpeta flaskapp y el archivo buildspec.yml a nuestra carpeta con el repositorio de codecommit

<center>
<img src="img/codecommit4.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/codecommit5.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/codecommit6.png" style="width: 100%; max-width: 600px;">
</center>

Subimos estos archivos a nuestro repositorio en codecommit

```sh
$ cd MaxCloud
$ git add .
$ git commit -m "add files"
$ git push
```

<center>
<img src="img/codecommit7.png" style="width: 100%; max-width: 600px;">
</center>

2 Vamos a crear nuestro proyecto en AWS CodeBuild

<center>
<img src="img/codebuild1.png" style="width: 100%; max-width: 600px;">
</center>

Colocaremos la siguiente información:

<center>
<img src="img/codebuild2.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/codebuild3.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/codebuild4.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/codebuild5.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/codebuild6.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/codebuild7.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/codebuild8.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/codebuild9.png" style="width: 100%; max-width: 600px;">
</center>

Ahora le damos click en "Start Build"

<center>
<img src="img/codebuild10.png" style="width: 100%; max-width: 600px;">
</center>

Observamos que el build presenta un error, es por que el rol que utiliza codebuild no tiene permisos para hacer push en AWS ECR

<center>
<img src="img/codebuild11.png" style="width: 100%; max-width: 600px;">
</center>

3 Vamos a crear nuestro repositorio en AWS ECR

<center>
<img src="img/ecr-work-1.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/ecr-work-2.png" style="width: 100%; max-width: 600px;">
</center>

A continuación vamos a agregar permisos al rol de AWS CodeBuild para que pueda realizar el push a ECR. 

Vamos a nuestro proyecto en Codebuild y vamos a la pestaña "Proyect details" y nos vamos al apartado "Environment" y le damos click en "Service Role"

<center>
<img src="img/codebuild12.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/codebuild13.png" style="width: 100%; max-width: 600px;">
</center>

Vamos a darle click en "Attach policies"

<center>
<img src="img/permissions1.png" style="width: 100%; max-width: 600px;">
</center>

Vamos a filtrar el permiso "AmazonEC2ContainerRegistryFullAccess", lo seleccionamos y le damos click en "Add permission"

<center>
<img src="img/permissions2.png" style="width: 100%; max-width: 600px;">
</center>

Regresamos al proyecto en CodeBuild y le damos en "Start build"

<center>
<img src="img/codebuild14.png" style="width: 100%; max-width: 600px;">
</center>

El build falla, debido a que nos falta configurar la variable de entorno AWS_ACCOUNT_ID

<center>
<img src="img/codebuild15.png" style="width: 100%; max-width: 600px;">
</center>

Vamos a agregar la variable de entorno

<center>
<img src="img/codebuild16.png" style="width: 100%; max-width: 600px;">
</center>

Colocamos AWS_ACCOUNT_ID y en el valor colocamos el numero de nuestra cuenta, luego le damos "Update Environment"

<center>
<img src="img/codebuild17.png" style="width: 100%; max-width: 600px;">
</center>

Le volvemos a dar a "Star build" y vemos que ahora el build se realizo con éxito

<center>
<img src="img/codebuild18.png" style="width: 100%; max-width: 600px;">
</center>

Nuestra imagen Docker debe aparecer en AWS ECR

<center>
<img src="img/ecr-new.png" style="width: 100%; max-width: 600px;">
</center>

4 Vamos a automatizar la creación de imágenes cada vez que se haga un push en master, para ello vamos al servicio de AWS CodePipeline y le damos click en "Create pipeline"

<center>
<img src="img/codepipeline1.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/codepipeline2.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/codepipeline3.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/codepipeline4.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/codepipeline5.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/codepipeline6.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/codepipeline7.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/codepipeline8.png" style="width: 100%; max-width: 600px;">
</center>

Despues de crear el pipeline, este se va ejecutar automáticamente y vemos que se ha generado una nueva imagen docker automáticamente

<center>
<img src="img/ecr-build.png" style="width: 100%; max-width: 600px;">
</center>

Cada vez que realicemos un push a la rama main se va a ejecutar el pipeline y va a generar una nueva imagen Docker en AWS ECR

5 Debemos eliminar los recursos creados en

- AWS ECR
- AWS Codepipeline
- AWS Codebuild
- AWS CodeCommit
