from src.crud.models import ImageModel
from src.pinsuggest.image import Image

class Controller:
    def __init__(self, image_model: ImageModel) -> None:
        self.image_model = image_model

    def favorite_image(self, image: Image):
        image_data = self.image_model.create(image)
        image_data.favorite()

        return image_data
    
    def unfavorite_image(self, image: Image):
        image.unfavorite()
        unfavorited_image = self.image_model.delete(image.id)
        return self.image_model.read()
