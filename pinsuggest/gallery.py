from bs4 import BeautifulSoup


from pinsuggest.album import Album
from pinsuggest.topic import Topic

fake_topic_HTML ="""
<html>
    <div>
        <div class="topic">
            <a class="link" href="link1"/>
            <div class="name">Topic1</div>
        </div>
        <div class="topic">
            <a class="link" href="link2"/>
            <div class="name">Topic2</div>
        </div>
        <div class="topic">
            <a class="link" href="link3"/>
            <div class="name">Topic3</div>
        </div>
    </div>
</html>
"""

class Gallery:
    """
    A set of albuns. Manager and generate albuns from scrapped Topic
    from Pinterest.
    """
    def __init__(self) -> None:
        self.pinterest_HTML = fake_topic_HTML
        self.albuns = self._set_albuns()
    
    def _set_albuns(self):
        """
        1 Extrair do Pinterest os topicos recomendados
        1.1 Instanciar os topicos
        2 Instanciar albuns com base nos topicos
        """
        html = BeautifulSoup(self.pinterest_HTML, 'html.parser')
        html_topics = html.find_all('div', class_='topic')
        _albuns = []
        for topic in html_topics:
            topic_name = topic.find('div')
            topic_link = topic.find('a')

            _albuns.append(Album(Topic(name=topic_name, link=topic_link)))
        
        return _albuns

    def get_albuns(self):
        return self.albuns

    def change_number_of_images(self, album, number_of_images_to_get):
        album.set_quantity_of_images(number_of_images_to_get)