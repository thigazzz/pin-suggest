from random import randint

from src.pinsuggest.album import Album
from src.pinsuggest.topic import Topic
from src.pinsuggest.image import Image


# TODO: Test to validate when the number of images 
# to get is greater of images getted
# TODO: Create a fixture to repetead code

def test_generate_list_with_different_images_from_each_other():
    """
    Test to ensure the diversity of images within a set.
    A set should not contain duplicate images.
    """
    mock_equal_images = [
        Image(
            id=1, title="title1", link_to="src1", topic=Topic(name="topic1", link="any")
        ),
        Image(
            id=1, title="title2", link_to="src1", topic=Topic(name="topic1", link="any")
        ),
        Image(
            id=1, title="title1", link_to="src2", topic=Topic(name="topic1", link="any")
        ),
    ]
    album = Album(topic=Topic(name="topic1", link="any"), quantity_of_images=3)

    image_list = album.get_images()

    assert (
        album._Album__there_are_no_repeated_images(mock_equal_images) == False
    )  # add this assert to a new test case
    assert album._Album__there_are_no_repeated_images(image_list) == True


def test_generate_list_of_different_images_between_one_call_and_another():
    """
    Test to ensure that subsequent sets of images do not contain duplicates from previous sets.
    """
    album = Album(topic=Topic(name="topic1", link="any"), quantity_of_images=3)

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
    album = Album(topic=Topic(name="topic1", link="any"), quantity_of_images=5)

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
    album = Album(topic=Topic(name="topic1", link="any"))
    old_image_list = [
        Image(id=randint(1, 100), title="name", link_to="src1", topic=Topic(name="topic1", link="any")),
        Image(id=randint(1, 100), title="name", link_to="src2", topic=Topic(name="topic1", link="any")),
        Image(id=randint(1, 100), title="name", link_to="src3", topic=Topic(name="topic1", link="any")),
    ]
    new_image_list = [
        Image(id=randint(1, 100), title="name", link_to="src4", topic=Topic(name="topic1", link="any")),
        Image(id=randint(1, 100), title="name", link_to="src2", topic=Topic(name="topic1", link="any")),
        Image(id=randint(1, 100), title="name", link_to="src5", topic=Topic(name="topic1", link="any")),
    ]

    is_diff_image_list = album._Album__has_different_images_comparing_another_list(
        old_image_list, new_image_list
    )

    assert is_diff_image_list == False

def test_favorite_and_image():
    album = Album(topic=Topic(name="topic1", link="any"), quantity_of_images=5)

    images = album.get_images()
    album.favorite_image(images[0])
    
    assert images[0].get_is_favorited() == True

def test_not_favorite_a_always_favorited_image():
    album = Album(topic=Topic(name="topic1", link="any"), quantity_of_images=5)

    images = album.get_images()
    album.favorite_image(images[0])
    
    assert album.favorite_image(images[0]) == None

def test_unfavorite_and_image():
    album = Album(topic=Topic(name="topic1", link="any"), quantity_of_images=5)

    images = album.get_images()
    album.favorite_image(images[0])
    album.unfavorite_image(images[0])
    
    assert images[0].get_is_favorited() == False
