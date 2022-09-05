from PIL import Image, ImageDraw
from io import BytesIO

import splatnet2statink as sp

class Game:

    def __init__(self) -> None:
        pass

    def get_data(self, indice=0):
        data = sp.get_all(indice)
        return data

    def get_image_home(self):
        data = self.get_data()
        img_temp = data["image_gear"]
        scoreboard = Image.open(BytesIO(img_temp)).convert("RGB")
        scoreboard.save("image_home.png")
        
    def get_image_game(self, indice=0):
        data = self.get_data(indice=indice)
        img_temp = data["image_result"]
        result = Image.open(BytesIO(img_temp)).convert("RGB")
        result.save(f"image_results.png")

# partie = Game()
# img_home = partie.get_image_home()
# img_result = partie.get_image_game()

