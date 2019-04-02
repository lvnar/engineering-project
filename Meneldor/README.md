# **Meneldor**

## Contenidos

- [**Meneldor**](#meneldor)
  - [Contenidos](#contenidos)
  - [Dependencias](#dependencias)
  - [Descripción](#descripci%C3%B3n)

## Dependencias

![](https://img.shields.io/badge/alpine-3.9-orange.svg)
![](https://img.shields.io/badge/postgres-11.2-darkviolet.svg)

## Descripción

Contenedor de base de datos. La carpeta */postgres-data* se establece volúmen que permite hacer persistente la información almacenada.

Las principales características del contenedor incluyen:
- Sistema operativo [**Alpine 3.9**](1)
- Base de datos [**Postgress 11.2**](2)
- Parámetros configurables proporcionados mediante variables de entorno:
  - Usuario (`POSTGRES_USER`)
  - Contraseña (`POSTGRES_PASSWORD`)
  - Nombre de la base de datos (`POSTGRES_DB`)


[1]: https://www.alpinelinux.org/posts/Alpine-3.9.0-released.html
[2]: https://www.postgresql.org/docs/11/release-11-2.html