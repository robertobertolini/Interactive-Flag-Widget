
# coding: utf-8

# In[7]:

# Roberto Bertolini and Tiffany Roberti

# This py file draws the American Flag using the turtle Graphics package 
# in Python. The program first draws the flag and then the user can learn
# more about the meaning of the symbols of the flag by clicking on them. 

# Subfunctions:

    # border
        # input: height,color
            # Draws the rectangular shape of the flag using the height and 
            # width specifications of the border
    # draw_blue
        # input: height
            # Draws the blue section of the American flag and fills the 
            # rectangle in with blue.
    # arrangment
        # input: None
            # This function sets up the specifications to arrange the rows of 
            # stars in the flag. 
    # america_star
        # input: size, color
            # This function sets up the specifications to arrange the rows of 
            # stars in the flag.
    # five_star
        # input: None
            # Uses the previous two functions, arrangement and america_star, to 
            # create a row of five stars 
    # six_star
        # input: None
            # Uses the previous two functions, arrangement and america_star, to 
            # create a row of six stars 
    # strip_write
        # input: turtle, string
            # Takes the string of the flag's name (U.S.A.) and alternates the color of 
            # each letter in the word
    # textbox_click
        # input: x and y coordinates
            # Retrieves the color of the point that the user clicks on and prints the 
            # corresponding meaning of the color to the user on the Turtle graphics window
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
    # be filled with the color red. 
    
    turtle.begin_fill()
    turtle.color(color)
    height = float(height)
    length = height *(1.9)
    length = round(length,2)
    print(height)
    print(length)
    
    # Draws a rectangle. Note that "forward" corresponds to the pointer moving east
    # in a straight line. The "right" command tells the Turtle to make a 90 degree turn
    # to the right. This is done four times to draw the quadrilateral.
    for i in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    
#     turtle.forward(length)
#     turtle.right(90)
#     turtle.forward(height)
#     turtle.right(90)
#     turtle.forward(length)
#     turtle.right(90)
#     turtle.forward(height)
#     turtle.right(90)
    turtle.begin_fill()
    turtle.color(color)
    turtle.end_fill

# This function draws the blue rectangle of the flag and shades it in blue.

def draw_blue(height):
    
    turtle.begin_fill()
    turtle.color("blue")
    x1=0
    y1=0
    height= float(height)
    blue_height = float(height*(7/float(13)))
    blue_width = height*1.9
    blue_width = blue_width * (2/float(5))
    
    # Sets the position and draws the rectangle
    
    turtle.setpos(x1,y1)
    for i in range(2):
        turtle.right(90)
        turtle.forward(blue_width)
        turtle.right(90)
        turtle.forward(blue_height)
#     turtle.right(90)
#     turtle.forward(blue_width)
#     turtle.right(90)
#     turtle.forward(blue_height)
    turtle.right(90)
    turtle.setpos(x1,y1)
    
    # Begin the fill process.
    turtle.begin_fill() 
    turtle.down() # Puts the mouse down
    
    # Draws the blue rectangle
    
    for i in range(2):
        turtle.forward(115)
        turtle.right(90)
        turtle.forward(80)
        turtle.right(90)
    
#     turtle.forward(115)
#     turtle.right(90)
#     turtle.forward(80)
#     turtle.right(90)
#     turtle.forward(115)
#     turtle.right(90)
#     turtle.forward(80)
#     turtle.right(90)
    turtle.up() # Picks the mouse up
    turtle.end_fill() # End fill.


# This function is used to arrange the rows of stars on a straight line

def arrangment():
    turtle.pu()
    turtle.left(90)
    turtle.forward(20)
    turtle.pd()


# Draws one of the 50 stars of the American flag. Note that this requires
# moving the pointer at a 144 degree angle with respect to the y axis to create 
# the star shape. The program fills in each star with the color white.

def america_star(size,color): 

    turtle.speed(100)
    size= float(size)
    turtle.right(90)
    turtle.begin_fill()
    turtle.color(color)
    turtle.down()
    for i in range(5):
        turtle.forward(size)
        turtle.left(144)
