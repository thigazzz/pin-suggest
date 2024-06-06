from dataclasses import dataclass

from src.pinsuggest.topic import Topic

@dataclass
class Image:
    id: int
    title: str
    link_to: str
    topic: Topic
    _is_favorited: bool = False

    def __repr__(self) -> str:
        return f'title: {self.title}, link: {self.link_to} \n'

    def favorite(self):
        self._is_favorited = True
    def unfavorite(self):
        self._is_favorited = False

    def get_is_favorited(self):
        return self._is_favorited