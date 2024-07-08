from src.pinsuggest.gallery import Gallery
from src.crud.models import ImageModel
from src.pinsuggest.image import Image

class Controller:
    def __init__(self, image_model: ImageModel) -> None:
        self.image_model = image_model
        self.gallery = Gallery()
        self.albuns = self.gallery.get_albuns()
        self.current_album = None

    def show_topics(self):
        topics = []
        for album in self.albuns:
            topics.append(album.topic.name)
        return topics
    
    def show_images(self, number_of_topic, number_of_images_to_get):
        self.current_album = self.albuns[number_of_topic - 1]

        if number_of_images_to_get:
            self.gallery.change_number_of_images(album=self.current_album, number_of_images_to_get=number_of_images_to_get)
        
        return self.current_album.get_images()

    def favorite(self, image: int): # TODO: FIX BUG, Not same picutures shows to favorite
        images = self.current_album.get_images()
        current_image = images[image - 1]
        return self.favorite_image(current_image)
    
    def unfavorite(self, image: int):
        current_image = self.image_model.read()[image - 1]
        return self.unfavorite_image(current_image)

    def favorite_image(self, image: Image):
        image_data = self.image_model.create(image)
        image_data.favorite()

        return image_data
    
    def unfavorite_image(self, image: Image):
        image.unfavorite()
        unfavorited_image = self.image_model.delete(image.id)
        return self.image_model.read()
    
    def list_all_favorited_images(self):
        return self.image_model.read()
