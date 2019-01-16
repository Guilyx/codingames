import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
lx, ly, itx, ity = [int(i) for i in input().split()]

tx = itx
ty = ity


# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    direction = ''
    
    if ty < ly:
        if ty != 18:
            direction = 'S'
            ty += 1
    elif ty > ly:
        if ty != 0:
            direction = 'N'
            ty -= 1
    if tx < lx:
        if tx != 40:
            direction += 'E'
            tx += 1
    elif tx > lx:
        if tx != 0:
            direction += 'W'
            tx -= 1
        
    print(direction)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # A single line providing the move to be made: N NE E SE S SW W or NW
