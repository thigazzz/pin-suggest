import os
import requests
from typing import Any
from random import randint

from bs4 import BeautifulSoup

from pinsuggest.image import Image

class Album:
    """
    Visualization for imagens scrapped in Pinterest
    """
    def __init__(self, topic, quantity_of_images=10) -> None:
        self.images = []
        self._quantity_of_images = quantity_of_images
        self.topic = topic
        self.url = 'https://br.pinterest.com' + self.topic.link
    
    def __repr__(self) -> str:
        return f'Album(topic={self.topic}, images={self.images}, quantity_of_images={self._quantity_of_images})\n'

    def get_images(self):
        """
        Scraps and return a structured list of images different between each other
        and differents comparing with a older list.
        Because of this behavior, the performance could be bad, because
        the process continue until a complety new list is generated.
        
        """
        soup = BeautifulSoup(self._scrap_site(), "html.parser")
        images = soup.find_all('div', {"data-test-id": "pin-visual-wrapper"})

        self.images = self.__generate_the_list_of_images(images=images)
        return self.images

    def __generate_the_list_of_images(self, images):
        indexes_of_images = []
        image_list = []
        for _ in range(0,self._quantity_of_images):
            while True:
                random_index = self.__generate_random_index(index_already_generated=indexes_of_images, maximum_range=len(images) - 1)

                image_list.append(self.__make_image(image_element=images[random_index]))
                
                if self.__is_unique_image(image_list=image_list):
                    break
                else:
                    indexes_of_images.append(random_index)
                    image_list.pop()

        return image_list
    
    def __is_unique_image(self, image_list):
        if self.__there_are_no_repeated_images(image_list) and self.__has_different_images_comparing_another_list(image_list, self.images):
            return True

    def __generate_random_index(self, index_already_generated, maximum_range):
        random_index = randint(0, maximum_range)
        if random_index in index_already_generated:
            return self.__generate_random_index(index_already_generated, maximum_range)
        return random_index
    
    def __make_image(self, image_element):
        informations = self.__scrap_image_information(element=image_element)
        return Image(
                randint(1, 100),
                informations[0],
                informations[1],
                self.topic,
            )

    def __scrap_image_information(self, element):
        image_element = element.find('img')
        image_name = image_element['alt']
        image_src = image_element['src']
        return (image_name, image_src)

    def __there_are_no_repeated_images(self, list):
        if self.__is_list_has_one_element(list):
            return True

        return self.__is_list_have_repetead_elements(list)
    
    def __is_list_has_one_element(self, list: list[Any]) -> bool:
        if len(list) < 2:
            return True
        return False
    
    def __is_list_have_repetead_elements(self, list):
        for current_element in range(0, len(list)):
            for next_element in range(current_element + 1, len(list)):
               if list[current_element].link_to == list[next_element].link_to:
                   return False
        return True
    
    def __has_different_images_comparing_another_list(self, new_images, old_images):
        for new_image in new_images:
            for old_image in old_images:
                if new_image.link_to == old_image.link_to:
                    return False
        return True
    
    def set_quantity_of_images(self, number):
        self._quantity_of_images = number

    def favorite_image(self, image):
        if image.get_is_favorited() == True:
            return None
        image.favorite()

    def unfavorite_image(self, image):
        if image.get_is_favorited() == False:
            return None
        image.unfavorite()
    
    def _scrap_site(self): # TODO: Move to a Scrapper Class
        if os.path.exists(f'cache/images-{self.topic.name}.html') == False:
            r = requests.get(self.url)
            with open(f'cache/images-{self.topic.name}.html', 'w') as f:
                f.write(r.text)

        with open(f'cache/images-{self.topic.name}.html', 'r') as f:
            return f.read()