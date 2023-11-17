import turtle
import os


print("Welcome to Turtle Draw!")
print("Enter the .txt filename below")
FILENAME = input("Filename: ")
turtledraw = turtle.Turtle()
turtle.Screen().setup(450,450)
turtledraw.speed(10)
turtledraw.penup()



textfile = open(FILENAME, 'r')
line = textfile.readline()
while line:
    print(line)
    sections = line.split(' ')

    if (len(sections) == 3):
        turtlecolor = sections[0]
        x = int(sections[1])
        y = int(sections[2])

        turtledraw.color(turtlecolor)
        turtledraw.goto(x,y)

        turtledraw.pendown()

    if (len(sections)== 1):
        turtledraw.penup()

    line = textfile.readline()

turtle.done()
textfile.close()
print('\nEnd')
