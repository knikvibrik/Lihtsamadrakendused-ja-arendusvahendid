import random

def try_next_move():
    if random.random() < 0.25:
        print("Try to go right")

    elif random.random() < 0.5:
        print("Try to go left")

    elif random.random() < 0.75:
        print("Try to go bottom")

    elif random.random() < 0.1:
        print("Try to go top")

try_next_move()

map1 = [
    [12, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 24]
]
map2 = [
    [12, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 24]
]
map3 = [
    [12, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [24, 0, 0, 0]
]
map4 = [
    [12, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0], 
    [1, 0, 0, 0, 0, 24]
]
map5 = [
    [0, 1, 0, 0, 0, 0],
    [0, 12, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 1, 24, 0, 0], 
    [1, 0, 0, 0, 0, 0]
]
map = map5

# define starting position
start_position_x = 0
start_position_y = 0

# define  function to take moves
def move(step, current_position_x,current_position_y):
    print("Current step is: ", step)
    print("Current current_position_y = ", current_position_y)
    print("Current current_position_x = ", current_position_x)

    can_move_right = current_position_x <= 4 and map[current_position_y][current_position_x + 1] == 0
    can_move_to_bottom = current_position_y <= 3 and map[current_position_y + 1][current_position_x] == 0
    can_move_left = current_position_x <= 4 and map[current_position_y][current_position_x - 1] == 0
    can_move_up = current_position_x <= 4 and map[current_position_y - 1][current_position_x] == 0 

    right_is_finish = current_position_x <= 4 and map[current_position_y][current_position_x + 1] == 24
    bottom_is_finish = current_position_y <= 3 and map[current_position_y + 1][current_position_x] == 24
    left_is_finish = current_position_x <= 4 and map[current_position_y][current_position_x - 1] == 24 
    up_is_finish = current_position_x <= 4 and map[current_position_y - 1][current_position_x] == 24 


    if right_is_finish:
        print("Found finish on right")
        return False
    if bottom_is_finish:
        print("Found finish on bottom")
        return False
    if left_is_finish:
        print("Found finish on left")
        return False
    if up_is_finish:
        print("Found finish on left")
        return False
    
    if can_move_right:
        print("Should move right")
        current_position_x = current_position_x + 1
    if can_move_to_bottom:
        print("Should move down")
        current_position_y = current_position_y + 1
    if can_move_left:
        print("Should move left")
        current_position_x = current_position_x - 1
    if can_move_up:
        print("Should move up")
        current_position_y = current_position_y - 1

current_move_number = 1
new_position = move(current_move_number, start_position_x, start_position_y)
while new_position:
    current_move_number = current_move_number + 1
    new_position = move(current_move_number, new_position[0], new_position[1])