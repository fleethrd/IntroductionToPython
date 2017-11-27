"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Ryan Fleetham.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

# define constants
speed = 10
size = 100
thickness = 3

window = rg.TurtleWindow()

# set up all of the turtles
blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('blue', thickness)
blue_turtle.speed = speed

red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red', thickness)
red_turtle.speed = speed

green_turtle = rg.SimpleTurtle('turtle')
green_turtle.pen = rg.Pen('green', thickness)
green_turtle.speed = speed

purple_turtle = rg.SimpleTurtle('turtle')
purple_turtle.pen = rg.Pen('purple', thickness)
purple_turtle.speed = speed

orange_turtle = rg.SimpleTurtle('turtle')
orange_turtle.pen = rg.Pen('orange', thickness)
orange_turtle.speed = speed

pink_turtle = rg.SimpleTurtle('turtle')
pink_turtle.pen = rg.Pen('pink', thickness)
pink_turtle.speed = speed

brown_turtle = rg.SimpleTurtle('turtle')
brown_turtle.pen = rg.Pen('brown', thickness)
brown_turtle.speed = speed

black_turtle = rg.SimpleTurtle('turtle')
black_turtle.pen = rg.Pen('black', thickness)
black_turtle.speed = speed

for k in range(4):
    # Put the pen down, then draw a square of the given size:
    blue_turtle.draw_square(size)

    # Pick up the pen and turn right
    blue_turtle.pen_up()
    blue_turtle.right(90)

    # Put the pen down again (so drawing resumes).
    blue_turtle.pen_down()

for k in range(3):
    # Put the pen down, then draw a triangle of the given size:
    red_turtle.draw_regular_polygon(3, size)

    # Pick up the pen and turn right.
    red_turtle.pen_up()
    red_turtle.left(120)

    # Put the pen down again (so drawing resumes).
    red_turtle.pen_down()

for k in range(5):
    # Put the pen down, then draw a pentagon of the given size:
    green_turtle.draw_regular_polygon(5, size)

    # Pick up the pen and turn right
    green_turtle.pen_up()
    green_turtle.left(72)

    # Put the pen down again (so drawing resumes).
    green_turtle.pen_down()

for k in range(6):
    # Put the pen down, then draw a hexagon of the given size:
    purple_turtle.draw_regular_polygon(6, size)

    # Pick up the pen and turn right
    purple_turtle.pen_up()
    purple_turtle.left(60)

    # Put the pen down again (so drawing resumes).
    purple_turtle.pen_down()

for k in range(7):
    # Put the pen down, then draw a heptagon of the given size:
    orange_turtle.draw_regular_polygon(7, size)

    # Pick up the pen and turn right
    orange_turtle.pen_up()
    orange_turtle.left(51.4285714)

    # Put the pen down again (so drawing resumes).
    orange_turtle.pen_down()

for k in range(8):
    # Put the pen down, then draw a octagon of the given size:
    pink_turtle.draw_regular_polygon(8, size)

    # Pick up the pen and turn right
    pink_turtle.pen_up()
    pink_turtle.left(45)

    # Put the pen down again (so drawing resumes).
    pink_turtle.pen_down()

for k in range(9):
    # Put the pen down, then draw a nonagon of the given size:
    brown_turtle.draw_regular_polygon(9, size)

    # Pick up the pen and turn right
    brown_turtle.pen_up()
    brown_turtle.left(40)

    # Put the pen down again (so drawing resumes).
    brown_turtle.pen_down()

for k in range(10):
    # Put the pen down, then draw a decagon of the given size:
    black_turtle.draw_regular_polygon(10, size)

    # Pick up the pen and turn right
    black_turtle.pen_up()
    black_turtle.left(36)

    # Put the pen down again (so drawing resumes).
    black_turtle.pen_down()

window.close_on_mouse_click()
