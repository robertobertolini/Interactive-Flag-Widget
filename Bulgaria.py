
# coding: utf-8

# In[2]:

# Roberto Bertolini and Tiffany Roberti

# This py file draws the Bulgarian Flag using the turtle Graphics package 
# in Python. The program first draws the flag and then the user can learn
# more about the meaning of the symbols of the flag by clicking on them. 

# Subfunctions:

    # border
        # input: height,color
            # Draws the rectangular shape of the flag using the height and 
            # width specifications of the border
    # strip_write
        # input: turtle, string
            # Takes the string of the flag's name  and alternates the color of 
            # each letter in the word
    # textbox_click
        # input: x and y coordinates
            # Retrieves the color of the point that the user clicks on and prints the 
            # corresponding meaning of the color to the user on the Turtle graphics window
    # usertext
        # input: color
            # Displays information about the flag's colors when the user clicks on the flag
    # getcoordinates
        # input: None
            # Uses the onscreenclick method of turtle to extract the x and y coordinate
            # that the user clicked on
    # modifyglobalvariables
        # input: x and y coordinates
            # Updates the point that the user clicks on (rawx and rawy are the global variables
            # specifying these points)

import turtle
import random
import time
from itertools import cycle
 

# The function "border" draws the flag's border

def border(height,color):
    
    # turtle.begin_fill is used to specify that we want the rectangle to 
    # be filled  
    
    turtle.begin_fill()
    turtle.color(color)
    height = float(height)
    length = height *(1.9)
    length = round(length,2)
    
    # Draws a rectangle. Note that "forward" corresponds to the pointer moving east
    # in a straight line. The "right" command tells the Turtle to make a 90 degree turn
    # to the right. This is done four times to draw the quadrilateral.
    
    for i in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.begin_fill()
    turtle.color(color)
    turtle.end_fill()

def stripe_write(turtle, string):
    color = cycle(["red", "green"])

    for character in string:
        turtle.color(next(color))
        turtle.write(character, move=True, font=("Times New Roman", 48, "normal"))

# This function takes the x and y coordinate that the user clicks on and uses the 
# getcanvas() method to retrieve the color of the point the user clicks on. Depending
# on the color and location, the program will display the meaning of the symbol to the user
# after the flag and instructions.
        
def textbox_click(rawx,rawy):
    turtle.up()
    turtle.setposition(rawx,rawy)
    turtle.down()
    rawy = -rawy
    canvas = turtle.getcanvas()
    canvas.pack(fill="both", expand=True)
    ids = canvas.find_overlapping(rawx, rawy, rawx, rawy)
    print(ids)
    if len(ids)<3: 
        index = ids[0]
        color = canvas.itemcget(index, "fill")
    if len(ids)>=3: 
        index = ids[-2]
        color = canvas.itemcget(index, "fill")
    usertext(color)
    
# Displays the symbolic meaning of the color that is clicked on as text above the flag
# at a specified position
    
def usertext(color):
    turtle.up()
    if color=="red":
        x1=0
        y1=200
        turtle.setposition(x1,y1) 
        turtle.down()
        turtle.color("red")
        turtle.write(" Red symbolizes the courage of the country",align="center",font=("Times New Roman", 20, "normal"))
        turtle.up()
        
    elif color=="white":     
        x1=0
        y1=135
        turtle.setposition(x1,y1) 
        turtle.down()
        turtle.color("white")
        turtle.write(" White symbolizes peace",align="center",font=("Times New Roman", 20, "normal"))
        turtle.up()
        
    elif color=="green":
        x1=0
        y1=45
        turtle.setposition(x1,y1) 
        turtle.down()
        turtle.color("green")
        turtle.write(" Green symbolizes the fertility of the soil \n and agricultural character of the country",align="center",font=("Times New Roman", 20, "normal"))
        turtle.up()

# Uses the command "onscreenclick" to extract the x and y coordinate
# that the user clicked on

def getcoordinates():
    turtle.onscreenclick(turtle.goto)
    turtle.onscreenclick(modifyglobalvariables)
    turtle.onscreenclick(textbox_click)

# Updates the location that the user clicks on
    
def modifyglobalvariables(rawx,rawy):
    global xclick
    global yclick
    xclick = int(rawx//1)
    yclick = int(rawy//1)    

########################## BEGIN MAIN FUNCTION ################################
    
def main():
    
    # Creates the rectangular border 
    turtle.bgcolor("CadetBlue")
    
    border(150,"black")
    
    # Brings the turtle to home position 

    x1=0
    y1=0
    turtle.setpos(x1,y1)

    # Determines the width of the 3 stripes

    height = 150
    stripwidth = height / float(3)
    turtle.speed(100)

    x1=0
    y1=0-stripwidth
    
    # Draws the three different color rectangles on the canvas
    
    color_list = ["white","green","red"]
    for i in range(len(color_list)):
        turtle.pu()
        turtle.begin_fill() 
        turtle.down() 
        turtle.color(color_list[i])
        turtle.setheading(90)
        turtle.setpos(x1,y1)
        length = height *(1.9)
        turtle.begin_fill()
        turtle.forward(stripwidth)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(stripwidth)
        turtle.right(90)
        turtle.forward(length)
        turtle.end_fill()
        y1 -= stripwidth  

# Brings the turtle again to the origin
    turtle.up()
    x1=0
    y1=0
    turtle.setposition(x1,y1)
    turtle.setheading(90)

    
# Prints Bulgaria in alternating colors
    x1 = -115
    y1 = -250
    turtle.setposition(x1,y1)
    turtle.down()
    stripe_write(turtle, "Bulgaria")
    turtle.up()
    
# Print the instructions  
    turtle.color("black")
    x1 = -175
    y1 = -100
    turtle.setposition(x1,y1)
    turtle.down()
    turtle.write(" Click on a feature of the\n flag to learn more about it!",align="center",font=("Times New Roman", 20, "normal"))

    xclick = 0
    yclick = 0

    # Extracts the point that the user clicks on and allows them to play with the flag interactively.
    
    getcoordinates()

    # No more drawings - we are done!  
    
    turtle.done()
    
    try:
        turtle.exitonclick()
    except Exception:
        pass
    
main()

############################# END MAIN FUNCTION ################################

