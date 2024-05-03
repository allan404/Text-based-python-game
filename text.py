import os

# text that displays at the start of the game
def prompt():
    print("\t\t\tWelcome to the game\n\n\
      You must collect all the items before fighting the boss.\n\n\
      Moves: \t' go {direction}' (travel north, east, or west)\n\
      \t' get {item}' (add nearby item to inventory)\n\n")


# clearing the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# map of the rooms of the game
rooms = {
    'start': {'North': 'room1', 'South': 'room2','East':'room4'},
    'room1': {'South': 'start', 'item': 'torch'},
    'room2': {'North': 'start', 'East': 'room3', 'item': 'armor'},
    'room3': {'West': 'room2', 'item': 'rifle'},
    'room4': {'West': 'start', 'East': 'room7', 'North': 'room5', 'item': 'gun'},
    'room5': {'South': 'room4', 'East': 'room6', 'item': 'knife'},
    'room6': {'West': 'room5', 'item': 'smokebomb'},
    'room7': {'West': 'room4', 'Boss': 'Avenger'}
}

# list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# inventory
inventory = []

# current room
current_room = "start"

# result of last move
msg = ""

clear()
prompt()

while True:

    clear()

    # display info player
    print(f"you are in the {current_room}\nInventory : {inventory}\n{'-' * 27}")

    # display msg
    print(msg)

    # item indicator
    if 'item' in rooms[current_room].keys():
        nearby_item = rooms[current_room]["item"]

        if nearby_item not in inventory:
            if nearby_item[-1] == 's':
                print(f" you see {nearby_item}")

            elif nearby_item[0] in vowels:
                print(f"You see an {nearby_item}")
            else:
                print(f"you see a {nearby_item}")

    # boss indicator
    if "Boss" in rooms[current_room].keys():
        if len(inventory) < 6:
            print(f"you lost a fight with {rooms[current_room]['Boss']}")
            break
        else:
            print(f"you beat {rooms[current_room]['Boss']}")
            break

    # accept user input
    user_input = input("enter your move:\n")

    # split move to individual words
    next_move = user_input.split(' ')

    # first word is action
    action = next_move[0].title()

    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()

        item = ''.join(item).title()

    # moving across the rooms
    if action == "Go":

        try:
            current_room = rooms[current_room][direction]
            msg = f"you travel {direction}"

        except:
            msg = f"you cant go that way"

    # picking up an item
    elif action == "Get":
        try:
            # Convert both item and room item to lowercase for case-insensitive comparison
            if item.lower() == rooms[current_room]["item"].lower():

                if item not in inventory:

                    inventory.append(rooms[current_room]["item"])
                    msg = f"{item} retrieved!"

                else:
                    msg = f"You already have the {item}"

            else:
                msg = f"Can't find {item}"
        except:
            msg = f"Can't find {item}"

    # exit the game
    elif action == "Exit":
        break
    else:
        msg = "invalid command"
