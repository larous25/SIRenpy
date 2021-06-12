# import turtle 

greenColor = "#50fa7b"
blackColor = "#202426"
whiteColor = "#f8f8f2"
redColor = "#ff5555"
pinkColor = "#ff79c6"
cyanColor = "#8be9fd"
yellowColor = "#f1fa8c"
class Computer:
    def __init__(self, t=None):
        self.t = t
        # self.t = turtle.RawTurtle(t)
        self.state = 0
    def setState(self, state):
        self.state = state


    def draw(self, x, y): 
        # centro de la pantalla
        if self.state == 0:
            self.healthy (x, y)
        elif self.state == 1:
            self.infected(x, y)
        elif self.state == 2:
            self.recovered(x, y)

    def healthy (self, x, y):
        self.t.create_rectangle(x, y, x+50, y+35, fill=blackColor)
        self.t.create_rectangle(x+3, y+3, x+47, y+27, fill=whiteColor)
        # final de la pantall
        self.t.create_rectangle(x+23, y+35, x+27, y+40, fill=blackColor)
        self.t.create_rectangle(x+15, y+38, x+35, y+40, fill=blackColor)
        # led de la pantalla
        self.t.create_rectangle(x+3, y+28, x+6, y+32, fill=whiteColor)
        # texto pantalla
        self.t.create_text(x+13, y+13, text="$_", font=("Helvetica", 8), fill=greenColor)

    def infected (self, x, y):
        self.t.create_rectangle(x, y, x+50, y+35, fill=blackColor)
        self.t.create_rectangle(x+3, y+3, x+47, y+27, fill=pinkColor)
        # final de la pantall
        self.t.create_rectangle(x+23, y+35, x+27, y+40, fill=blackColor)
        self.t.create_rectangle(x+15, y+38, x+35, y+40, fill=blackColor)
        # led de la pantalla
        self.t.create_rectangle(x+3, y+28, x+6, y+32, fill=redColor)
        # texto pantalla
        self.t.create_text(x+13, y+13, text="$_", font=("Helvetica", 8), fill=whiteColor)
        
    def recovered (self, x, y):
        self.t.create_rectangle(x, y, x+50, y+35, fill=blackColor)
        self.t.create_rectangle(x+3, y+3, x+47, y+27, fill=cyanColor)
        # final de la pantall
        self.t.create_rectangle(x+23, y+35, x+27, y+40, fill=blackColor)
        self.t.create_rectangle(x+15, y+38, x+35, y+40, fill=blackColor)
        # led de la pantalla
        self.t.create_rectangle(x+3, y+28, x+6, y+32, fill=yellowColor)
        # texto pantalla
        self.t.create_text(x+13, y+13, text="$_", font=("Helvetica", 8), fill=whiteColor)
        