from dog_door import DogDoor
from remote import Remote


def main():
    door = DogDoor()
    remote = Remote(door=door)

    print("Fido barks to go outside...")
    remote.press_button()

    print("Fido has gone outside... ")

    print("Fido's all done...")
    
    print("Fido's back inside... ")



if __name__ == "__main__":
    main()
