from bark import Bark
import threading
class DogDoor:
    def __init__(self) -> None:
        self._open = False
        self._allowed_barks: list[Bark] = []

    @property
    def allowed_barks(self) -> list[Bark]:
        return self._allowed_barks

    def add_allowed_bark(self, bark: Bark) -> None:
        if not isinstance(bark, Bark):
            raise ValueError("Only Bark object can be added")
        self._allowed_barks.append(bark)

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