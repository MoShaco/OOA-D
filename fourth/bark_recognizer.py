from dog_door import DogDoor
from bark import Bark
class BarkRecognizer:
    def __init__(self, door: DogDoor) -> None:
        self._door = door
    
    @property
    def door(self) -> DogDoor:
        return self._door
    
    
    def recognize(self, bark: Bark) -> None:
        print(f"BarkRecognizer: Heard a {bark.sound}")
        allowed_barks: list[Bark] = self.door.allowed_barks
        for allowed_bark in allowed_barks:
            if allowed_bark.equals(bark):
                self.door.open()
                return
        print("This dog is not allowed")