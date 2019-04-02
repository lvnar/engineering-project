# **Thorondor**

## Contenidos

- [**Thorondor**](#thorondor)
  - [Contenidos](#contenidos)
  - [Dependencias](#dependencias)
  - [Aplicación de Rastreo](#aplicaci%C3%B3n-de-rastreo)
  - [Deploy](#deploy)

## Dependencias

![1](https://img.shields.io/badge/Thoron-1.0-darkred.svg)
![2](https://img.shields.io/badge/Meneldor-1.0-darkred.svg)

![](https://img.shields.io/badge/docker-*-blue.svg)
![](https://img.shields.io/badge/docker--compose-*-blue.svg)


## Aplicación de Rastreo

Aplicación que permite a un grupo de usuarios administrar su correspondiente flotilla de vehículos, es decir, definir sus propiedades, incluida su posición.

Está dividida en dos componentes principales:

- [**Thoron**](1): REST API que proporciona los servicios necesarios para:
  - Manejo de sesión.
  - Administración de usuarios.
  - Administración de vehículos.
- [**Meneldor**](2): Base de datos que almacena la información requerida por el sistema

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

4. Es necesario crear el usuario administrador que permitirá dar de alta los usarios del sistema. Ésto es posible con el siguiente comando y proporcionando la información solicitada:
   ```
   $ docker exec -it thoron python manage.py createsuperuser
   
   Nombre de usuario (leave blank to use 'root'): admin
   Dirección de correo electrónico: admin@thorondor.net
   Password: *****
   Password (again): ***** 
   Superuser created successfully.
   ```
5. Luego de loggear al usuario *admin*, es posible hacer uso de los servicios `/user` para dar de alta a los usuario requeridos. [**Ver Thoron**](1).

6. A partir de este momento, cada usuario es capaz de administrar su propio grupo de vehículos.


[1]: Thoron/README.md
[2]: Meneldor/README.md