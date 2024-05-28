import typer
app = typer.Typer()

from pinsuggest.gallery import Gallery

# TODO: Found a way to not setup app
def setup_app():
    gallery = Gallery()
    global albuns
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
def images(number_of_topic: int):
    print("Sugerimos essas imagens para você.\n")
    current_album = albuns[number_of_topic - 1]
    current_album.get_images()
    c = 1
    for image in current_album.images:
        print(f'[{c}] {image.title}: {image.link_to}\n')
        c += 1


if __name__ == "__main__":
    app()