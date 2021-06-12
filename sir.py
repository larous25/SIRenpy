import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

greenColor = "#50fa7b"
redColor = "#ff5555"
cianColor = "#8be9fd"

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt



class Logic (): 
    def __init__ (self, population, infected, maximumDays):
        self.Days = maximumDays
    # Total population, N.
        self.N = population
    # Initial number of infected and recovered individuals, I0 and R0.
        self.I0, self.R0 = infected, 0
    # Everyone else, S0, is susceptible to infection initially.
        self.S0 = self.N - self.I0 - self.R0
    # A grid of time points (in days)
        self.t = np.linspace(0, self.Days, self.Days)
    # Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
        self.beta = 0.2
        self.gamma = 1./10 


    def makeData (self):
        y0 = self.S0, self.I0, self.R0
        return odeint(deriv, y0, self.t, args=(self.N, self.beta, self.gamma))

    def makePlot (self, ret):

        S, I, R = ret.T
        # print(S, I, R)
        # Plot the data on three separate curves for S(t), I(t) and R(t)
        fig = plt.figure(facecolor='w')
        ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
        ax.plot(self.t, S, greenColor, alpha=0.5, lw=4, label='suseptible')
        ax.plot(self.t, I, redColor, alpha=0.5, lw=4, label='Infectado')
        ax.plot(self.t, R, cianColor, alpha=0.5, lw=4, label='Recuperado')
        ax.set_xlabel('Dias pasados')
        ax.set_ylabel('cantidad:' + str(self.N))
        ax.set_ylim(0, self.N)
        ax.yaxis.set_tick_params(length=0)
        ax.xaxis.set_tick_params(length=0)
        ax.grid(b=True, which='major', c='w', lw=1, ls='-')
        legend = ax.legend()
        legend.get_frame().set_alpha(0.5)
        # for spine in ('top', 'right', 'bottom', 'left'):
            # ax.spines[spine].set_visible(False)
        plt.show()


