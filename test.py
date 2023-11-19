import turtle
import os

print("Welcome to Turtle Draw!")
print("Enter the .txt filename below")
FILENAME = input("Filename: ")
turtledraw = turtle.Turtle()
turtle.Screen().setup(450, 450)
turtledraw.speed(10)
turtledraw.penup()

# Variable to store total distance
total_distance = 0

textfile = open(FILENAME, 'r')
line = textfile.readline()
drawing_started = False

while line:
    print(line)
    sections = line.split(' ')

    if len(sections) == 3:
        turtlecolor = sections[0]
        x = int(sections[1])
        y = int(sections[2])

        if not drawing_started:
            drawing_started = True
        else:
            # Calculate distance moved
            distance_moved = ((turtledraw.xcor() - x)**2 + (turtledraw.ycor() - y)**2)**0.5
            total_distance += distance_moved

        turtledraw.color(turtlecolor)
        turtledraw.goto(x, y)
        turtledraw.pendown()

    elif len(sections) == 1:
        turtledraw.penup()
        drawing_started = False  # Set drawing_started to False when pen is up

    line = textfile.readline()

# Function to measure and print total distance
def measure_distance():
    turtledraw.penup()
    turtledraw.goto(-200, -200)  # Adjust the coordinates as needed
    turtledraw.pendown()
    turtledraw.color("black")
    turtledraw.write(f"Total Distance: {total_distance:.2f}", font=("Arial", 12, "normal"))
    turtledraw.penup()
    turtledraw.home()

measure_distance()

turtle.done()
textfile.close()
print('\nEnd')
