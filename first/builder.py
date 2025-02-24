from enum import Enum

class Builder(Enum):
    FENDER = "Fender"
    MARTIN = "Martin"
    GIBSON = "Gibson"
    COLLINGS = "Collings"
    OLSON = "Olson" 
    RYAN = "Ryan"
    PRS = "Prs" 
    ANY = "Any"

    def __str__(self) -> str:
        return self.value