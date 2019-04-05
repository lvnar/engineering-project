# **Thorondor**

## Contenidos

- [**Thorondor**](#thorondor)
  - [Contenidos](#contenidos)
  - [Dependencias](#dependencias)
  - [Aplicación de Rastreo](#aplicaci%C3%B3n-de-rastreo)
  - [Deploy](#deploy)
  - [Ambiente de pruebas](#ambiente-de-pruebas)
    - [Servicios](#servicios)
    - [Configuración inicial](#configuraci%C3%B3n-inicial)

## Dependencias

![1](https://img.shields.io/badge/Thoron-1.0-darkred.svg)
![2](https://img.shields.io/badge/Meneldor-1.0-darkred.svg)
![3](https://img.shields.io/badge/Gwaihir-1.0-darkred.svg)

![](https://img.shields.io/badge/docker-*-blue.svg)
![](https://img.shields.io/badge/docker--compose-*-blue.svg)


## Aplicación de Rastreo

Aplicación que permite a un grupo de usuarios administrar su correspondiente flotilla de vehículos, es decir, definir sus propiedades, incluida su posición.

Está dividida en tres componentes principales:

- [**Gwaihir**][3]: Web app para acceso de usuarios finales.
- [**Thoron**][1]: REST API que proporciona los servicios necesarios para:
  - Manejo de sesión.
  - Administración de usuarios.
  - Administración de vehículos.
- [**Meneldor**][2]: Base de datos que almacena la información requerida por el sistema.

## Deploy

1. Crear el archivo `.env` en la raíz del directorio, es decir, en la misma ubicación del archivo `docker-compose.yml`.
   
2. Establecer las variables de entorno dentro de dicho archivo, es decir, las variables de la base de datos. Por ejemplo:
    ```
    ### Thorondor/.env
    
    # Nombre de la base de datos
    POSTGRES_DB=thorondor
    
    # Nombre de usuario
    POSTGRES_USER=user
    
    # Contraseña de usuario
    POSTGRES_PASSWORD=password
    ```

3. En la misma ubicación, junto a `docker-compose.yml`, se inician los contenedores con el siguiente comando:
   ```
   $ docker-compose up -d
   ```
   **\*Nota**: Para permitir el acceso externo a la base de datos, antes de iniciar los contenedores, es necesario descomentar el par de líneas correspondientes en dicho archivo y establecer el puerto deseado.

4. Es necesario crear el usuario administrador que permitirá dar de alta los usuarios del sistema. Ésto es posible con el siguiente comando y proporcionando la información solicitada:
   ```
   $ docker exec -it thoron python manage.py createsuperuser
   
   Nombre de usuario (leave blank to use 'root'): admin
   Dirección de correo electrónico: admin@thorondor.net
   Password: *****
   Password (again): ***** 
   Superuser created successfully.
   ```
5. Luego de loggear al usuario *admin*, es posible hacer uso de los servicios `/user` para dar de alta a los usuario requeridos. [**Ver Thoron**][1].

6. A partir de este momento, cada usuario es capaz de administrar su propio grupo de vehículos.


## Ambiente de pruebas

Para fines de testeo de la aplicación, se dieron de alta los tres servicios en una instancia de [**AWS**][4]. Éste puede ser encontrado en la dirección [**ec2-18-220-20-71.us-east-2.compute.amazonaws.com**](http://ec2-18-220-20-71.us-east-2.compute.amazonaws.com).

### Servicios

Se decidió permitir el acceso externo a los servicos, para monitoreo. Se han evitado los puertos por defecto y se establecieron de la siguiente forma:
- [**Gwahir**][3]: Puerto 80 
- [**Thoron**][1]: Puerto 8080
- [**Meneldor**][2]: Puerto 5000

### Configuración inicial

Ha sido dado de alta un usuario administrador y uno regular para permitir el acceso a la aplicación web y a los servicios. Las credenciales son las siguientes:
- Administrador:
  - Nombre de usuario: admin
  - Contraseña: password

- Usuario:
  - Nombre de usuario: user1
  - Contraseña: password


[1]: Thoron/README.md
[2]: Meneldor/README.md
[3]: Gwaihir/README.md
[4]: https://aws.amazon.com/es/