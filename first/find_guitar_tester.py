from guitar import Guitar
from guitar_spec import GuitarSpec
from inventory import Inventory
from type import Type
from builder import Builder
from wood import Wood

def main() -> None:
    # Create inventory
    inventory: Inventory = Inventory()

    # Add guitars to inventory
    inventory.add_guitar(
        serial_number="SN12345", 
        price=1500.00, 
        builder=Builder.FENDER, 
        model="Stratocaster", 
        type=Type.ELECTRIC, 
        back_wood=Wood.ALDER, 
        top_wood=Wood.MAPLE,
        num_strings=12
        )
    
    inventory.add_guitar(
        serial_number="SN12346", 
        price=1500.00, 
        builder=Builder.FENDER, 
        model="Stratocaster", 
        type=Type.ELECTRIC, 
        back_wood=Wood.ALDER, 
        top_wood=Wood.MAPLE,
        num_strings=6
        )
    
    inventory.add_guitar(
        serial_number="SN12347", 
        price=1500.00, 
        builder=Builder.MARTIN, 
        model="Stratocaster", 
        type=Type.ACOUSTIC, 
        back_wood=Wood.ALDER, 
        top_wood=Wood.MAPLE,
        num_strings=12
        )

    # Print out all of the guitars
    print("Rick's Store has the following guitars: ")
    count: int = 1
    for guitar in inventory.guitars:
        print(f"{count} - {guitar}")
        count += 1
    print()

    # Check for guitar by serial number
    guitar_id: str = "SN12345"
    if not inventory.get_guitar(guitar_id) is None:
        print(f"Found the guitar with the id {guitar_id}")
    else:
        print(f"Couldn't find the guitar with the id {guitar_id}")
    print()

    what_errik_likes = GuitarSpec(
        builder=Builder.FENDER, 
        model="Stratocaster", 
        type=Type.ELECTRIC, 
        back_wood=Wood.ALDER, 
        top_wood=Wood.MAPLE,
        num_strings=12
        )
    
    matching_guitars: list[Guitar] = inventory.search(what_errik_likes)
    if matching_guitars:
        print(f"Found {len(matching_guitars)} matching guitars")
        count = 1
        for guitar in matching_guitars:
            print(f"{count} - {guitar}")
            count += 1
    else:
        print("Sorry, couldn't find matchig guitar with your search")
if __name__ == "__main__":
    main()