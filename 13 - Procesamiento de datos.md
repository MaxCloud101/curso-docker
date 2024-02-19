# Procesamiento de datos

1 Vamos a crear un repositorio de contenedores en AWS ECR

<center>
<img src="img/pa-ecr1.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/pa-ecr2.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/pa-ecr3.png" style="width: 100%; max-width: 600px;">
</center>


2 Vamos a clonar el repositorio de GitHub en nuestro ambiente en Cloud9

```sh
$ git clone https://github.com/MaxCloud101/curso-docker.git
```
<center>
<img src="img/pa-github1.png" style="width: 100%; max-width: 600px;">
</center>

A continuación nos digimos a la carpeta "processapp", construimos la imagen Docker y la subimos a ECR (Reemplazamos XXXXXXXXXXX por nuestro numero de cuenta)

```sh
$ cd curso-docker/processapp/
$  aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin XXXXXXXXXXX.dkr.ecr.us-west-2.amazonaws.com
$ docker build -t procesapp .
$ docker tag procesapp:latest XXXXXXXXXXX.dkr.ecr.us-west-2.amazonaws.com/procesapp:latest
$ docker push XXXXXXXXXXX.dkr.ecr.us-west-2.amazonaws.com/procesapp:latest
```

<center>
<img src="img/pa-dockerbuild.png" style="width: 100%; max-width: 600px;">
</center>

Si realizamos los pasos correctamente, se mostrara la imagen en nuestro repositorio

<center>
<img src="img/pa-ecr4.png" style="width: 100%; max-width: 600px;">
</center>

3 Configuracion de la red

Nosotros vamos a lanzar contenedores en AWS batch, estos contenedores no van a tener una IP publica, solo tendrán una IP privada, por ello no podrán conectarse a diferentes APIs mediante HTTPS, para que los paquetes de red que salgan hacia internet y puedan tener una IP publica vamos a colocar los contenedores en una subnet privada, luego dejaremos que los paquetes salgan por un NAT gateway localizado en una subnet publica, estos paquetes ahora contendrán la IP publica del NAT Gateway y podrán ser dirigidos hacia internet

Actualmente en mi cuenta tengo la red con el CIDR: 172.31.0.0/16, con las siguientes subnets publicas

172.31.0.0/20
172.31.16.0/20
172.31.32.0/20
172.31.48.0/20

a continuación voy a agregar el siguiente segmento de red, que sera privada

172.31.64.0/20

Vamos al servicio de VPC, luego vamos al apartado de subnets, y le damos click en "Create Subnet" y llenamos los campos requeridos

<center>
<img src="img/pa-subnet1.png" style="width: 100%; max-width: 600px;">
</center>

A continuación vamos a la sección NAT Gateway, llenamos la información necesaria y le damos click en "Create NAT Gateway" (debes darle click en Allocate Elastic IP, también debes seleccionar cualquier subnet publica, no la que nosotros creamos)

<center>
<img src="img/nat-gateway.png" style="width: 100%; max-width: 600px;">
</center>

Luego vamos a la pestaña "Route Table" y le damos click en "Create route Table" 

<center>
<img src="img/pa-subnet3.png" style="width: 100%; max-width: 600px;">
</center>

En la route table creada vamos a darle click en "Edit Routes" y agregamos la ruta al Nat Gateway

<center>
<img src="img/pa-subnet4.png" style="width: 100%; max-width: 600px;">
</center>

Luego vamos a la pestaña "Subnet associations" y agregamos la route table a la subnet private, finalmente debería quedar como se muestra en la imagen

<center>
<img src="img/pa-subnet5.png" style="width: 100%; max-width: 600px;">
</center>

Si se configuro correctamente todos los recursos lanzados en la subnet privada ahora tendrán acceso a internet

4 Para crear el cluster de Fargate nos vamos al servicio de AWS Batch, luego a la pestaña de "Compute Environments" y le damos click en "Create"

<center>
<img src="img/pa-fargate1.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/pa-fargate2.png" style="width: 100%; max-width: 600px;">
</center>

En la siguiente pestaña no olvides solamente seleccionar la subnet privada que acabamos de crear (Esto para que los contenedores solo se lancen en la subnet privada)

<center>
<img src="img/pa-fargate3.png" style="width: 100%; max-width: 600px;">
</center>

Vamos a la ultima pantalla de Review y le damos click en "Create"

5 Vamos al servicio de S3 y le damos click en "Create Bucket", aquí colocamos el nombre del bucket y le damos click en "Create Bucket"

<center>
<img src="img/pa-s31.png" style="width: 100%; max-width: 600px;">
</center>

Luego entramos al Bucket y en la pestaña "properties"  en la sección Amazon EventBridge le damos click en "Edit" y le damos a "On"

