# Copiando data

Para poder copiar data entre el host y los contenedores  usaremos el comando copy 

#### docker cp

El comando cp te permitira copiar archivos, para ello usaremos el siguiente comando

```sh
docker cp CONTAINER:SRC_PATH DEST_PATH
docker cp SRC_PATH  CONTAINER:DEST_PATH
```
