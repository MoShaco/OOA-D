from dog_door import DogDoor

class Remote:
    def __init__(self, door: DogDoor):
        self._door = door
    
    @property
    def door(self) -> DogDoor:
        return self._door
    

    def press_button(self) -> None:
        print("Pressing the remote control button...")
        if self.door.is_open():
            self.door.close()
        else:
            self.door.open()