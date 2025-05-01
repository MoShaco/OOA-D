import threading
class DogDoor:
    def __init__(self) -> None:
        self._open = False
    

    def open(self) -> None:
        print("The dog door opens")
        self._open = True
        timer = threading.Timer(5.0, self.close)
        timer.start()
    
    def close(self) -> None:
        print("The dog door closes")
        self._open = False
    
    def is_open(self) -> bool:
        return self._open
    