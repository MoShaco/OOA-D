from dog_door import DogDoor
from bark_recognizer import BarkRecognizer
import time

def main():
    door: DogDoor = DogDoor()
    recognizer: BarkRecognizer = BarkRecognizer(door=door)

    print("Fido starts barking...")
    recognizer.recognize("Woof")
    print("\n Fido has gone outside ...")
    print("\n Fido's all done ...")

    time.sleep(10)

    print("... but he's stuck outside!")
    print("\n Fido starts barking ...")
    recognizer.recognize("Woof")
    
    print("\n Fido's back inside ...")

if __name__ == "__main__":
    main()
