from unittest.mock import MagicMock
from src.pinsuggest.image import Image
from src.pinsuggest.topic import Topic
from src.crud.controllers import Controller
from src.crud.models import SqliteTopicsModel, SqliteImagesModel

def test_convert_information_from_database_to_image_class():
    """
    Test to validate the creation of a element with data from database 
    communicable to rest of application. The way to make this is get
    the information from database and instantiate to a Image object.

    >>> instatiate_image()
    Image(id=any, title=any, link_to=any, topic=Topic('any', any'), _is_favorited=True)
    """
    mock_data_from_database = (1, 'any', 'any', 1) # id, name, link, topic
    assert_image = Image(id=1, title='any', link_to='any', topic=Topic(name='any', link='any'))
    assert_image._is_favorited = True
    mock_topics_model = SqliteTopicsModel()
    mock_topics_model.read_one = MagicMock(return_value=(1,'any','any'))
    controller = Controller(mock_topics_model, SqliteImagesModel())

    instatiated_image = controller.instatiate_image(mock_data_from_database)

    assert instatiated_image == assert_image

# TODO: Do test to facorite an imagem with no created topic and vice-versa
# TODO: Do test for unfavorite method

def test_bla():
    controller = Controller(SqliteTopicsModel(), SqliteImagesModel())
    image = controller.favorite_image(Image(id=None, title='COntroller', link_to='controller', topic=Topic(name='controller', link='controller')))
    print(image)
    print(image.get_is_favorited(), image.id)
    controller.unfavorite_image(image)