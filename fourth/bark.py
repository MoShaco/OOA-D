class Bark:
    def __init__(self, sound: str) -> None:
        self._sound = sound

    @property
    def sound(self) -> str:
        return self._sound
    

    def equals(self, bark: object) -> bool:
        if isinstance(bark, Bark):
            if self.sound.casefold() == bark.sound.casefold():
                return True
        return False

    def __str__(self) -> str:
        return self.sound