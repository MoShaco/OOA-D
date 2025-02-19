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
    
    def add_guitar(self, serial_number: str, price: float, builder: Builder, model: str, type: Type, back_wood: Wood, top_wood: Wood) -> None:
        guitar: Guitar = Guitar(
            serial_number=serial_number, 
            price=price, builder=builder, 
            model=model, 
            type=type, 
            back_wood=back_wood, 
            top_wood=top_wood)
        
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
            guitar_spec: GuitarSpec = guitar.spec
            if searching_guitar.builder and searching_guitar.builder != guitar_spec.builder:
                continue
            if searching_guitar.model and searching_guitar.model.lower() != guitar_spec.model.lower():
                continue
            if searching_guitar.type and searching_guitar.type != guitar.spec.type:
                continue
            if searching_guitar.back_wood and searching_guitar.back_wood != guitar_spec.back_wood:
                continue
            if searching_guitar.top_wood and searching_guitar.top_wood != guitar_spec.top_wood:
                continue
            matching_guitars.append(guitar)
        return matching_guitars

    



    
# def main() -> None:
#     # Create inventory
#     inventory: Inventory = Inventory()

#     # Add guitars to inventory
#     inventory.add_guitar(
#         serial_number="SN12345", 
#         price=1500.00, 
#         builder=Builder.FENDER, 
#         model="Stratocaster", 
#         type=Type.ELECTRIC, 
#         back_wood=Wood.ALDER, 
#         top_wood=Wood.MAPLE
#         )
    
#     inventory.add_guitar(
#         serial_number="SN12346", 
#         price=1500.00, builder=Builder.MARTIN, 
#         model="Stratocaster", 
#         type=Type.ACOUSTIC, 
#         back_wood=Wood.ALDER, 
#         top_wood=Wood.MAPLE
#         )
    
#     # Print out all of the guitars
#     for guitar in inventory.guitars:
#         print(f"The id is: {guitar.serial_number}, and it's price is: {guitar.price}")

#     # Check for guitar by serial number
#     guitar_id: str = "SN12345"
#     if not inventory.get_guitar(guitar_id) is None:
#         print(f"Found the guitar with the id {guitar_id}")
#     else:
#         print(f"Couldn't find the guitar with the id {guitar_id}")
    
#     what_errik_likes = Guitar(serial_number="", price=0, builder=Builder.FENDER, model="Stratocaster", type=Type.ELECTRIC, back_wood=Wood.ALDER, top_wood=Wood.MAPLE)
#     if not inventory.search(what_errik_likes) is None:
#         print("Be happy Errik, found the guitar you like: ")
#         print(what_errik_likes)
#     else:
#         print("Sorry, Erik, there is no match")

# if __name__ == "__main__":
#     main()