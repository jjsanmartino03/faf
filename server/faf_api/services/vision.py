import os.path
import pickle
from collections import Counter
from pathlib import Path
# import face_recognition
import random

from faf_api.models import Players


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

        # image = face_recognition.load_image_file(filepath)

        # face_locations = face_recognition.face_locations(image, model='hog')
        # face_encodings = face_recognition.face_encodings(image, face_locations)

        # for encoding in face_encodings:
        #    player_ids.append(player_id)
        #    encodings.append(encoding)

        # player_id_encodings = {"player_ids": player_ids, "encodings": encodings}
        # with self.encodings_location.open(mode="wb") as f:
        #     pickle.dump(player_id_encodings, f)
        return

    def recognize_players_in_image(self, image_location: str):
        # recibe una imagen y devuelve los jugadores reconocidos
        """
        Given an unknown image, get the locations and encodings of any faces and
        compares them against the known encodings to find potential matches.
        """
        # with self.encodings_location.open(mode="rb") as f:
        #     loaded_encodings = pickle.load(f)
        #
        # input_image = face_recognition.load_image_file(image_location)
        #
        # input_face_locations = face_recognition.face_locations(
        #     input_image, model='hog'
        # )
        # input_face_encodings = face_recognition.face_encodings(
        #     input_image, input_face_locations
        # )
        #
        # # pillow_image = Image.fromarray(input_image)
        # # draw = ImageDraw.Draw(pillow_image)
        #
        # recognized_player_ids = []
        # for bounding_box, unknown_encoding in zip(
        #         input_face_locations, input_face_encodings
        # ):
        #     player_id = self._recognize_face(unknown_encoding, loaded_encodings)
        #
        #     if not player_id:
        #         player_id = "Unknown"
        #
        #     recognized_player_ids.append(player_id)
        #
        # for player_id in recognized_player_ids:
        #     if player_id == "Unknown":
        #         return False
        #
        #     player = Players.objects.get(id=player_id)
        #     if not player or player.status == 0:
        #         return False
        #
        # return True
        return random.choice([True, False])

    def _recognize_face(self, unknown_encoding, loaded_encodings):
        """
        Given an unknown encoding and all known encodings, find the known
        encoding with the most matches.
        """

        # boolean_matches = face_recognition.compare_faces(
        #     loaded_encodings["encodings"], unknown_encoding
        # )
        #
        # votes = Counter(
        #     player_id
        #     for match, player_id in zip(boolean_matches, loaded_encodings["player_ids"])
        #     if match
        # )
        # if votes:
        #     return votes.most_common(1)[0][0]
