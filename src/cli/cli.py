from class_cli import CLI

cli = CLI()

from src.crud.repository import SqliteImagesModelRepository, SqliteTopicsRepository
from src.crud.controllers import Controller
from src.crud.models import ImageModel, TopicModel

DATABASE_PATH = 'database/favorites.db'


@cli.Program()
class Program:
    def __init__(self) -> None:
        topic_model = TopicModel(repository=SqliteTopicsRepository(database_path=DATABASE_PATH))
        image_model = ImageModel(image_repository=SqliteImagesModelRepository(database_path=DATABASE_PATH), topic_model=topic_model)
        self.controller = Controller(image_model=image_model)
        self.showed_favorited_images = False

    @cli.Operation()
    def show_topics(self):
        print("Esse são os tópicos recomendados de hoje: \n")
        c = 1
        for topic in self.controller.show_topics():
            print(f'[{c}] {topic}')
            c += 1
        print("\nDigite o comando 'images' + o número do tópico desejado: ")
        
    
    @cli.Operation()
    def images(self, number_of_topic, number_of_images_to_get):
        print("Sugerimos essas imagens para você.\n") ## Tratar argumentos opcional
        c = 1
        for image in self.controller.show_images(int(number_of_topic), int(number_of_images_to_get)):
            print(f'[{c}] {image.title}: {image.link_to}\n')
            c += 1

    @cli.Operation()
    def favorite(self, number_of_image):
        favorited_image = self.controller.favorite(image=int(number_of_image))
        print(f"Imagem: {favorited_image.title} favoritada!")

    @cli.Operation()
    def unfavorite(self, image):
        if self.showed_favorited_images == False:
            print("Veja primeiro quais imagens estão favoritadas!")
            return
        self.controller.unfavorite(image=int(image))
        print("Imagem desfavoritada!")
        self.showed_favorited_images = False

    @cli.Operation()
    def favorited(self):
        favorited_images = self.controller.list_all_favorited_images()
        print('Essas são as imagens favoritadas')
        c = 1
        for f_image in favorited_images:
            print(f"[{c}] - {f_image.title}")
            c += 1
        self.showed_favorited_images = True

        
    
    
if __name__ == '__main__':
    Program().CLI.main()