from typing import Annotated, Optional
import typer
app = typer.Typer()

from pinsuggest.gallery import Gallery

# TODO: Found a way to not setup app
def setup_app():
    global gallery
    global albuns
    gallery = Gallery()
    albuns =  gallery.get_albuns()
    

setup_app()

@app.command()
def topics():
    print("Esse são os tópicos recomendados de hoje: \n")
    c = 1
    for album in albuns:
        print(f'[{c}] {album.topic.name}')
        c += 1
    print("\nDigite o comando 'images' + o número do tópico desejado: ")

@app.command()
def images(number_of_topic: int, number_of_images_to_get: Annotated[Optional[int], typer.Argument()] = None):
    current_album = albuns[number_of_topic - 1]
    if number_of_images_to_get:
        gallery.change_number_of_images(album=current_album, number_of_images_to_get=number_of_images_to_get)

    print("Sugerimos essas imagens para você.\n")
    current_album.get_images()
    c = 1
    for image in current_album.images:
        print(f'[{c}] {image.title}: {image.link_to}\n')
        c += 1


if __name__ == "__main__":
    app()