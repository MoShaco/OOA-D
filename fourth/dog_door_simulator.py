from dog_door import DogDoor
from bark import Bark
from remote import Remote
from bark_recognizer import BarkRecognizer
import time

def main():
    door: DogDoor = DogDoor()
    door.add_allowed_bark(Bark(sound="rowlf"))
    door.add_allowed_bark(Bark(sound="rooowlf"))
    door.add_allowed_bark(Bark(sound="rawlf"))
    door.add_allowed_bark(Bark(sound="woof"))
    recognizer: BarkRecognizer = BarkRecognizer(door=door)
    remote: Remote = Remote(door=door)

    # Simulate the hardware hearing a bark
    print("Bruce starts barking...")
    recognizer.recognize(Bark(sound="rowlf"))
    print("\n Bruce has gone outside ...")
    time.sleep(10)
    print("\n Bruce's all done ...")
    print("... but he's stuck outside!")

    # Simulate the hardware hearing a bark (not Bruce !)
    small_dog_bark = Bark(sound="yip")
    print("A small dog starts barking.")
    recognizer.recognize(small_dog_bark)
    time.sleep(5)

    # Simulate the hardware hearing a bark again
    print("Bruce starts barking.")
    recognizer.recognize(Bark(sound="rooowlf"))
    print("Bruce's back inside ...")

if __name__ == "__main__":
    main()
