def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def do_a_hurdle():
    turn_left()
    i = 0
    while wall_on_right():
        move()
        i += 1
    turn_right()
    move()
    turn_right()
    for a in range(i):
        move()
    turn_left()


#Maze
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()