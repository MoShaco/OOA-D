from enum import Enum

class Wood(Enum):
    INDIAN_ROSEWOOD = "Indian Rosewood"
    BRAZILIAN_ROSEWOOD = "Brazilian Rosewood"
    MAHOGANY = "Mahogany"
    MAPLE = "Maple"
    COCOBOLO = "Cocobolo"
    CEDAR = "Cedar"
    ADIRONDACK = "Adirondack"
    ALDER = "Alder"
    SITKA = "Sitka"


    def __str__(self) -> str:
        return self.value

