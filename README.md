# CS 515 Adventure
# Adventure Game

## Author Information
Ankit Durgaprasad Chaurasia
achauras@stevens.edu

[Github Repository](https://github.com/AnkitChaurasia1997/CS515-Adventure.git)

## Estimation of Hours Spent on the project
I spent around 19 hours approximately on the project.

## Testing of the code
1. Initially I started the testing by forking the main branch and started testing on my VSCODE terminal.
2. Later on I wrote test cases gradually in the format specified in description, and wrote a test harness to check the output.

## Unresolved Issue or bug
1. Running test #17 on /autograder/source/badmaps/loop_badexit.map...FAILED!
Expected non-zero exit status, got 0.
Expected non-empty STDERR, was empty.

I tried to solve the bug by using this

for exit_room in room['exits'].values():
                if exit_room not in room_names:
                    print("Invalid map file: Exit points to non-existent room.", file=sys.stderr)
                    sys.exit(1)

## Examples of difficult bugs resolved
Apart from mentioned issue I didnt have any issues

## Extensions Implemented
1. **help** : I have implemented the help extension, that shows a list of commands that the user can run. The implementation is dynamic which means everytime one adds a command it will dynamically appear in response from the help command. It also print "..", indicating the commands which accept input parameters. The following example shows the help command.

```
What would you like to do? help
You can run the following commands:
  go ...
  look
  get ...
  inventory
  quit
  help
  drop ...
  unlock ...
```

2. **drop** : I have implemented the drop extension which drops an item from the player's inventory. The following example demonstrates the drop command.
```
> A white room

You are in a simple room with white walls.

Exits: north east

What would you like to do? go east
You go east.

> A red room

This room is fancy. It's red!

Items: rose

Exits: north west

What would you like to do? get rose
You pick up the rose.
What would you like to do? inventory
Inventory:
  rose
What would you like to do? drop rose
You drop the rose.
What would you like to do? inventory
You're not carrying anything.
What would you like to do? look
> A red room

This room is fancy. It's red!

Items: rose

Exits: north west

What would you like to do? drop
Sorry, you need to 'drop' something.
What would you like to do? drop mango
You don't have mango in your inventory.
```

3. **Locked doors** : I've added a locked door extension in which some doors are locked on the map and can be unlocked with the **unlock** command. To unlock a locked door, a special key is required. The key is searchable on the map. If the player has this key in their inventory, they can unlock the door. The example below demonstrates the locked door extension. You must use the **game.map** file given as the map when utilizing this extension.
```
>  A white room

You are in a simple room with white walls.

Exits: north east

What would you like to do? go north
The door is locked, you need to unlock the door.
What would you like to do? go east
You go east.

> A red room

This room is fancy. It's red!

Items: rose

Exits: north west

What would you like to do? get rose
You pick up the rose.
What would you like to do? look
> A red room

This room is fancy. It's red!

Exits: north west

What would you like to do? go west
You go west.

> A white room

You are in a simple room with white walls.

Exits: north east

What would you like to do? go north
The door is locked, you need to unlock the door.
What would you like to do? unlock north
You don't have the correct key to unlock the door.
What would you like to do? go east
You go east.

> A red room

This room is fancy. It's red!

Exits: north west

What would you like to do? go north
You go north.

> A green room

You are in a simple room, with bright green walls.

Items: black comb

Exits: west south

What would you like to do? get black comb
You pick up the black comb.
What would you like to do? inventory
Inventory:
  black comb
  rose
What would you like to do? look
> A green room

You are in a simple room, with bright green walls.

Exits: west south

What would you like to do? go west
The door is locked, you need to unlock the door.
What would you like to do? unlock west
You have now unlocked the door! You can go in!
What would you like to do? go west
You go west.

> A blue room

This room is simple, too, but with blue walls.

Exits: east south

What would you like to do?
```