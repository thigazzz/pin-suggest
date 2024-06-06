from dataclasses import dataclass

@dataclass
class Topic:
    id: int | None
    name: str
    link: str

    def __str__(self) -> str:
        return f'{self.name}'