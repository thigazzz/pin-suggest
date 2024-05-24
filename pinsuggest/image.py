from dataclasses import dataclass, field

from pinsuggest.topic import Topic

@dataclass
class Image:
    id: int
    title: str
    link_to: str
    topic: Topic
    _is_favorited: bool = False

    def favorite(self):
        self._is_favorited = True
    def unfavorite(self):
        self._is_favorited = False

    def get_is_favorited(self):
        return self._is_favorited