from random import randint
from src.crud.models import SqliteTopicsModel, SqliteImagesModel
from src.pinsuggest.topic import Topic
from src.pinsuggest.image import Image

class Controller:
    def __init__(self, topic_model: SqliteTopicsModel, image_model: SqliteImagesModel) -> None:
        self.topic_model = topic_model
        self.image_model = image_model

    def favorite_image(self, image: Image):
        topic = self.topic_model.read_one_by_name(image.topic.name) # id
        if topic == None:
            _id = randint(1,1000)
            topic_id = self.topic_model.create((_id, image.topic.name, image.topic.link))[0]
        else:
            topic_id = topic[0]

        _id = randint(1,1000)
        image_to_create = (_id, image.title, image.link_to, topic_id) # id, title, link, idTopic
        new_image = self.image_model.create(item=image_to_create)
        image = self.instatiate_image(new_image)
        return image
    
    def unfavorite_image(self, image: Image):
        """
        1. Pegar id
        2. Deletar
        3. Ler as imagens do banco
        4. Retornas as instancias
        """
        image_id = image.id
        self.image_model.delete(image_id)
        return self.list_all_images()


    def list_all_images(self):
        images_data = self.image_model.read()
        images = []
        for image_data in images_data:
            images.append(self.instatiate_image(image_data))
        return images

    def instatiate_image(self, data):
        topic_id = data[3]
        topic_data = self.topic_model.read_one(topic_id)
        topic = Topic(name=topic_data[1], link=topic_data[2])
        image = Image(id=data[0], title=data[1], link_to=data[2], topic=topic)
        image.favorite()
        return image
