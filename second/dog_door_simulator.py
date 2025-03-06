from dog_door import DogDoor
from remote import Remote
import time

def main():
    door = DogDoor()
    remote = Remote(door=door)
    remote.press_button()

    print("Fido has gone outside... ")
    print("Fido's all done...")

    time.sleep(10)

    print("... but he's stuck outside!")
    print("\n Fido starts barking ...")
    print("... so Gina grabs the remote control.")

    remote.press_button()
    
    print("\n Fido's back inside ...")

if __name__ == "__main__":
    main()
