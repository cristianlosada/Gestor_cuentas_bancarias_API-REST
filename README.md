# Proyecto de Consulta de Saldo y Operaciones Bancarias

El objetivo principal de este proyecto es proporcionar una solución de software para la gestión de cuentas de ahorro. El sistema permite a los usuarios consultar el saldo de sus cuentas, crear nuevas cuentas, consignar dinero a sus cuentas y retirar dinero de ellas. La solución se implementa como una API RESTful, construida en Python con el framework Flask.

El uso de una API RESTful permite que la solución sea fácilmente escalable y adaptable a las necesidades futuras del negocio. Además, el sistema se puede integrar con otros sistemas de software mediante la utilización de una interfaz de programación de aplicaciones (API), lo que lo hace ideal para su uso en una amplia variedad de aplicaciones.

## Funcionalidades

- Consultar saldo de una cuenta
- Crear una cuenta de ahorros
- Consignar a una cuenta de ahorros
- Retirar dinero de una cuenta

## Tecnologías utilizadas

- Python 3.9
- Flask

## Instalación

Pasos para instalar y ejecutar el proyecto:

1. Clonar el repositorio
2. Instalar las dependencias: `py -m pip install -r requirements.txt`
3. Ejecutar el archivo app.py: `py ./src/app.py`

## Uso

- Consultar saldo: Hacer una petición GET a la ruta `/api/cuenta/saldo/<numero_cuenta>` donde `numero_cuenta` es el número de cuenta de la que se quiere consultar el saldo.
- Crear cuenta de ahorros: Hacer una petición POST a la ruta `/api/cuenta/crear` con los datos de la cuenta a crear en el cuerpo de la petición en formato JSON.
- Consignar a cuenta de ahorros: Hacer una petición POST a la ruta `/api/cuenta/consignar/<numero_cuenta>` con los datos de la cuenta y el valor a consignar en el cuerpo de la petición en formato JSON.
- Retirar de cuenta de ahorros: Hacer una petición POST a la ruta `/api/cuenta/retirar/<numero_cuenta>` con los datos de la cuenta y el valor a retirar en el cuerpo de la petición en formato JSON.

## Contribuir

1. Hacer un fork del repositorio
2. Crear una rama para trabajar en la nueva funcionalidad: `git checkout -b nueva-funcionalidad`
3. Hacer los cambios necesarios y hacer commit: `git commit -am "Agrega nueva funcionalidad"`
4. Hacer push a la rama creada: `git push origin nueva-funcionalidad`
5. Crear un pull request en GitHub

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.
