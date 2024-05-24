from dataclasses import dataclass

@dataclass
class Topic:
    name: str
    link: str

    def __str__(self) -> str:
        return f'{self.name}'