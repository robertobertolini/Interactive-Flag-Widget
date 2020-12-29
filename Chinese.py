
# coding: utf-8

# In[13]:

# Roberto Bertolini and Tiffany Roberti

# This py file draws the American Flag using the turtle Graphics package 
# in Python. The program first draws the flag and then the user can learn
# more about the meaning of the symbols of the flag by clicking on them. 

# Subfunctions:

    # border
        # input: height,color
            # Draws the rectangular shape of the flag using the height and 
            # width specifications of the border
    # big_star
        # input: vertices, steps, length
            # Draws the big yellow star in the red rectangle
    # chinese_star
        # input: size, color, angle
            # Draws the four smaller stars at the specified angles in the flag       
    # draw_littlestar
        # input: x_coordinate,y_coordinate
            # Command one of the little stars at a specified position
    # strip_write
        # input: turtle, string
            # Takes the string of the flag's name (U.S.A.) and alternates the color of 
            # each letter in the word
    # textbox_click
        # input: x and y coordinates
            # Retrieves the color of the point that the user clicks on and prints the 
            # corresponding meaning of the color to the user on the Turtle graphics window
    # texttextbox
        # input: color, x_position, y_position, length, and width of rectangle to be drawn
            # Creates a textbox around the white text that characterizes the white parts of 
            # the flag to make it easier for the user to read.
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
from itertools import cycle
#import matplotlib

# The function "border" draws the flag's border

def border(height,color):
    
    # turtle.begin_fill gets the height and length dimensions.
    
    height = float(height)
    length = height *(1.9)
    length = round(length,2)
    
    # Draws a rectangle. Note that forward corresponds to drawing by the pointer
    # in a straight line and right means we turn to the right at a 90 degree angle.
    # This is done four times for the polygon.
    turtle.begin_fill()
    turtle.color(color)
    turtle.down()
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
    turtle.end_fill()

# Creates the big star with a specified length and then fills in the star with
# the yellow color
    
def big_star(vertices, steps, length):
    turtle.color("gold")
    turtle.begin_fill()
    for i in range(vertices):
        turtle.forward(length)
        turtle.right(steps*360.0/vertices)
    turtle.end_fill()

# Creates the smaller stars with the specified orientation and angle  
    
def chinese_star(size,color,angle): 

    turtle.speed(300)
    size= float(size)
    turtle.right(90)
    turtle.begin_fill()
    turtle.color(color)
    turtle.down()
    
    for i in range(5):
        turtle.forward(size)
        turtle.left(angle)
    
#     turtle.forward(size)
#     turtle.left(angle)
#     turtle.forward(size)
#     turtle.left(angle)
#     turtle.forward(size)
#     turtle.left(angle)
#     turtle.forward(size)
#     turtle.left(angle)
#     turtle.forward(size)
#     turtle.left(angle)
    turtle.end_fill()       
    
def draw_littlestar(position_x,position_y):
    turtle.setposition(position_x,position_y)
    turtle.down()
    chinese_star(15,"gold",144)
    turtle.up()

# Uses the itertools command cycle to alternate the coloring of each letter
# in the word of the country name. Cycle continues to iterate through the list
# and colors each letter differently until all letters in the word have been colored    

def stripe_write(turtle, string):
    color = cycle(["red", "gold"])

    for character in string:
        turtle.color(next(color))
        turtle.write(character, move=True, font=("Times New Roman", 48, "normal"))

# This function takes the x and y coordinate that the user clicks on and uses the 
# getcanvas() method to retrieve the color of the point the user clicks on. Depending
# on the color and location, the program will display the meaning of the symbol to the user
# after the flag and instructions.
        
def textbox_click(rawx,rawy):
    print(rawx,rawy)
    turtle.up()
    turtle.setposition(rawx,rawy)
    turtle.down()
    
    # Specifies the coordinates of the smaller stars inside the 
    # red rectangle
    
    inside = (
        (77.0<=rawx<=80.0 and 77.0<=rawy<=80.0) 
        or (78.0<=rawx<=80.0 and -18.0<=rawy<=-15.0) 
        or (96.0<=rawx<=99.0 and -62.0<=rawy<=-58.0) 
        or (96.0<=rawx<=99.0 and -37.0<=rawy<=-32.0) 
        or (34.0<=rawx<=49.0 and -44.0<=rawy<=-36.0)
             )
    rawy = -rawy
    
    # If the user clicks on one of the gold stars
    
    if inside:
        color = "gold"
        print(color)
        
    # Uses the getcanvas() method to retrieve the color of the 
    # point the user clicks on. Depending on the color and location, 
    # the program will display the meaning of the symbol to the user
    # after the flag and instructions.    
        
    else:
        canvas = turtle.getcanvas()
        canvas.pack(fill="both", expand=True)
        ids = canvas.find_overlapping(rawx, rawy, rawx, rawy)
