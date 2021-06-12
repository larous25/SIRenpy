#Autor: Brian E. Bustos

# import turtle
import tkinter as tk
from tkinter import ttk

from computer import Computer
from sir import Logic


# constantes 
# color de la letra
whiteColor = 'white'
# color fondo
colorTwo = '#282a36'
blueColor = '#6272a4'
colorFive = '#44475a'

# algunas letras
colorFour = '#bd93f9'
redColor = "#ff5555"
yellowColor = '#f1fa8c'

# clase principal
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg=colorTwo)
        self.master = master
        #
        self.puntos = []

        self.computers = list()
        self.pack()
        # izquierdo
        self.leftFrame = tk.Frame(self, relief="sunken", borderwidth=1, bg=blueColor)
        self.leftFrame.grid(column=0,row=0, sticky="ns")
        # godo
        self.rightFrame = tk.Frame(self, relief="sunken", borderwidth=1, bg=blueColor)
        self.rightFrame.grid(column=1,row=0)
        # cantidad de dias
        self.days = 0
        self.maximumDays = 60
        self.createWidgets()

    def createWidgets(self):

        # cantidad de infectados
        self.numberTitleLabel = tk.Label(self.leftFrame, text="Número de infectados", bg=colorTwo, fg=whiteColor, bd=10, relief="flat")
        self.numberTitleLabel.pack(side="top", pady=5)

        self.numberInfectedSpin = tk.Spinbox(
            self.leftFrame, 
            from_=0, to=100, 
            width=5, 
            bg=colorFive, 
            fg=colorFour, 
            bd=10, 
            relief="flat", 
            validate="key",
            validatecommand=(self.register(self.onValidationKeyInfection), "%P")
        )
        self.numberInfectedSpin.pack(side="top", pady=5)

        # cantidad de personas
        self.totalTitleLabel = tk.Label(self.leftFrame, text='Número de computadores', bg=colorTwo, fg=whiteColor, bd=10, relief="flat")
        self.totalTitleLabel.pack(side="top", pady=5)
    
        self.populationSpin = tk.Spinbox(
            self.leftFrame, 
            from_=1, to=100, 
            width=5, 
            bg=colorFive, 
            fg=colorFour, 
            bd=10, 
            relief="flat",
            validate="key",
            validatecommand=(self.register(self.onValidationKeyPoblation), "%P")
        )
        
        self.populationSpin.pack(side="top", pady=5)
    
        # boton para iniciar la simulacion
        self.initSimulation = tk.Button(self.leftFrame, bg=blueColor, fg=colorFour, bd=10, relief="flat")
        self.initSimulation["text"] = "Iniciar"
        self.initSimulation["command"] = self.run
        self.initSimulation.pack(side="bottom", pady=20)


        #PARTE DERECHA
        self.canvas = tk.Canvas(self.rightFrame, width = 1000, height = 800, relief = tk.FLAT)
        self.canvas.pack()

    def addProgress (self):
        if (self.days < self.maximumDays):
            sir = self.puntos[self.days]
            s = round(sir[0])
            i = round(sir[1])
            r = round(sir[2])
            print(s, i, r)
            self.draw(self.makeComputersGrayAgain(int(self.populationSpin.get()), i, r))
            self.days += 1
            self.progre["value"] = self.days
            self.daysGone["text"] = "Días:" + str(self.days)
        

    def lessProgress (self):
        if (self.days > 0):
            sir = self.puntos[self.days]
            s = round(sir[0])
            i = round(sir[1])
            r = round(sir[2])
            self.draw(self.makeComputersGrayAgain(int(self.populationSpin.get()), i, r))
            self.days -= 1
            self.progre["value"] = self.days
            self.daysGone["text"] = "Días:" + str(self.days)

    # Nota: Pendiente agregar que no se pueda colocar mayor numero
    # infectados que de computadores full
    def onValidationKeyInfection (self, p):
        if p.isdigit():
            if int(p) not in range(0, 100):
                return False
        elif p == "":
            return True    

        return p.isdigit()

    def onValidationKeyPoblation (self, p):
        if p.isdigit():
            if int(p) not in range(1, 100):
                return False
        elif p == "":
            return True    

        return p.isdigit()


    def jls_extract_def(self, pcs, rango):
        if pcs > rango: 
            rango +=1 
        else: 
            rango = pcs
        return rango

    def showPlot (self):
        self.logic.makePlot(self.puntos)

    def run(self):
        self.logic = Logic(int(self.populationSpin.get()), int(self.numberInfectedSpin.get()), 60)
        self.puntos = self.logic.makeData()

        self.daysGone = tk.LabelFrame(
            self.canvas,
            text="Días:0",
            bg=colorTwo,
            fg=yellowColor,
            bd=10, 
            relief="flat",
            font=("Verdana",24)
        )
        self.daysGone.place(
            x=650, y=35,
            width=170, 
            height=40, 
        )
        s = ttk.Style()
        s.theme_use('alt')
        s.configure("red.Horizontal.TProgressbar", foreground=redColor, background=redColor)

        self.progre = ttk.Progressbar(
            self.canvas,
            style="red.Horizontal.TProgressbar",
            orient='horizontal', 
            length = 600, 
            maximum = self.maximumDays,
            mode = 'determinate'
        )
        self.progre.place(x=100, y=765)

        # Botones 
        bdButton = 2
        

        self.addControl = tk.Button(
            self.canvas, 
            bg=blueColor, 
            fg=colorFour, 
            bd=bdButton, 
            relief="flat"
        )
        self.addControl["text"] = "-"
        self.addControl["command"] = self.lessProgress
        self.addControl.place(x=50, y=750)

        self.lessControl = tk.Button(
            self.canvas, 
            bg=blueColor, 
            fg=colorFour, 
            bd=bdButton, 
            relief="flat"
        )
        self.lessControl["text"] = "+"
        self.lessControl["command"] = self.addProgress
        self.lessControl.place(x=700, y=750)

        self.graphControl = tk.Button(
            self.canvas, 
            bg=blueColor, 
            fg=whiteColor, 
            bd=bdButton, 
            relief="flat"
        )
        self.graphControl["text"] = "Gráfica"
        self.graphControl["command"] = self.showPlot
        self.graphControl.place(x=750, y=750)
        self.draw(self.makeComputersGrayAgain(int(self.populationSpin.get()), int(self.numberInfectedSpin.get()), 0))

    def draw(self, pcs):
        self.canvas.update()
        self.canvas.delete("all")
        rango = 0
        pox = 0
        pc= 0
        while pcs > 0:
            pcs -= rango
            x = 500 - (pox*50)
            # NOTA: arreglar el rango maximo
            for i in range(rango, 0, -1):
                self.computers[pc].draw(x, pox*50)
                pc += 1
                x += 100
            pox += 1 
            rango = self.jls_extract_def(pcs, rango)


    def makeComputersGrayAgain (self, population, infected, r):
        self.computers = []
        for i in range(population):
            self.computers.append(Computer(self.canvas))
        for i in range(r):
            self.computers[i].setState(2)
        if infected > 0:    
            for i in range(r, (r+infected), 1):
                self.computers[i].setState(1)
        return population

# frame main ventana 
window = tk.Tk()
window.title("Simulación de virus de computadora")
window.geometry('1200x800')
window.configure(bg=colorTwo)
app = Application(master=window)
app.mainloop()




