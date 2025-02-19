from enum import Enum

class Type(Enum):
    ACOUSTIC = "acoustic"
    ELECTRIC = "electric"

    def __str__(self) -> str:
        return self.value
