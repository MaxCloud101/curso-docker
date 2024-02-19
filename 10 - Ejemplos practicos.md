# Ejemplos practicos

## Trabajando con postgresql

1 Vamos a inicializar un contenedor con postgresql

```sh
$ docker run -d \
	--name my-postgres \
	-e POSTGRES_PASSWORD=mysecretpassword \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
	-v /custom/mount:/var/lib/postgresql/data \
	-p 5000:5432 postgres
```

2 Instalamos postgresql en nuestro host para utilizar el cliente psql y poder conectarnos al postgres corriendo dentro del contenedor (Los siguientes comandos son para Amazon Linux 2023)

```sh
sudo dnf update
sudo dnf install postgresql15.x86_64 postgresql15-server -y
```

3 Nos conectamos al postgresql corriendo dentro del contenedor

```sh
$ psql -h localhost -p 5000 -U postgres
```


## Trabajando con redis

1 Vamos a inicializar el contenedor con redis

```sh
$ docker run -d --name myredis -p 6000:6379 redis
```

2 Vamos a instalar redis en el host local (Los siguientes comandos son para Amazon Linux 2023)

```sh
sudo dnf install -y redis6
sudo systemctl start redis6
sudo systemctl enable redis6
sudo systemctl is-enabled redis6
redis6-server --version
redis6-cli ping
```
3 Ahora nos conectamos desde nuestro host local hacia el redis corriendo en el contenedor

```sh
redis6-cli -h localhost -p 6000
```
