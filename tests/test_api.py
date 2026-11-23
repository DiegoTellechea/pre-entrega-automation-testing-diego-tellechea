
import requests

from utils.logger import logger


def test_obtener_usuario(base_url, headers):
    try:
        logger.info("Iniciando prueba API: obtener usuario")

        url = f"{base_url}/users/2"

        logger.info(f"Enviando solicitud GET: {url}")
        response = requests.get(url, headers=headers)

        # NIVEL 1: STATUS CODE
        codigo = response.status_code
        assert codigo == 200
        logger.info(f"Status code validado: {codigo}")

        data = response.json()

        # NIVEL 2: HEADERS
        assert "application/json" in response.headers["Content-Type"]
        logger.info("Content-Type validado correctamente")

        # NIVEL 3: ESTRUCTURA
        assert isinstance(data, dict)
        assert "data" in data
        assert isinstance(data["data"], dict)

        assert "id" in data["data"]
        assert "email" in data["data"]
        assert "first_name" in data["data"]
        assert "last_name" in data["data"]
        logger.info("Estructura de respuesta validada correctamente")

        # NIVEL 4: CONTENIDO
        assert data["data"]["id"] == 2
        assert data["data"]["email"] == "janet.weaver@reqres.in"
        logger.info("Contenido de respuesta validado correctamente")

        # NIVEL 5: TIEMPO DE RESPUESTA
        tiempo = response.elapsed.total_seconds()
        assert tiempo < 2
        logger.info(f"Tiempo de respuesta: {tiempo:.3f} segundos")

        logger.info("Prueba API obtener usuario finalizada correctamente")

    except Exception:
        logger.exception("Error durante la prueba API: obtener usuario")
        raise


def test_crear_usuario(base_url, headers):
    try:
        logger.info("Iniciando prueba API: crear usuario")

        url = f"{base_url}/users/"

        usuario = {
            "email": "diego.tell@hotmail.com",
            "first_name": "diego",
            "last_name": "Tell",
            "job": "alumno"
        }

        logger.info(f"Enviando solicitud POST: {url}")
        response = requests.post(url, headers=headers, json=usuario)

        # NIVEL 1: STATUS CODE
        assert response.status_code == 201
        logger.info(f"Status code validado: {response.status_code}")

        # NIVEL 2: HEADERS
        assert "application/json" in response.headers["Content-Type"]
        logger.info("Content-Type validado correctamente")

        # NIVEL 3: ESTRUCTURA
        data = response.json()

        assert "id" in data
        assert "email" in data
        assert "first_name" in data
        assert "last_name" in data
        logger.info("Estructura de respuesta validada correctamente")

        # NIVEL 4: CONTENIDO
        assert data["email"] == usuario["email"]
        assert data["first_name"] == usuario["first_name"]
        logger.info("Contenido de respuesta validado correctamente")

        # NIVEL 5: TIEMPO DE RESPUESTA
        tiempo = response.elapsed.total_seconds()
        assert tiempo < 2
        logger.info(f"Tiempo de respuesta: {tiempo:.3f} segundos")

        logger.info("Prueba API crear usuario finalizada correctamente")

    except Exception:
        logger.exception("Error durante la prueba API: crear usuario")
        raise


def test_eliminar_usuario(base_url, headers):
    try:
        logger.info("Iniciando prueba API: eliminar usuario")

        url = f"{base_url}/users/2"

        logger.info(f"Enviando solicitud DELETE: {url}")
        response = requests.delete(url, headers=headers)

        # NIVEL 1: STATUS CODE
        assert response.status_code == 204
        logger.info(f"Status code validado: {response.status_code}")

        # NIVEL 2: HEADERS
        assert "Content-Type" not in response.headers
        logger.info("Ausencia de Content-Type validada")

        # NIVEL 3 y 4: ESTRUCTURA Y CONTENIDO
        assert len(response.content) == 0
        logger.info("Respuesta vacia validada correctamente")

        # NIVEL 5: TIEMPO DE RESPUESTA
        tiempo = response.elapsed.total_seconds()
        assert tiempo < 2
        logger.info(f"Tiempo de respuesta: {tiempo:.3f} segundos")

        logger.info("Prueba API eliminar usuario finalizada correctamente")

    except Exception:
        logger.exception("Error durante la prueba API: eliminar usuario")
        raise








 

