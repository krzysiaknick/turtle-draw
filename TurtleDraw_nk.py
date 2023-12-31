import turtle

print("Welcome to Turtle Draw!")
print("Enter the .txt filename below")
FILENAME = input("Filename: ")
turtledraw = turtle.Turtle()
screen = turtle.Screen()
screen.setup(450, 450)
turtledraw.speed(10)
turtledraw.penup()

# Variable to store total distance
total_distance = 0

textfile = open(FILENAME, 'r')
line = textfile.readline()
drawing_started = False

while line:
    sections = line.split(' ')

    if len(sections) == 3:
        turtlecolor = sections[0]
        x = int(sections[1])
        y = int(sections[2])

        if not drawing_started:
            drawing_started = True
        else:
            # Calculate distance moved (Credit ChatGPT)
            distance_moved = ((turtledraw.xcor() - x)**2 + (turtledraw.ycor() - y)**2)**0.5
            total_distance += distance_moved

        turtledraw.color(turtlecolor)
        turtledraw.goto(x, y)
        turtledraw.pendown()

    elif len(sections) == 1:
        turtledraw.penup()
        drawing_started = False  

    line = textfile.readline()


def measure_distance():
    turtledraw.penup()
    turtledraw.goto(40, -200)  
    turtledraw.pendown()
    turtledraw.color("black")
    turtledraw.write(f"Total Distance: {total_distance:.2f}", font=("Arial", 12, "normal"))
    turtledraw.penup()

measure_distance()

# Close the window when the Enter key is pressed
screen.onkey(turtle.bye, "Return")

screen.listen()
screen.mainloop()

textfile.close()
print('\nEnd')