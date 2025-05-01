from dog_door import DogDoor
class BarkRecognizer:
    def __init__(self, door: DogDoor) -> None:
        self._door = door
    
    @property
    def door(self) -> DogDoor:
        return self._door
    
    
    def recognize(self, bark: str) -> None:
        print(f"BarkRecognizer: Heard a {bark}")
        self.door.open()