<center>
<img src="img/pa-s32.png" style="width: 100%; max-width: 600px;">
</center>

6 A continuación vamos a configurar nuestro Job con AWS Batch, para ello vamos a ir a AWS IAM, aquí vamos a revisar que exista el role ecsTaskExecutionRole, si no existe lo creamos y verificamos que tenga los siguientes permisos atachados:

<center>
<img src="img/pa-permissions1.png" style="width: 100%; max-width: 600px;">
</center>

Luego vamos a crear un IAM Role, vamos a darle click en el menú lateral Roles y luego a "Create Role", vamos a rellenar la información como se muestra en la imagen

<center>
<img src="img/pa-role1.png" style="width: 100%; max-width: 600px;">
</center>

En la siguiente pestaña vamos a agregar los permisos

AmazonDynamoDBFullAccess
AmazonS3FullAccess

En la siguiente pestaña solo vamos a colocar el nombre y vamos a darle click en "Create Role"

<center>
<img src="img/pa-permissions2.png" style="width: 100%; max-width: 600px;">
</center>

Ahora nos dirigimos al servicio de AWS Batch, le damos click en "Job definitions" luego le damos click en "Create" y llenamos la siguiente información:

<center>
<img src="img/pa-batch1.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/pa-batch2.png" style="width: 100%; max-width: 600px;">
</center>

En la siguiente pestaña vamos a configurar:

<center>
<img src="img/pa-batch3.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/pa-batch4.png" style="width: 100%; max-width: 600px;">
</center>

En la siguiente pestaña no colocamos nada y le damos click en "Next".

En la pestaña de "Job definition review" le damos click en "Create job definition"

Ahora vamos a crear una cola, para ello vamos a al menú lateral en el apartado "Job queues" y le damos click en "Create", colocamos la siguiente información:

<center>
<img src="img/pa-batch5.png" style="width: 100%; max-width: 600px;">
</center>

Luego le damos click en "Create job queue"

7 Ahora vamos a crear la maquina de estados en "Step function". Para ello vamos al servicio de Step Functions y le damos click en "Create state machine", seleccionamos una plantilla en blanco, vamos a configurar la siguiente información

<center>
<img src="img/stepfunction1.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/stepfunction2.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/stepfunction3.png" style="width: 100%; max-width: 600px;">
</center>

```sh
{
  "Environment": [
    {
      "Name": "S3_KEY",
      "Value.$": "$.detail.object.key"
    },
    {
      "Name": "S3_BUCKET",
      "Value.$": "$.detail.bucket.name"
    }
  ]
}
```

<center>
<img src="img/stepfunction4.png" style="width: 100%; max-width: 600px;">
</center>

Finalmente le damos click en "Create", nos va a pedir agregar algunos permisos los aceptamos y continuamos

8 Vamos a conectar los eventos en Amazon EventBridge, vamos a la pestaña rules y le damos click en "Create Rule"

<center>
<img src="img/eventbridge1.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/eventbridge2.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/eventbridge3.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/eventbridge4.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/eventbridge5.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/eventbridge6.png" style="width: 100%; max-width: 600px;">
</center>

Finalmente le damos click en Next y en el ultimo paso le damos click en "Create Rule"

9 Creamos nuestra tabla en DynamoDB

<center>
<img src="img/dynamo1.png" style="width: 100%; max-width: 600px;">
</center>

10 Para probar toda la ejecución de nuestro pipeline vamos a subir el archivo 2023-12-01.csv que se encuentra en nuestro repositorio al bucket en S3 y vemos que la maquina de estados se empieza a ejecutar

<center>
<img src="img/test1.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/test2.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/test3.png" style="width: 100%; max-width: 600px;">
</center>

Si todo se realzó con éxito vamos a ver el paso de la maquina de estados en verde y la información en DynamoDB

<center>
<img src="img/test4.png" style="width: 100%; max-width: 600px;">
</center>

<center>
<img src="img/test5.png" style="width: 100%; max-width: 600px;">
</center>

11 Finalmente no olvides eliminar los siguiente recursos

1 Tabla en DynamoDB

2 Regla en Amazon EventBridge

3 Maquina de estados en Step Function

4 En AWS Batch primero debes deshabilitar la cola y luego eliminar

5 En Job definitions no se puede eliminar la definición del job, solo se puede "Deregister

6 Eliminar el el repositio en AWS ECR

7 Eliminar el nat Gateway

8 Una vez se elimine el Nat Gateway vamos a Elastic Ip debes seleccionar el recurso creado y darle "Release Elastic IP addresses"

9 Eliminar la subnet privada que habíamos creado

10 Eliminar la route table
