# QA Automation Framework con Python

Framework de automatización de pruebas desarrollado como Trabajo Final Integrador del curso de QA Automation.

El proyecto combina pruebas automatizadas de interfaz de usuario (UI), pruebas de API y pruebas funcionales bajo el enfoque BDD, utilizando Python y distintas herramientas del ecosistema de testing.

El sitio utilizado para las pruebas de interfaz es **[SauceDemo](https://www.saucedemo.com/)** y para las pruebas de API se utiliza **[ReqRes](https://reqres.in/)**.

## Objetivos del proyecto

Desarrollar un framework de automatización organizado, reutilizable y extensible, aplicando buenas prácticas de testing y programación.

El proyecto incluye:

- Automatización de flujos de inicio de sesión.
- Validación del inventario y catálogo de productos.
- Agregado de productos al carrito y verificación de su contenido.
- Pruebas de API mediante métodos GET, POST y DELETE.
- Validación de códigos de estado, contenido JSON y tiempos de respuesta.
- Pruebas BDD utilizando Gherkin y Behave.
- Manejo de datos externos mediante archivos CSV y JSON.
- Implementación del patrón Page Object Model (POM).
- Registro de eventos y resultados mediante logging.
- Capturas de pantalla ante fallos en las pruebas.
- Generación de reportes HTML con Pytest.
- Integración continua mediante GitHub Actions.

## Tecnologías y herramientas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje de programación |
| Selenium WebDriver | Automatización de interfaz web |
| Pytest | Ejecución y organización de pruebas |
| Requests | Automatización de pruebas de API |
| Behave | Pruebas BDD |
| Gherkin | Descripción de escenarios |
| pytest-html | Generación de reportes HTML |
| pytest-check | Validaciones múltiples dentro de una prueba |
| pytest-rerunfailures | Reintentos de pruebas fallidas |
| Git | Control de versiones |
| GitHub | Repositorio y colaboración |
| GitHub Actions | Integración continua |
| Chrome | Navegador utilizado para las pruebas |

## Estructura del proyecto

```text
Preentrega/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── data/
│   ├── products.json
│   └── users.csv
│
├── features/
│   ├── steps/
│   │   └── login_steps.py
│   ├── environment.py
│   └── login.feature
│
├── logs/
│
├── pages/
│   ├── cart_page.py
│   ├── inventory_page.py
│   └── login_page.py
│
├── reports/
│   ├── screenshots/
│   └── reporte.html
│
├── tests/
│   ├── test_api.py
│   ├── test_cart.py
│   ├── test_inventory.py
│   └── test_login.py
│
├── utils/
│   ├── helpers.py
│   ├── logger.py
│   └── reader.py
│
├── .gitignore
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```

## Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar a la carpeta del proyecto:

```bash
cd Preentrega
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
```

Activarlo en Windows:

```bash
venv\Scripts\activate
```

### 3. Instalar las dependencias

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Ejecución de las pruebas

### Pruebas automatizadas con Pytest

Para ejecutar toda la suite:

```bash
python -m pytest -v
```

Para ejecutar un archivo específico:

```bash
python -m pytest tests/test_login.py -v
```

### Pruebas BDD con Behave

Para ejecutar los escenarios definidos en Gherkin:

```bash
python -m behave
```

## Reportes y registros

### Reporte HTML

Pytest genera un reporte HTML con los resultados de ejecución en:

```text
reports/reporte.html
```

El reporte permite consultar las pruebas ejecutadas y sus resultados.

### Capturas de pantalla

Cuando una prueba de interfaz falla, el framework puede generar una captura de pantalla para facilitar el análisis del error.

Las capturas se almacenan en:

```text
reports/screenshots/
```

### Logs

El framework utiliza el módulo `logging` de Python para registrar eventos durante la ejecución.

Los archivos de registro se almacenan en:

```text
logs/
```

## Integración continua – GitHub Actions

El proyecto incorpora un workflow de GitHub Actions ubicado en:

```text
.github/workflows/tests.yml
```

El workflow permite ejecutar automáticamente las pruebas cuando se realizan cambios en el repositorio o se genera un Pull Request hacia la rama principal.

Se ejecutan:

- Instalación de dependencias.
- Pruebas automatizadas con Pytest.
- Escenarios BDD con Behave.
- Publicación del reporte HTML como artefacto de la ejecución.

## Arquitectura y organización

El framework utiliza el patrón **Page Object Model (POM)** para separar la lógica de interacción con las páginas web de los casos de prueba.

- `pages/`: clases que representan las páginas de la aplicación.
- `tests/`: pruebas automatizadas de UI y API.
- `features/`: escenarios BDD y sus definiciones de pasos.
- `data/`: datos externos utilizados por las pruebas.
- `utils/`: funciones auxiliares, lectura de datos y logging.
- `reports/`: reportes y capturas de pantalla.
- `conftest.py`: configuración y fixtures compartidas de Pytest.

Esta organización facilita el mantenimiento, la reutilización de código y la incorporación de nuevos casos de prueba.

## Autor

Proyecto desarrollado como Trabajo Final Integrador del curso de QA Automation.