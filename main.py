import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("white")
screen.title("D20 Die Roll")
screen.tracer(0)  # Disable auto-updates for smooth animation

# Create a turtle for drawing the D20
d20 = turtle.Turtle()
d20.hideturtle()
d20.speed(0)
d20.penup()

# Create a turtle for displaying the number
number = turtle.Turtle()
number.hideturtle()
number.penup()
number.color("black")

def draw_d20():
    """Draw a simplified 2D representation of a D20 (icosahedron)"""
    d20.clear()
    d20.goto(0, 100)
    d20.pendown()
    d20.color("lightblue")
    d20.begin_fill()
    for _ in range(3):  # Draw a triangle (simplified D20 face)
        d20.forward(150)
        d20.left(120)
    d20.end_fill()
    d20.penup()

def show_number(num):
    """Display the current number on the D20"""
    number.clear()
    number.goto(0, -20)
    number.write(str(num), align="center", font=("Arial", 36, "bold"))

def roll_d20(x=0, y=0):
    """Animate the D20 roll and show the final result"""
    screen.onclick(None)  # Disable click during animation
    
    # Animation loop
    for _ in range(15):
        draw_d20()
        show_number(random.randint(1, 20))
        screen.update()
        time.sleep(0.1)
    
    # Final result
    final_roll = random.randint(1, 20)
    show_number(final_roll)
    screen.update()
    
    screen.onclick(roll_d20)  # Re-enable click

# Initial setup
draw_d20()
show_number("?")
screen.onclick(roll_d20)
screen.mainloop()