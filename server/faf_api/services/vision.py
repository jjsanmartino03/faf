import os.path
import pickle
from collections import Counter
from pathlib import Path
import cv2
import platform
import dlib
import numpy as np
from PIL import Image, ImageDraw,ImageFont

# if system is windows, then select custom model predictor
if platform.system == "Windows":
    model_path = os.path.join(os.path.dirname(__file__), 'shape_predictor_68_face_landmarks.dat')
    pose_predictor_68_point = dlib.shape_predictor(model_path)
import face_recognition

from faf_api.models import Players

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


class VisionService:
    encodings_location = Path("output/encodings.pkl")

    def __init__(self):
        Path("output").mkdir(exist_ok=True)

    def train_new_player_image(self, filepath: str, player_id: int):
        # recibe una imagen y la agrega al encoding
        """
        Loads images in the training directory and builds a dictionary of their
        names and encodings.
        """
        player_ids = []
        encodings = []

        if os.path.exists(self.encodings_location):
            with self.encodings_location.open(mode="rb") as f:
                player_id_encodings = pickle.load(f)
                player_ids = player_id_encodings["player_ids"]
                encodings = player_id_encodings["encodings"]

        image = face_recognition.load_image_file(filepath)

        face_locations = face_recognition.face_locations(image, model='hog')
        face_encodings = face_recognition.face_encodings(image, face_locations)

        for encoding in face_encodings:
            player_ids.append(player_id)
            encodings.append(encoding)

        player_id_encodings = {"player_ids": player_ids, "encodings": encodings}
        with self.encodings_location.open(mode="wb") as f:
            pickle.dump(player_id_encodings, f)
        return

    def recognize_players_in_image(self, image_location: str):
        # recibe una imagen y devuelve los jugadores reconocidos
        """
        Given an unknown image, get the locations and encodings of any faces and
        compares them against the known encodings to find potential matches.
        """
        with self.encodings_location.open(mode="rb") as f:
            loaded_encodings = pickle.load(f)

        input_image = face_recognition.load_image_file(image_location)

        input_face_locations = face_recognition.face_locations(
            input_image, model='hog'
        )
        input_face_encodings = face_recognition.face_encodings(
            input_image, input_face_locations
        )
        cv_image = cv2.cvtColor(input_image, cv2.COLOR_RGB2BGR)

        recognized_player_ids = []
        validation_ok = True
        for bounding_box, unknown_encoding in zip(
                input_face_locations, input_face_encodings
        ):
            player_id = self._recognize_face(unknown_encoding, loaded_encodings)

            if not player_id:
                cv_image = self._display_face(cv_image, bounding_box, "Desconocido", WHITE, BLACK)
                player_id = "Desconocido"
                recognized_player_ids.append(player_id)
                continue

            recognized_player_ids.append(player_id)
            player = Players.objects.get(id=player_id)

            if not player:
                validation_ok = False
                cv_image = self._display_face(cv_image, bounding_box, "Unknown", RED)
                continue

            print(player.name)
            print(player)

            if player and player.status == 0:
                validation_ok = False
                cv_image = self._display_face(cv_image, bounding_box, player.name, RED)
            else:
                cv_image = self._display_face(cv_image, bounding_box, player.name, GREEN)

        if len(recognized_player_ids) == 0:
            validation_ok = False

        cv2.imwrite(image_location, cv_image)

        return validation_ok

    def _recognize_face(self, unknown_encoding, loaded_encodings):
        """
        Given an unknown encoding and all known encodings, find the known
        encoding with the most matches.
        """

        boolean_matches = face_recognition.compare_faces(
            loaded_encodings["encodings"], unknown_encoding
        )

        votes = Counter(
            player_id
            for match, player_id in zip(boolean_matches, loaded_encodings["player_ids"])
            if match
        )
        if votes:
            return votes.most_common(1)[0][0]

    def _display_face(self, image, bounding_box, name, color, text_color=WHITE):
        """
        Draws bounding boxes around faces, a caption area, and text captions.
            """
        top, right, bottom, left = bounding_box
        image_height, image_width = image.shape[:2]

        # Calculate scale factor based on image dimensions
        scale_factor = image_height / 1500  # Adjust 1500 to a suitable base height

        # Adjust rectangle height and text size using the scale factor
        rectangle_height = int(35 * scale_factor)

        # Draw rectangle around the face
        cv2.rectangle(image, (left, top), (right, bottom), color, 2)

        # Draw filled rectangle for the name
        cv2.rectangle(image, (left, bottom - rectangle_height), (right, bottom), color, cv2.FILLED)

        # Use a font that supports special characters
        font_path = "fonts/Roboto-Medium.ttf"  # Ensure this path is correct
        font = ImageFont.truetype(font_path, int(30 * scale_factor))

        # Convert the image to PIL format
        pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(pil_image)

        # Put the name text
        draw.text((left + 6, bottom - rectangle_height), name, font=font, fill=text_color)

        # Convert the image back to OpenCV format
        image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

        return image
    def delete_player_from_model(self, player_id):
        # recibe un id de jugador y lo elimina del modelo
        """
        Deletes a player from the model
        """
        with self.encodings_location.open(mode="rb") as f:
            loaded_encodings = pickle.load(f)

        player_ids = loaded_encodings["player_ids"]
        encodings = loaded_encodings["encodings"]

        result_players = []
        result_encodings = []
        for i, player in enumerate(player_ids):
            if player != player_id:
                print(i, player, player_id)
                result_players.append(player)
                result_encodings.append(encodings[i])
                # player_ids.pop(i)
                # encodings.pop(i)

        player_id_encodings = {"player_ids": player_ids, "encodings": encodings}
        with self.encodings_location.open(mode="wb") as f:
            pickle.dump(player_id_encodings, f)
        return
