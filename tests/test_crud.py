import caribou
import os

from src.crud.controllers import Controller
from src.crud.models import ImageModel, TopicModel
from src.crud.repository import SqliteImagesModelRepository, SqliteTopicsRepository
from src.pinsuggest.image import Image
from src.pinsuggest.topic import Topic

TEST_DATABASE_PATH = 'database/favorites.dev.db'
TEST_MIGRATIONS_PATH = 'database/migrations-dev'
TEST_DATABASE_VERSION = '20240606140216'

def open_database():
    os.system('caribou upgrade database/favorites.dev.db database/migrations-dev/.')
def close_database():
    os.system('caribou downgrade database/favorites.dev.db database/migrations-dev/. 0')


def test_favorite_an_image_with_exist_topic():
    """
    Test for favorite an image functionally. Pass through
    all layers: controller, model and repository; and all
    interactions

    >>> controller.favorite_image(image)
    1; Create a new data in database
    2. Return the image favorited
    """
    open_database()

    # ARRANGE
    mock_topic = Topic(id=1, name='topic_fake', link='link_to_topic_fake')
    mock_image_to_favorite = Image(id=None, title='name_fake1', link_to='src_fake', topic=mock_topic)
    assert_image = Image(id=1, title='name_fake1', link_to='src_fake', topic=mock_topic)

    topic_model = TopicModel(repository=SqliteTopicsRepository(database_path=TEST_DATABASE_PATH))
    image_model = ImageModel(image_repository=SqliteImagesModelRepository(database_path=TEST_DATABASE_PATH), topic_model=topic_model)
    controller = Controller(image_model=image_model)

    # ACT
    topic_model.create(mock_topic)
    added_image = controller.favorite_image(mock_image_to_favorite)
    added_image = controller.favorite_image(mock_image_to_favorite)

    # ASSERT
    try:
        assert added_image.title == assert_image.title
        assert added_image.link_to == assert_image.link_to
        assert added_image.topic.name == assert_image.topic.name
        assert added_image.topic.link == assert_image.topic.link
        assert len(topic_model.read()) == 1
    finally:
        close_database()

def test_favorite_an_image_with_no_exist_topic():
    """
    Test for favorite an image functionally. Pass through
    all layers: controller, model and repository; and all
    interactions

    >>> controller.favorite_image(image)
    1; Create a new data in database
    2. Return the image favorited
    """
    open_database()
    
    # ARRANGE
    mock_topic = Topic(id=1, name='topic_fake', link='link_to_topic_fake')
    mock_image_to_favorite = Image(id=None, title='name_fake1', link_to='src_fake', topic=mock_topic)
    assert_image = Image(id=1, title='name_fake1', link_to='src_fake', topic=mock_topic)

    topic_model = TopicModel(repository=SqliteTopicsRepository(database_path=TEST_DATABASE_PATH))
    image_model = ImageModel(image_repository=SqliteImagesModelRepository(database_path=TEST_DATABASE_PATH), topic_model=topic_model)
    controller = Controller(image_model=image_model)

    # ACT
    added_image = controller.favorite_image(mock_image_to_favorite)

    # ASSERT
    try:
        assert added_image.title == assert_image.title
        assert added_image.link_to == assert_image.link_to
        assert added_image.topic.name == assert_image.topic.name
        assert added_image.topic.link == assert_image.topic.link
    finally:
        close_database()