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

import requests
import os

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
        html = BeautifulSoup(self._scrap_site(), 'html.parser')
        # html_topics = html.find_all('div', class_='topic')
        html_topics = html.find_all('div', {"data-test-id": "today-tab-article"})
        _albuns = []
        for topic in html_topics:
            # topic_name = topic.find('div') #a > div > div > div > div > div > div > div h2
            topic_name = topic.select_one('a > div > div > div > div > div > div > div h2').text
            topic_link = topic.find('a')['href']

            _albuns.append(Album(Topic(name=topic_name, link=topic_link)))
        
        return _albuns
    
    def _scrap_site(self):
        if os.path.exists('cache/topics.html') == False:
            PINTEREST_URL = 'https://www.pinterest.com/today/'
            r = requests.get(PINTEREST_URL)
            with open('cache/topics.html', 'w') as f:
                f.write(r.text)

        with open('cache/topics.html', 'r') as f:
            return f.read()

    def get_albuns(self):
        return self.albuns

    def change_number_of_images(self, album, number_of_images_to_get):
        album.set_quantity_of_images(number_of_images_to_get)