#     turtle.forward(size)
#     turtle.left(144)
#     turtle.forward(size)
#     turtle.left(144)
#     turtle.forward(size)
#     turtle.left(144)
#     turtle.forward(size)
#     turtle.left(144)
#     turtle.forward(size)
#     turtle.left(144)
    turtle.end_fill()

# Draws a row of five stars #

def five_stars():
    for i in range(5):
        america_star(8,"white")
        arrangment()
        
def six_stars():
    for i in range(6):
        america_star(8,"white")
        arrangment()

# def five_stars():
#     america_star(8,"white")
#     arrangment()
#     america_star(8,"white")
#     arrangment()
#     america_star(8,"white")
#     arrangment()
#     america_star(8,"white")
#     arrangment()
#     america_star(8,"white")

# Draws a row of six stars #

# def six_stars():
#     america_star(8,"white")
#     arrangment()
#     america_star(8,"white")
#     arrangment()
#     america_star(8,"white")
#     arrangment()
#     america_star(8,"white")
#     arrangment()
#     america_star(8,"white")
#     arrangment()
#     america_star(8,"white")

# Uses the itertools command cycle to alternate the coloring of each letter
# in the word of the country name. Cycle continues to iterate through the list
# and colors each letter differently until all letters in the word have been colored
    
def stripe_write(turtle, string):
    color = cycle(["red", "black", "blue"])

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
    #print(ids)
    if len(ids)<3: 
        index = ids[0]
        color = canvas.itemcget(index, "fill")
#         if color != '':
#             print(color.lower())
    if len(ids)>=3: 
        index = ids[-2]
        color = canvas.itemcget(index, "fill")
#         if color != '':
#             print(color.lower())
    usertext(color)
    
def texttextbox(color,xposition,yposition,length,width):
    turtle.setposition(xposition,yposition)
    turtle.begin_fill()
    turtle.color(color)
    turtle.down()
    for i in range(2):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
    turtle.up()
    turtle.end_fill()
    
    
def usertext(color):
    turtle.up()
    if color=="#ff0000":
        x1=0
        y1=250
        turtle.setposition(x1,y1) 
        turtle.down()
        turtle.color("red")
        turtle.write(" Red symbolizes hardiness and valor",align="center",font=("Times New Roman", 20, "normal"))
        turtle.up()
    elif color=="#ffffff":
        texttextbox("brown",-220,166,445,80)
        
#         turtle.setposition(-220,166)
#         turtle.begin_fill()
#         turtle.color("brown")
#         turtle.down()
#         turtle.forward(445)
#         turtle.left(90)
#         turtle.forward(80)
#         turtle.left(90)
#         turtle.forward(445)
#         turtle.left(90)
#         turtle.forward(80)
#         turtle.left(90)
#         turtle.up()
#         turtle.end_fill()
        
        
        x1=0
        y1=170
        turtle.setposition(x1,y1) 
        turtle.down()
        turtle.color("white")
        turtle.write(" The 13 red and white strips symbolize\n the 13 original colonies",align="center",font=("Times New Roman", 20, "normal"))
        turtle.up()
        
    elif color=="white":
        texttextbox("grey",-220,65,445,80)
#         turtle.setposition(-220,65)
#         turtle.begin_fill()
#         turtle.color("grey")
#         turtle.down()
#         turtle.forward(445)
#         turtle.left(90)
#         turtle.forward(80)
#         turtle.left(90)
#         turtle.forward(445)
#         turtle.left(90)
#         turtle.forward(80)
#         turtle.left(90)
#         turtle.up()
#         turtle.end_fill()
        
        
        x1=0
        y1=75
        turtle.setposition(x1,y1) 
        turtle.down()
        turtle.color("white")
        turtle.write("White symbolizes purity and innocence.\nThe 50 stars represent the 50 states",align="center",font=("Times New Roman", 20, "normal"))
        turtle.up()
        
    elif color=="blue":
        x1=0
        y1=25
        turtle.setposition(x1,y1) 
        turtle.down()
        turtle.color("blue")
        turtle.write(" Blue symbolizes vigilance, perseverance, and justice",align="center",font=("Times New Roman", 20, "normal"))
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
#     print(xclick)
#     print(yclick)

