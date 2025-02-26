def escape_room():
    print("You are in a dimly lit room. You see a dusty bookshelf, a locked drawer, and a window.")
    key_found = False
    while True:
        action = input("What do you want to do? (open drawer/examine bookshelf/look out window/): ").strip().lower()
        if action == "open drawer":
            if key_found:
                print("Congratulations! You've escaped the room!")
                break
            else:
                print("The drawer is locked.")
        elif action == "look out window":
            print("You see a dark alleyway.")
        elif action == "examine bookshelf":
            print("The bookshelf is filled with old, leather-bound books. One book seems slightly out of place.")
            examine_book = input("Do you want to examine the book? (yes/no): ").strip().lower()
            if examine_book == "yes":
                print("You found a small key!")
                key_found = True
        else:
            print("I don't understand that action.")

if __name__ == "__main__":
    escape_room()
