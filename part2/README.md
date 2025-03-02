# HolbertonBnB Part2

## Descripción del Proyecto

Este proyecto es un clon de AirBnB desarrollado como parte del programa de Holberton School. El objetivo es construir un sistema escalable que permita la gestión de usuarios, reseñas, lugares y amenities, utilizando una arquitectura bien definida y aplicando principios de diseño de software.

## Estructura del Repositorio

El repositorio está organizado en los siguientes directorios y archivos principales:

- **models/**: Contiene la lógica del modelo de datos y las clases que representan las entidades del sistema.

  - `base_model.py`: Clase base que define atributos y métodos comunes.
  - `user.py`: Modelo de usuario.
  - `place.py`: Modelo de lugar.
  - `review.py`: Modelo de reseña.
  - `amenity.py`: Modelo de amenidades.

- **tests/**: Contiene los casos de prueba automatizados para validar la funcionalidad del sistema.

  - `test_review.py`: data validation para endpoints de clase review
  - `test_user.py`: data validation para endpoints de clase user
  - `test_place.py`: data validation para endpoints de clase place
  - `test_amenities.py`: data validation para endpoints de clase amenities

- **api/**: Implementación de la API RESTful para interactuar con el sistema.

  - `v1/`: Versión 1 de la API con controladores específicos.
  - `app.py`: Punto de entrada de la API.

- **web\_static/**: Contiene archivos HTML, CSS y JavaScript para la interfaz de usuario.

- **README.md**: Este archivo de documentación con una visión general del proyecto.

## Instalación y Configuración

### Prerrequisitos

Para ejecutar este proyecto, necesitarás tener instalado:

- Python 3
- Flask
- pip (administrador de paquetes de Python)

### Instalación de Dependencias

Ejecuta el siguiente comando en la raíz del proyecto para instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```

### Cómo Ejecutar la Aplicación

Para iniciar la API, ejecuta el siguiente comando:

```bash
python3 api/app.py
```

El servidor se ejecutará por defecto en `http://127.0.0.1:5000/`.

## Authors

@BruDosSant
@Rodrigoferrer
@feratholberton

Este proyecto está desarrollado como parte del currículo de Holberton School Uruguay.