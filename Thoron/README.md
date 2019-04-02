# **Thoron**

## Contenidos

- [**Thoron**](#thoron)
  - [Contenidos](#contenidos)
  - [Dependencias](#dependencias)
  - [Descripción](#descripci%C3%B3n)
    - [Funcionalidad](#funcionalidad)
      - [Autenticación](#autenticaci%C3%B3n)
      - [Superusuario](#superusuario)
      - [Usuario](#usuario)
  - [Servicios API](#servicios-api)
  - [Documentación y pruebas](#documentaci%C3%B3n-y-pruebas)

## Dependencias

![](https://img.shields.io/badge/alpine-3.9-orange.svg)

![](https://img.shields.io/badge/python-3.7-darkgreen.svg)
![](https://img.shields.io/badge/django-2.1.7-darkgreen.svg)

## Descripción

Aplicación de ratreo creada con [**Django**](1). Servicios REST donde se administra un grupo de usuarios y su correspondiente flotilla de vehículos, es decir, definir sus propiedades y su posición.

Cada vehículo tiene los siguientes datos:
1. Id de vehículo
2. Placas
3. Última posición conocida (latitud,longitud)

### Funcionalidad

#### Autenticación

La aplicación es capaz de permitir el acceso de usuarios mediante el uso de un nombre de usuario (*username*) y contraseña (*password*). Cuenta con dos nieveles de administración, *superusuario* y *usuario*.

#### Superusuario

Hace uso del [*superusuario* propio de **Django**](2) para ser dado de alta. Tiene la capacidad de administrar los usuarios del sistema.

#### Usuario

Tienen por objetivo la administración de un grupo de vehículos. Este tipo de usuario es capaz de:
 - Insertar un vehículo.
 - Actualizar un vehículo.
 - Borrar cada vehículo.
 - Ver los vehículos que ha insertado.

## Servicios API

<table>
    <thead>
        <tr>
            <th>Colección</th>
            <th>URI</th>
            <th>Method</th>
            <th>Descripción</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=3>Sesión</td>
            <td>/login/</td>
            <td>POST</td>
            <td>Iniciar sesión</td>
        </tr>
        <tr>
            <td>/logout/</td>
            <td>POST</td>
            <td>Cerrar sesión</td>
        </tr>
        <tr>
            <td>/user/</td>
            <td>GET</td>
            <td>Usuario actual</td>
        </tr>
        <tr>
            <td rowspan=5>Usuarios</td>
            <td rowspan=2>/users/</td>
            <td>GET</td>
            <td>Listar usuarios</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>Crear usuario</td>
        </tr>
        <tr>
            <td rowspan=3>/users/{id}/</td>
            <td>GET</td>
            <td>Detalle usuario</td>
        </tr>
        <tr>
            <td>PUT, PATCH</td>
            <td>Actualizar usuario*</td>
        </tr>
        <tr>
            <td>DELETE</td>
            <td>Eliminar usuario</td>
        </tr>
        <tr>
            <td rowspan=5>Vehículos</td>
            <td rowspan=2>/vehicles/</td>
            <td>GET</td>
            <td>Listar vehículos</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>Crear vehículo</td>
        </tr>
        <tr>
            <td rowspan=3>/vehicles/{id}/</td>
            <td>GET</td>
            <td>Detalle vehículo</td>
        </tr>
        <tr>
            <td>PUT, PATCH</td>
            <td>Actualizar vehículo*</td>
        </tr>
        <tr>
            <td>DELETE</td>
            <td>Eliminar vehículo</td>
        </tr>
    </tbody>
</table>

**\*Nota:** Se recomienda el uso del método *PATCH* para actualizar una entidad. El método *PUT* el más común, pero requiere una actualización completa. [Ver más.](4)

## Documentación y pruebas

Se ha desarrollado, en [**Postman**](5), la documentación detallada del API. [**Ver documentación completa**](https://documenter.getpostman.com/view/552873/S17xrkSb).

Además, se implementaron pruebas unitarias  que pueden ser ejecutadas de forma manual. El botón de abajo permite importar la colección de peticiones (*Thoron*) y las variables de ambiente requeridas (*Thorondor*).

De acuerdo a las variables iniciales, es posible alcanzar el servidor local o el servidor en [**AWS**](6), bajo la dirección **ec2-18-220-20-71.us-east-2.compute.amazonaws.com:8080**. 
  
  [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/d2e4e43cc100083d2f06#?env%5BThorondor%20EC2%5D=W3siZGVzY3JpcHRpb24iOnsiY29udGVudCI6IiIsInR5cGUiOiJ0ZXh0L3BsYWluIn0sInZhbHVlIjoiZWMyLTE4LTIyMC0yMC03MS51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tOjgwODAiLCJrZXkiOiJob3N0IiwiZW5hYmxlZCI6dHJ1ZX0seyJkZXNjcmlwdGlvbiI6eyJjb250ZW50IjoiIiwidHlwZSI6InRleHQvcGxhaW4ifSwidmFsdWUiOiJhZG1pbiIsImtleSI6InVzZXJuYW1lIiwiZW5hYmxlZCI6dHJ1ZX0seyJkZXNjcmlwdGlvbiI6eyJjb250ZW50IjoiIiwidHlwZSI6InRleHQvcGxhaW4ifSwidmFsdWUiOiI4Iiwia2V5IjoidXNlcl9pZHgiLCJlbmFibGVkIjp0cnVlfSx7ImRlc2NyaXB0aW9uIjp7ImNvbnRlbnQiOiIiLCJ0eXBlIjoidGV4dC9wbGFpbiJ9LCJ2YWx1ZSI6IjEiLCJrZXkiOiJ2ZWhpY2xlX2lkeCIsImVuYWJsZWQiOnRydWV9LHsidmFsdWUiOiI1N2M4MzA5Mzg2Zjc5YmQ3ZGQ2Njg2M2M1ZWM5MDNjZDNlZjA5NzMzIiwia2V5IjoiYWRtaW5fdG9rZW4iLCJlbmFibGVkIjp0cnVlfSx7InZhbHVlIjoiNTdjODMwOTM4NmY3OWJkN2RkNjY4NjNjNWVjOTAzY2QzZWYwOTczMyIsImtleSI6InRva2VuIiwiZW5hYmxlZCI6dHJ1ZX0seyJ2YWx1ZSI6InVzZXI2Iiwia2V5IjoibmV3X3VzZXIiLCJlbmFibGVkIjp0cnVlfSx7InZhbHVlIjo3LCJrZXkiOiJ1c2VyX2lkIiwiZW5hYmxlZCI6dHJ1ZX0seyJ2YWx1ZSI6IjBlMmUxMmY5MmVmMDQwMTZkZDU4YTA2NGZkZjkwNzkxYTUzZDNlNTUiLCJrZXkiOiJ1c2VyX3Rva2VuIiwiZW5hYmxlZCI6dHJ1ZX0seyJ2YWx1ZSI6IkNBUjA3MDAxIiwia2V5IjoibmV3X3ZlaGljbGUiLCJlbmFibGVkIjp0cnVlfSx7InZhbHVlIjo1LCJrZXkiOiJ2ZWhpY2xlX2lkIiwiZW5hYmxlZCI6dHJ1ZX1d)




[1]: https://docs.djangoproject.com/es/2.1/
[2]: https://docs.djangoproject.com/en/1.9/ref/django-admin/#createsuperuser
[3]: https://documenter.getpostman.com/view/552873/S17xrkHt
[4]: https://medium.com/backticks-tildes/restful-api-design-put-vs-patch-4a061aa3ed0b
[5]: https://www.getpostman.com/
[6]: https://aws.amazon.com/es/

