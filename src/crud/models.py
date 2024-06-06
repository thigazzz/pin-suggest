from random import randint
from typing import Any

from src.pinsuggest.image import Image
from src.pinsuggest.topic import Topic
from src.crud.repository import Database

def make_id():
    return randint(1,1000)

class TopicModel(Database):
    def __init__(self, repository) -> None:
        self.repository = repository

    def get_topic_id(self, topic) -> int:
        """
        Retornar id do topico. Se topico não existir, criar um
        """
        _topic = self.repository.read_one_by_name(topic.name)
        if _topic == None:
            print("AAAAAAAAAAAA")
            return self.create(topic).id
        _topic = self.__make_topic(_topic)
        return _topic.id
    
    def __make_topic(self, data):
        return  Topic(id=data[0], name=data[1], link=data[2])
    
    def create(self, item: Topic) -> Topic:
        return self.__make_topic(self.repository.create((make_id(), item.name, item.link)))
        
    def read(self) -> list[Topic]:
        topics_data = self.repository.read()
        topics = []
        for topic_data in topics_data:
            topics.append(self.__make_topic(topic_data))
        return topics
    def read_one(self, id, by=False) -> Topic:
        if by:
            return self.__make_topic(self.repository.read_one_by_name(id))
        return self.__make_topic(self.repository.read_one(id))
    def update(self, item: Topic, id) -> Topic:
        return self.__make_topic(self.repository.update((item.name, item.link), id))
    def delete(self, id) -> None:
        return self.repository.delete(id)
class ImageModel(Database):
    def __init__(self, image_repository, topic_model: TopicModel) -> None:
        self.repository = image_repository
        self.topic_model = topic_model

    def __make_image(self, data) -> Image:
        return Image(id=data[0], title=data[1], link_to=data[2], topic=self.topic_model.read_one(data[3]))

    def create(self, item: Image) -> Image:
        image_to_create = (make_id(), item.title, item.link_to, self.topic_model.get_topic_id(item.topic))
        return self.__make_image(self.repository.create(item=image_to_create))
    
    def read(self) -> list[Image]:
        images_data = self.repository.read()
        images = []
        for image_data in images_data:
            images.append(self.__make_image(image_data))
        return images
    def read_one(self, id) -> Image:
        return self.__make_image(self.repository.read_one(id))
    def delete(self, id) -> None:
        return self.repository.delete(id)
    def update(self, item, id) -> Any:
        ...
    