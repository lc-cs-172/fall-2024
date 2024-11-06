"""Koch curve; https://en.wikipedia.org/wiki/Koch_snowflake"""

from turtle import Turtle, win

def koch(n : int, step : float, turtle : Turtle):
    """Draw a Koch curve of order n."""
    if n == 0:
        turtle.go_forward(step)
        return
    koch(n - 1, step, turtle)
    turtle.turn_left(60.0)
    koch(n - 1, step, turtle)
    turtle.turn_left(-120.0)
    koch(n - 1, step, turtle)
    turtle.turn_left(60.0)
    koch(n - 1, step, turtle)

def main():
    n = 0
    step = 3.0 ** -n
    turtle = Turtle(0.0, 0.1, 0.0)
    koch(n, step, turtle)
    win.getMouse()

if __name__ == '__main__':
    main()
