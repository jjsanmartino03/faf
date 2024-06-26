import face_recognition
import cv2
import numpy as np

# Cargar las imágenes de referencia y obtener sus codificaciones
known_face_encodings = []
known_face_names = []

# Ejemplo: Cargar rostros conocidos
known_face_1 = face_recognition.load_image_file("/home/julian/projects/vision/training/joe_biden/RTS2M37E_1.jpg")
known_face_encoding_1 = face_recognition.face_encodings(known_face_1)[0]
known_face_encodings.append(known_face_encoding_1)
known_face_names.append("Joe Biden")

known_face_2 = face_recognition.load_image_file("/home/julian/projects/vision/training/elon_musk/161871.jpg")
known_face_encoding_2 = face_recognition.face_encodings(known_face_2)[0]
known_face_encodings.append(known_face_encoding_2)
known_face_names.append("Elon Musk")

# Cargar la imagen en la que queremos buscar rostros
image_to_check = face_recognition.load_image_file("/home/julian/projects/vision/validation/elon_joe.jpeg")

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