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

## Dependencias

![](https://img.shields.io/badge/python-3.7-darkgreen.svg)
![](https://img.shields.io/badge/django-2.1.7-darkgreen.svg)

![](https://img.shields.io/badge/docker-*-blue.svg)
![](https://img.shields.io/badge/docker--compose-*-blue.svg)

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

Hace uso del [*superusuario* propio de **Django**](2) para ser dado alta. Tiene la capacidad de administrar los usuarios del sistema.

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

**\*** Se recomienda el uso del método *PATCH* para actualizar de forma parcial una entidad. El método *PUT* el más común para este fin, pero requiere una actualización completa. [Ver más.](3)


[1]: https://docs.djangoproject.com/es/2.1/
[2]: https://docs.djangoproject.com/en/1.9/ref/django-admin/#createsuperuser
[3]: https://medium.com/backticks-tildes/restful-api-design-put-vs-patch-4a061aa3ed0b