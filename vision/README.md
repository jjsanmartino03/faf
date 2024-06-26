# Reconocimiento Facial

## Elección de la tecnología a utilizar

Se realizo una búsqueda de las distintas librerías de reconocimiento facial disponibles aptas para utilizar en Python,
así encontramos que la librería `face_recognition` era una de las más utilizadas debido a su eficiencia, accesibilidad y
facilidad de uso.
Luego utilizamos la herramienta "ChatGPT" para realizar una prueba rápida de funcionamiento de esta librería, de ahí
obtuvimos las siguientes líneas de código, en el cual también se utiliza la librería "opencv" para el manejo y edición
de las imágenes.

# Código de prueba:

   ```python
    import face_recognition
    import cv2
    import numpy as np

    # Cargar las imágenes de referencia y obtener sus codificaciones
    known_face_encodings = []
    known_face_names = []

    # Ejemplo: Cargar rostros conocidos
    known_face_1 = face_recognition.load_image_file("ruta_a_tu_imagen_de_referencia_1.jpg")
    known_face_encoding_1 = face_recognition.face_encodings(known_face_1)[0]
    known_face_encodings.append(known_face_encoding_1)
    known_face_names.append("Nombre de la Persona 1")

    known_face_2 = face_recognition.load_image_file("ruta_a_tu_imagen_de_referencia_2.jpg")
    known_face_encoding_2 = face_recognition.face_encodings(known_face_2)[0]
    known_face_encodings.append(known_face_encoding_2)
    known_face_names.append("Nombre de la Persona 2")

    # Cargar la imagen en la que queremos buscar rostros
    image_to_check = face_recognition.load_image_file("ruta_a_tu_imagen_a_verificar.jpg")

    # Encontrar todas las ubicaciones de rostros y sus codificaciones en la imagen
    face_locations = face_recognition.face_locations(image_to_check)
    face_encodings = face_recognition.face_encodings(image_to_check, face_locations)

    # Convertir la imagen a color (para OpenCV)
    image_to_check = cv2.cvtColor(image_to_check, cv2.COLOR_RGB2BGR)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # Comparar el rostro con los rostros conocidos
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Desconocido"

    # Usar el rostro conocido con la menor distancia
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]

    # Dibujar un rectángulo alrededor del rostro
    cv2.rectangle(image_to_check, (left, top), (right, bottom), (0, 255, 0), 2)

    # Colocar el nombre debajo del rostro
    cv2.rectangle(image_to_check, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(image_to_check, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Mostrar la imagen con las anotaciones
    cv2.imshow("Imagen", image_to_check)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

**Con esta prueba pudimos comprobar el correcto funcionamiento de la librería de reconocimiento facial**

# Imágenes de referencia:

![7ec61a7a-c5e0-4db9-a732-1b9052919098](https://github.com/jjsanmartino03/faf/assets/114831273/d2e597c1-83e0-40b4-be6a-19f9b34a77cb)
![e9bd2708-51a4-42d9-8f6d-e803e7f8e74b](https://github.com/jjsanmartino03/faf/assets/114831273/bf8c0438-ab12-4ab2-a69c-2aca4e8c16e1)

# Imagen a verificar:

![51e7dc63-203e-4e2f-9e51-a6e4f637be21](https://github.com/jjsanmartino03/faf/assets/114831273/da5ac2f2-0f7f-43c0-9439-62fa8291c6b8)

# Resultado:

![501fd3d0-4cd0-4421-827d-c1de877b54ac](https://github.com/jjsanmartino03/faf/assets/114831273/8df745fa-f3e0-4652-9cf0-13c6f934954a)

# Comentarios extra:

- Se pueden cargar varias imágenes de rostros y guardar sus codificaciones en formato ".dat".
- Se pueden cargar más de una imagen de referencia para una misma persona.
- Se pueden reconocer múltiples rostros/personas en una misma imagen.

## Instalación de la herramienta de visión
Prerrequisitos: Tener instalado Python 3.7 o superior y `virtualenv`

Pasos:
1. Clonar el repositorio.
2. Crear un entorno virtual: `virtualenv venv`
3. Activar el entorno virtual: `source venv/bin/activate`
4. Instalar las dependencias: `pip install -r requirements.txt`
5. Ejecutar el script: `python proof-of-concept/poc.py`