def draw_star_five(position1,position2):
    turtle.setposition (position1,position2)
    five_stars()
    turtle.pu()
    turtle.home()
    
def draw_star_six(position1,position2):
    turtle.setposition (position1,position2)
    six_stars()
    turtle.pu()
    turtle.home()

########################## BEGIN MAIN FUNCTION ################################

def main():

    # Creates the rectangular border 
    
    border(150,"black")

    # Brings the turtle to home position 

    x1=0
    y1=0
    turtle.setpos(x1,y1)

    # Determines the width of the 13 stripes

    height = 150
    stripwidth = height / float(13)
    turtle.speed(100)

    x1=0
    y1=0-stripwidth

    # Draws the stripes and alternates the colors of them. Note that the
    # last line brings the turtle below along the height based on the width of
    # each strip after each successive iteration #

    for i in range(13):
        if i%2 ==0:
            r = 1
            g = 0
            b = 0
        else:
            r = 1
            g = 1
            b = 1
        
        turtle.pu()
        turtle.setheading(90)
        turtle.pd()
        turtle.setpos(x1,y1)
        turtle.color(r,g,b)
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

    turtle.pu()

# Brings the turtle again to the home #

    x1=0
    y1=0
    turtle.setposition(x1,y1)
    turtle.pd()
    turtle.setheading(90)

### Draws the blue rectangle ###

    draw_blue(150)

# Row one. Draws the stars and then sets them based on the arrangment function 
    draw_star_six(5,-4)
#     x1 = 5
#     y1 = -4
#     turtle.setposition (x1,y1)
#     six_stars()
#     turtle.pu()
#     turtle.home()
    
# Row two
    draw_star_five(15,-12)

#     x1=15
#     y1=-12
#     turtle.setposition (x1,y1)
#     five_stars()
#     turtle.pu()
#     turtle.home()

# Row three
    draw_star_six(5,-20)
#     x1=5
#     y1=-20
#     turtle.setposition (x1,y1)
#     six_stars()
#     turtle.pu()
#     turtle.home()

# Row four    
    draw_star_five(15,-28)

#     x1=15
#     y1=-28
#     turtle.setposition (x1,y1)
#     five_stars()
#     turtle.pu()
#     turtle.home()

# Row five    
    draw_star_six(5,-36)
    
#     x1=5
#     y1=-36
#     turtle.setposition (x1,y1)
#     six_stars()
#     turtle.pu()
#     turtle.home()

# Row six
    draw_star_five(15,-44)

#     x1=15
#     y1=-44
#     turtle.setposition (x1,y1)
#     five_stars()
#     turtle.pu()
#     turtle.home()

# Row seven
    draw_star_six(5,-52)
#     x1=5
#     y1=-52
#     turtle.setposition (x1,y1)
#     six_stars()
#     turtle.pu()
#     turtle.home()

# Row eight
    draw_star_five(15,-60)
    
#     x1=15
#     y1=-60
#     turtle.setposition (x1,y1)
#     five_stars()
#     turtle.pu()
#     turtle.home()

# Row nine
    draw_star_six(5,-68)
    
#     x1=5
#     y1=-68
#     turtle.setposition (x1,y1)
#     six_stars()
#     turtle.pu()
#     turtle.home()
    
# Prints USA
    x1 = -75
    y1 = -250
    turtle.setposition(x1,y1)
    stripe_write(turtle, "USA")
    
# Print the instructions  
    turtle.color("black")
    x1 = -175
    y1 = -100
    turtle.setposition(x1,y1)
    turtle.write(" Click on a feature of the\n flag to learn more about it!",align="center",font=("Times New Roman", 20, "normal"))

    xclick = 0
    yclick = 0

    # Extracts the point that the user clicks on and allows them to play with the flag interactively.
    
    getcoordinates()

    # No more drawings - we are done!  
    
    turtle.done()
    
main()

############################# END MAIN FUNCTION ################################

