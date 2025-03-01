class DogDoor:
    def __init__(self) -> None:
        self._open = False
    

    def open(self) -> None:
        print("The dog door opens")
        self._open = True
    
    def close(self) -> None:
        print("The dog door closes")
        self._open = False
    
    def is_open(self) -> bool:
        return self._open
    