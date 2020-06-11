from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
visited = set()
paths = Stack()
while len(visited)<len(room_graph):
    exits = player.current_room.get_exits()
    path =[]
    for i in exits:
        if i is not None and player.current_room.get_room_in_direction(i) not in visited:
            path.append(i)
    visited.add(player.current_room)

    if len(path)>0:
        direction = random.choice(path)
        paths.push(direction)
        traversal_path.append(direction)
        player.travel(direction)
        
    else:
        back = {'s': 'n', 'n': 's', 'w': 'e', 'e': 'w'}
        e= paths.pop()
        traversal_path.append(back[e])
        player.travel(back[e])
  


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
'''
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
'''