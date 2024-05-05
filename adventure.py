import json
import sys
import traceback
import inspect

class Adventure:
    def __init__(self, map_file):
        self.inventory_items=[]
        self.load_map(map_file)
        self.current_room = self.start_room

    def load_map(self, map_file):
        with open(map_file, 'r') as file:
            map_data = json.load(file)
            # Validate map
            if 'start' not in map_data or 'rooms' not in map_data:
                print("Invalid map file: Missing 'start' or 'rooms' key.", file=sys.stderr)
                sys.exit(1)
            room_names = set()
            for room in map_data['rooms']:
                if 'name' not in room or 'desc' not in room or 'exits' not in room:
                    print("Invalid map file: Missing required fields in rooms.", file=sys.stderr)
                    sys.exit(1)
                if room['name'] in room_names:
                    print("Invalid map file: Duplicate room names.", file=sys.stderr)
                    sys.exit(1)

                room_names.add(room['name'])
            for exit_room in room['exits'].values():
                if exit_room not in room_names:
                    print("Invalid map file: Exit points to non-existent room.", file=sys.stderr)
                    sys.exit(1)
            # Extract start room
            self.start_room = map_data['start']
            # Extract rooms
            self.rooms = {room['name']: room for room in map_data['rooms']}

    def go(self, direction):
        exits = self.rooms[self.current_room]['exits']
        if direction in exits:
            print(f"You go {direction}.\n")
            self.current_room = exits[direction]
            self.look()
        else:
            print(f"There's no way to go {direction}.")

    def look(self):
        current_room = self.rooms[self.current_room]
        print(f"> {current_room['name']}\n")
        print(f"{current_room['desc']}\n")
        if 'items' in self.rooms[self.current_room]:
            item = ", ".join(self.rooms[self.current_room]['items'])
            if item:
                print(f"Items: {item}\n")
        exits = " ".join(current_room['exits'].keys())
        print(f"Exits: {exits}\n")

    def get(self, item):
        if 'items' in self.rooms[self.current_room]:
            items = self.rooms[self.current_room]['items']
            if item in items:
                self.inventory_items.append(item)
                print(f"You pick up the {item}.")
                items.remove(item)
            else:
                print(f"There's no {item} anywhere.")
        else:
            print(f"There's no {item} anywhere.")

    def inventory(self):
        if len(self.inventory_items) > 0:
            print("Inventory:")
            for i in sorted(self.inventory_items):
                print(f"  {i}")
        else:
            print("You're not carrying anything.")
        return True

    def quit(self):
        print("Goodbye!")
        sys.exit(0)

    def command_prompt(self, command):
        parts = command.split()
        verb = parts[0]
        if verb == 'go':
            if len(parts) > 1:
                self.go(parts[1])
            else:
                print("Sorry, you need to 'go' somewhere.")
        elif verb == 'look':
            self.look()
        elif verb == 'get':
            if len(parts) > 1:
                self.get(" ".join(parts[1:]))
            else:
                print("Sorry, you need to 'get' something.")
        elif verb == 'inventory':
            self.inventory()
        elif verb == 'quit':
            self.quit()
        elif verb == 'help':
            self.help()
        else:
            print("I don't understand that command.")

    def help(self):
        verbs = ['go', 'look', 'get', 'inventory', 'quit', 'help']
        print("You can run the following commands:")
        for verb in verbs:
            print(f"  {verb}")

    def play(self):
        self.look()
        while True:
            command = input("What would you like to do? ").strip().lower()
            if not command:
                continue
            self.command_prompt(command)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 adventure.py [map filename]", file=sys.stderr)
        sys.exit(1)
    map_file = sys.argv[1]
    adventure_game = Adventure(map_file)
    adventure_game.play()
