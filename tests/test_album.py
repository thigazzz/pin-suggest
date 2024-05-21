from collections import namedtuple
from random import randint

from bs4 import BeautifulSoup

from fake import fake_pinterest_HTML

Image = namedtuple("Image", "id,title,link_to,topic")

class Topic: ...


class Album:
    """
    Visualization for imagens scrapped in Pinterest
    """
    def __init__(self, quantity_of_images=10) -> None:
        self.images = []
        self.quantity_of_images = quantity_of_images
        self.pinterest_HTML = ""

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

        for _ in range(0,self.quantity_of_images):
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
                        topic=Topic(),
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


def test_generate_list_with_different_images_from_each_other():
    """
    Test to ensure the diversity of images within a set.
    A set should not contain duplicate images.
    """
    mock_equal_images = [Image(id=1,title='title1',link_to='src1', topic=Topic()),Image(id=1,title='title2',link_to='src1', topic=Topic()), Image(id=1,title='title1',link_to='src2', topic=Topic())]
    album = Album(quantity_of_images=3)
    album.pinterest_HTML = fake_pinterest_HTML

    image_list = album.get_images()

    assert album.there_are_no_repeated_images(mock_equal_images) == False # add this assert to a new test case
    assert album.there_are_no_repeated_images(image_list) == True

def test_generate_list_of_different_images_between_one_call_and_another():
    """
    Test to ensure that subsequent sets of images do not contain duplicates from previous sets.
    """
    album = Album(quantity_of_images=3)
    album.pinterest_HTML = fake_pinterest_HTML

    old_list = album.get_images()
    new_list = album.get_images()

    old_list = [item.link_to for item in old_list]
    new_list = [item.link_to for item in new_list]

    assert new_list != old_list

def test_get_images_for_specified_quantity():
    """
    Test to validate that the number of images returned corresponds to the specified quantity.
    By default, the quantity is 10 images per call.

    >>> get_images()
    [Image1, Image2, Image3, Image4, Image5]
    # The quantity, in this case, is 5 images per call
    """
    album = Album(quantity_of_images=5)
    album.pinterest_HTML = fake_pinterest_HTML

    images_list = album.get_images()

    assert len(images_list) == 5
    for image in images_list:
        assert type(image) == Image

def test_detect_repeated_images_between_older_and_newer_images():
    """
    Test to detect if a new list of images does contain any images from an old list.
    If the new list has any images from the old list, the validation should 
    fail and a new set of images should be fetched.

    >>> album.get_images()
    [image1, image2, image3]

    >>> album.get_images()
    [image4, image2, image5]

    >>> album.is_different)images(new_image_list)
    False # is not different, have a equal image
    # [image1, image2, image3] == [image4, image2, image5] image2 is same in both
    """
    album = Album()
    old_image_list = [
        Image(id=randint(1, 100), title="name", link_to="src1", topic=Topic()),
        Image(id=randint(1, 100), title="name", link_to="src2", topic=Topic()),
        Image(id=randint(1, 100), title="name", link_to="src3", topic=Topic()),
    ]
    new_image_list = [
        Image(id=randint(1, 100), title="name", link_to="src4", topic=Topic()),
        Image(id=randint(1, 100), title="name", link_to="src2", topic=Topic()),
        Image(id=randint(1, 100), title="name", link_to="src5", topic=Topic()),
    ]

    is_diff_image_list = album.has_different_images_comparing_another_list(old_image_list, new_image_list)

    assert is_diff_image_list == False
