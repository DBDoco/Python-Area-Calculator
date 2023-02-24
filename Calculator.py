# Izradio: Dominik Bedenic (github.com/DBDoco)

from sympy import *
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
import warnings

# Sakrivanje upozorenja koje nastaje zbog korijena iz negativnog broja
warnings.filterwarnings('ignore')

# Funkcija parabole                                                             
def parabola(x):
    return x**2

# Funkcija kružnice
def kruznica(x):
    return np.sqrt(2-x**2)

#-------- RAČUNANJE POVRŠINE --------#

# Računanje sjecišta između parabole i kružnice
x, y = symbols('x y')
parabola_eq = Eq(x**2, y)
kruznica_eq = Eq(x**2 + y**2, 2)
sjecista = solve((parabola_eq, kruznica_eq), (x, y))

# Određeni integral (od -1 do 1 po x osi) od gornje krivulje.
integral_gornje_krivulje, _ = integrate.quad(kruznica, sjecista[0][0], sjecista[1][0])

# Određeni integral (od -1 do 1 po x osi) od donje krivulje.
integral_donje_krivulje, _ = integrate.quad(parabola, sjecista[0][0], sjecista[1][0])

# Za računanje površine trebamo razliku određenog integrala (od -1 do 1 po x osi) od gornje krivulje odnosno kružnice i određenog integrala (od -1 do 1 po x osi) od donje krivulje odnosno parabole.
povrsina = integral_gornje_krivulje - integral_donje_krivulje

print("Površina između parabole (unutar parabole) i kružnice je: ", povrsina)

#-------------------------------------#


#-------- CRTANJE GRAFOVA I TRAŽENE POVRŠINE --------#

# Definiranje granica koordinatnog sustava
xmin, xmax, ymin, ymax = -4, 4, -4, 4

# Osnovna mjerna jedinica, razmak između pojedine definirane točke na x i y osi
ticks_frequency = 1

# Definicija koordinatnog sustava odnosno figure
fig, ax = plt.subplots(figsize=(10, 10))

# Definiranje osi x i osi y
ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

# Pozicioniranje osi i skrivanje krajnje gornje i desne crte obruba
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Dodavanje naslova za x i y osi
ax.set_xlabel('$x$', size=14, labelpad=-24, x=1.02)
ax.set_ylabel('$y$', size=14, labelpad=-21, y=1.02, rotation=0)
 
# Dodavanje "0" na graf
plt.text(0.49, 0.49,"0", ha='right', va='top',
    transform=ax.transAxes,
         horizontalalignment='center', fontsize=14)

# Određivanje broja i razmaka između pojedine točke na osima
x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
ax.set_xticks(x_ticks[x_ticks != 0])
ax.set_yticks(y_ticks[y_ticks != 0])

# Dodavanje mreže u pozadini
ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

# np.linespace vraća brojeve iz zadanog intervala (-4,4) pogodan za crtanje funkcije
x = np.linspace(-4, 4, 10000)

# Spremanje rješenja funkcije u varijablu. Za kružnicu su posebno izračuanate gornja i donja polutka jer gornja funkcija računa samo gornju polutku. To je zbog toga što np.sqrt() funkcija vraća praznu vrijednost za negativne brojeve
_polukruznica_gornja=kruznica(x)
_polukruznica_donja=-(kruznica(x))
_parabola=parabola(x)

# Određivanje granica površine koja se treba osjenčati. np.where vraća sve vrijednosti koje zadovoljavaju uvjet
presjek = np.where(_parabola <= _polukruznica_gornja)

# Crtanje parabole, gornje i donje polukružnice
plt.plot(x, _parabola, 'r', label='y = x^2')
plt.plot(x, _polukruznica_gornja,'b', label='x^2+y^2=2')
plt.plot(x, _polukruznica_donja, 'b')

# Sjenčanje tražene površine i dodavanje u legendu
plt.fill_between(x[presjek], _parabola[presjek], _polukruznica_gornja[presjek], label='Površina = {}'.format(povrsina), color='gray', alpha=0.5)

# Crtanje legende
plt.legend()

# Spremanje u slike
# plt.savefig('graf.jpg', bbox_inches='tight')

# Prikaz koordinatnog sustava sa svim dodanim komponentama
plt.show()

#-------------------------------------#