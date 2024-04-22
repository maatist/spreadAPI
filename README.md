# spreadAPI

Desafio de Buda para puesto de desarrollador.
La API tiene 3 endpoints los cuales consultan el spread de la totalidad de los mercados, fijan un spread de alerta y muestran una lista de los spread de los mercados verificados con el spread de alerta 

## Requisitos

- Docker

## Instalación

Primero, clona este repositorio en tu máquina local:

Luego, navega al directorio del proyecto

```bash
cd yourproject
```

Construye la imagen de Docker

```bash
docker build -t yourproject .
```
## Uso

```bash
docker run -p 4000:4000 yourproject
```
Ingresar a [localhost](http://localhost:4000/) para verificar el funcionamiento y ver la documentacion de la api

## Tests
### Opcion 1

Para ejecutar las pruebas, primero debes instalar las dependencias de prueba en tu maquina local:

```bash
pip install -r requirements.txt
```

Luego puedes ejecutar las pruebas con:

```bash
pytest
```

### Opcion 2

Con el contenedor docker corriendo, verificar el id del contenedor con:

```bash
docker ps                          
```

Y luego ejecutar las pruebas con 

```bash
docker exec -it <"docker_id"> pytest
```



