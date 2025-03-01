from dog_door import DogDoor
from remote import Remote


def main():
    door = DogDoor()
    remote = Remote(door=door)

    print("Fido barks to go outside...")
    remote.press_button()

    print("Fido has gone outside... ")
    remote.press_button()

    print("Fido's all done...")
    remote.press_button()
    
    print("Fido's back inside... ")
    remote.press_button()



if __name__ == "__main__":
    main()
