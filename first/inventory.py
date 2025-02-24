from guitar import Guitar
from guitar_spec import GuitarSpec
from typing import Optional
from type import Type
from builder import Builder
from wood import Wood


class Inventory:
    def __init__(self) -> None:
        self._guitars: list[Guitar] = []
    
    @property
    def guitars(self) -> list[Guitar]:
        return self._guitars
    
    def add_guitar(self, serial_number: str, price: float, builder: Builder, model: str, type: Type, back_wood: Wood, top_wood: Wood, num_strings: int) -> None:
        guitar: Guitar = Guitar(
            serial_number=serial_number, 
            price=price, builder=builder, 
            model=model, 
            type=type, 
            back_wood=back_wood, 
            top_wood=top_wood,
            num_strings=num_strings
            )
        
        self.guitars.append(guitar)

    def get_guitar(self, serial_number: str) -> Optional['Guitar']:
        for guitar in self.guitars:
            if guitar.serial_number == serial_number:
                return guitar
        return None
    
    def search(self, searching_guitar: GuitarSpec) -> list[Guitar]:
        """ Compare builder, model, type, back_wood, top_wood"""
        matching_guitars: list[Guitar] = []
        for guitar in self.guitars:
            if guitar.spec.match(searching_guitar):
                matching_guitars.append(guitar)
        return matching_guitars