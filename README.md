Para construir la imagen de Docker se usa el siguiente comando:
    docker build --tag nombre-imagen .

    -ejemplo: docker build --tag tarea2-flask .

Para poder ejecutar esa imagen de Docker en un contenedor se usa el siguiente comando:
    docker run -p puerto_local:puerto_contenedor nombre-imagen

    -ejemplo: docker run -p 8080:5000 tarea2-flask

Para poder ejecutar el contenedor de forma detach se usa el siguiente comando:
    docker run -d -p 8080:5000 tarea2-flask


Abrir un browser y acceder a: http://localhost:puerto_local
    -ejemplo: http://localhost:8080


---------------------------------------------------
Para ejecutar solo la app en flask se usa el siguiente comando
    python app.py

Despues se accede a: http://127.0.0.1:5000
