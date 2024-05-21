from collections import namedtuple
from bs4 import BeautifulSoup


fake_pinterest_HTML = """"
<html>
    <div>
        <div class='image'>
            <span id='name'>Image 1</span>
            <span id='src'>Src 1</span>
        </div>
        <div class='image'>
            <span id='name'>Image 2</span>
            <span id='src'>Src 2</span>
        </div>
        <div class='image'>
            <span id='name'>Image 3</span>
            <span id='src'>Src 3</span>
        </div>
        <div class='image'>
            <span id='name'>Image 4</span>
            <span id='src'>Src 4</span>
        </div>
        <div class='image'>
            <span id='name'>Image 5</span>
            <span id='src'>Src 5</span>
        </div>
        <div class='image'>
            <span id='name'>Image 6</span>
            <span id='src'>Src 6</span>
        </div>
    </div>
</html>
"""


Image = namedtuple("Image", "id,title,link_to,topic")
from random import randint, shuffle


class Topic: ...


class Album:
    def __init__(self, quantity_of_images=10) -> None:
        self.image_list = []
        self.quantity_of_images = quantity_of_images
        self.pinterest_HTML = ""

    def get_images(self):
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
                
                if self.have_same_itens(image_list) == False and self.is_different_image_list(image_list, self.image_list):
                    break
                else:
                    indexes_of_images.append(random_index)
                    image_list.pop()



        self.image_list = image_list
        return self.image_list

    def have_same_itens(self, list):
        if len(list) < 2:
            return False
        for i in range(0, len(list)):
            for l in range(i + 1, len(list)):
               if list[i].link_to == list[l].link_to:
                   return True

        return False
    
    def is_different_image_list(self, new_images, old_images):
        for new_image in new_images:
            for old_image in old_images:
                if new_image.link_to == old_image.link_to:
                    return False
        return True

def test_generate_a_list_with_differets_inner_images():
    """
    Test to ensure the diversity of images in a set. A set
    not able to have equal images.
    """
    mock_equal_images = [Image(id=1,title='title1',link_to='src1', topic=Topic()),Image(id=1,title='title2',link_to='src1', topic=Topic()), Image(id=1,title='title1',link_to='src2', topic=Topic())]
    album = Album(quantity_of_images=3)
    album.pinterest_HTML = fake_pinterest_HTML

    image_list = album.get_images()

    assert album.have_same_itens(mock_equal_images) == True # add this assert to a new test case
    assert album.have_same_itens(image_list) == False

def test_return_a_different_set_of_images_between_two_calls():
    """
    Test to ensure which the next set of images not have equal images
    from the older.
    """
    album = Album(quantity_of_images=3)
    album.pinterest_HTML = fake_pinterest_HTML

    old_list = album.get_images()
    new_list = album.get_images()

    old_list = [item.link_to for item in old_list]
    new_list = [item.link_to for item in new_list]

    assert new_list != old_list

def test_get_images_for_setted_quantity():
    """
    Test to validate whether the number of images returned
    corresponds to the number passed to the function 'get_images'.
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

def test_verify_repetead_images_in_image_list():
    """
    Test to validate the equality of a old and new image list generated,
    If the new list have a same image of older, the validation returns
    False and a new get images process is started.

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

    is_diff_image_list = album.is_different_image_list(old_image_list, new_image_list)

    assert is_diff_image_list == False
