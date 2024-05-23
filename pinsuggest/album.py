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
        self.pinterest_HTML = ""
        self.topic = topic

    def get_images(self):
        """
        Scraps and return a structured list of images different between each other
        and differents comparing with a older list.
        Because of this behavior, the performance could be bad, because
        the process continue until a complety new list is generated.
        
        """
        soup = BeautifulSoup(self.pinterest_HTML, "html.parser")

        images = soup.find_all(class_="image")
        image_list = []
        indexes_of_images = []

        for _ in range(0,self._quantity_of_images):
            while True:
                random_index = randint(0, len(images) - 1)
                if random_index in indexes_of_images:
                    random_index = randint(0, len(images) - 1)

                image_name = images[random_index].find(id="name")
                image_src = images[random_index].find(id="src")
                image_list.append(
                    Image(
                        id=randint(1, 100),
                        title=image_name,
                        link_to=image_src,
                        topic=self.topic,
                    )
                )
                
                if self.there_are_no_repeated_images(image_list) and self.has_different_images_comparing_another_list(image_list, self.images):
                    break
                else:
                    indexes_of_images.append(random_index)
                    image_list.pop()



        self.images = image_list
        return self.images

    def there_are_no_repeated_images(self, list):
        if len(list) < 2:
            return True
        for i in range(0, len(list)):
            for l in range(i + 1, len(list)):
               if list[i].link_to == list[l].link_to:
                   return False

        return True
    
    def has_different_images_comparing_another_list(self, new_images, old_images):
        for new_image in new_images:
            for old_image in old_images:
                if new_image.link_to == old_image.link_to:
                    return False
        return True
    
    def set_quantity_of_images(self, number):
        self._quantity_of_images = number