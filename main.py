import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(400, 400)
screen.bgcolor("white")
screen.title("D20 Die Roll")
screen.tracer(0)  # Disable auto-updates for smooth animation

# Create die visual (square shape)
die = turtle.Turtle()
die.shape("square")
die.shapesize(3, 3, 5)
die.color("red")
die.penup()

# Create number display
number = turtle.Turtle()
number.hideturtle()
number.penup()
number.goto(0, -10)
number.color("white")

def show_number(num):
    """Display the current number on the die"""
    number.clear()
    number.write(str(num), align="center", font=("Arial", 24, "bold"))

def roll_die(x=0, y=0):
    """Animate the die roll and show final result"""
    screen.onclick(None)  # Disable click during animation
    
    # Animation loop
    for _ in range(20):
        die.setheading(die.heading() + 18)  # Rotate die
        show_number(random.randint(1, 20))
        screen.update()
        turtle.time.sleep(0.05)
    
    # Final result
    final_roll = random.randint(1, 20)
    show_number(final_roll)
    die.setheading(0)  # Reset orientation
    screen.update()
    
    screen.onclick(roll_die)  # Re-enable click

# Initial setup
show_number("?")
screen.onclick(roll_die)
turtle.mainloop()