#         print(type(rawx))
#         print(ids)
        if len(ids) >= 3: 
            index = ids[-2]
            color = canvas.itemcget(index, "fill")
#             if color != '':
#                 print(color.lower())
        if len(ids) == 2: 
            index = ids[0]
            color = canvas.itemcget(index, "fill")
#             if color != '':
#                 print(color.lower())
    usertext(color)

# For colors (in this case white) that cannot be seen because of the light background,
# this function draws a textbox with the corresponding dimensions at a specified position 
# as the text so the user does not have any problems reading it visually.

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
    
# Displays the symbolic meaning of the color that is clicked on as text above the flag
# at a specified position
    
def usertext(color):
    turtle.up()
    if color=="red":
        #eraseble.clear()
        x1=0
        y1=250
        turtle.setposition(x1,y1) 
        turtle.down()
        turtle.color("red")
        turtle.write(" Red symbolizes the Communist Revolution",align="center",font=("Times New Roman", 20, "normal"))
        turtle.up()
    elif color=="gold":
        
        # Since it is hard to see gold on a white background, we create a 
        # grey rectangle so the text can be easily displayed to the user.
        texttextbox("grey",-250,15,500,190)
#         turtle.setposition(-250,15)
#         turtle.begin_fill()
#         turtle.color("grey")
#         turtle.down()
#         turtle.forward(500)
#         turtle.left(90)
#         turtle.forward(190)
#         turtle.left(90)
#         turtle.forward(500)
#         turtle.left(90)
#         turtle.forward(190)
#         turtle.left(90)
#         turtle.up()
#         turtle.end_fill()
        
        x1=0
        y1=15
        turtle.setposition(x1,y1) 
        turtle.down()
        turtle.color("gold")
        turtle.write(" The large star symbolizes the\n Communist Party of China. The four\n smaller stars symbolize the four\n social classes: the working class,\n the peasantry, the urban petite\n bourgeoisie and the national bourgeoisie", font=("Arial", 20, "normal"), align="center")
        turtle.up()
        
# Uses the command "onscreenclick" to extract the x and y coordinate
# that the user clicked on
            
def getcoordinates():
    turtle.onscreenclick(turtle.goto)
    turtle.onscreenclick(modifyglobalvariables) # Here's the change!
    turtle.onscreenclick(textbox_click)

# Updates the location that the user clicks on    
    
def modifyglobalvariables(rawx,rawy):
    global xclick
    global yclick
    xclick = int(rawx//1)
    yclick = int(rawy//1)
#     print(xclick)
#     print(yclick)
    
########################## BEGIN MAIN FUNCTION ################################

def main():

# Creates the border

    border(150,"red") 
    turtle.begin_fill()
    turtle.down()
    turtle.color("red")
    turtle.up()

# Creates the big star

    x1=15
    y1=-33
    turtle.setposition(x1,y1) 
    big_star(5,2,50)
    turtle.begin_fill()
    turtle.down()
    turtle.color("gold")
    turtle.up()

# Creates the second star
    draw_littlestar(95,-25)
#     x1 = 95
#     y1=-25
#     turtle.setposition(x1,y1)
#     turtle.down()
#     chinese_star(15,"gold",144)
#     turtle.up()

# Creates the third star
    draw_littlestar(105,-58)
#     x1 = 105
#     y1=-58
#     turtle.setposition(x1,y1)
#     turtle.down()
#     chinese_star(15,"gold",144)
#     turtle.up()

# Creates the first star
    draw_littlestar(82,-24)
#     x1 = 82
#     y1=-24
#     turtle.setposition(x1,y1)
#     turtle.down()
#     chinese_star(15,"gold",144)
#     turtle.up()

# Creates the fourth star
    draw_littlestar(70,-80)
#     x1 = 70
#     y1=-80
#     turtle.setposition(x1,y1)
#     turtle.down()
#     chinese_star(15,"gold",144)
#     turtle.up()
#     turtle.home()

# Prints "China"

    x1 = -120
    y1 = -250
    turtle.setposition(x1,y1)
    stripe_write(turtle, "CHINA")    

# # Print the instructions 

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

