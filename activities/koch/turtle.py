"""An implementation of turtle graphics."""

import math
import graphics as g

win = g.GraphWin('Turtle Graphics', 400, 400)
win.setCoords(0.0, 0.0, 1.0, 1.0)

class Turtle:

    def __init__(self, x0 : float, y0 : float, a0 : float):
        """Initialize a new turtle at (x0, y0) facing a0 degrees from the x-axis."""
        self.x = x0
        self.y = y0
        self.a = a0

    def turn_left(self, delta):
        """Instruct the turtle to turn left (counterclockwise) by `delta` degrees."""
        self.a += delta
    
    def go_forward(self, step : float):
        """Instruct the turtle to move forward distance `step`, drawing a line."""
        old_x = self.x
        old_y = self.y

        self.x += step * math.cos(math.radians(self.a))
        self.y += step * math.sin(math.radians(self.a))
        l = g.Line(g.Point(old_x, old_y), g.Point(self.x, self.y))
        l.draw(win)

def main():
    n = 3
    step = math.sin(math.radians(180.0/n))
    print(str(step))
    turtle = Turtle(.5, .0, 180.0/n)
    for i in range(n):
        turtle.go_forward(step)
        turtle.turn_left(360.0/n)
    win.getMouse()

if __name__ == '__main__':
    main()
