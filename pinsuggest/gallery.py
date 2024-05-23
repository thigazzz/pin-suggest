from bs4 import BeautifulSoup

fake_pinterest_HTML = """
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
from pinsuggest.album import Album
from pinsuggest.topic import Topic

class Gallery:
    """
    A set of albuns. Manager and generate albuns from scrapped Topic
    from Pinterest.
    """
    def __init__(self) -> None:
        self.albuns = self._set_albuns()
    
    def _set_albuns(self):
        """
        1 Extrair do Pinterest os topicos recomendados
        1.1 Instanciar os topicos
        2 Instanciar albuns com base nos topicos
        """
        html = BeautifulSoup(fake_pinterest_HTML, 'html.parser')
        html_topics = html.find_all('div', class_='topic')
        _albuns = []
        for topic in html_topics:
            topic_name = topic.find('div')
            topic_link = topic.find('a')

            _albuns.append(Album(Topic(name=topic_name, link=topic_link)))

    def get_albuns(self):
        return self.albuns