# funzione print()
print('Hello, world!')
x = 'there'
print('hello, {}!' .format(x))

# tipi di dati
my_var = 1 # tipo int
my_var = 1.1 #tipo float
my_var = 'ciao' # tipo str
my_var = True # tipo booleano
my_var = None # tipo 'niente'

type(my_var) is int # oppure: float, str, bool, None (controllo il tipo di dato)

# accedere alle stringhe
mia_stringa = [1,2,3,4,5]
mia_stringa[2] # 3° carattere della stringa
mia_stringa[-1] # penultimo carttere della stringa

# slicing 'tagliare una fetta di stringa'
mia_stringa[0:50] # dal 1° al 50° carattere
mia_stringa[0:-1] # dal 1° al penultimo

# operatori di confronto: ritornano True o False

# % -> ritorna il modulo, ossia il resto della divisione x/y

# liste (oggeti possono anche essere diversi)
my_list = [1,2,3] # lista di numeri
my_list = ['Marco','Irene', 'Paolo'] # lista di stringhe

# operatori di appartenenza (in, not in)

# dizionari (permette di associare un valore ad una key)
my_dict = {'Trieste': 34100, 'Padova': 35100} # dizionario di numeri
my_dict = {'Trieste': 'TS', 'Padova': 'PD'} # dizionario di stringhe
# accedere ai valori di un dizionario
CAP_ts = my_dict['Trieste'] #assegno alla variabile il valore legato alla key 'Trieste'
# gli operatori di appartenenza agiscono sulle chiavi

# istruzioni condizionali (la riga contenente l'istruzione condizionale termina con i due punti)
#esempio costrutto if
your_var = 3
if (my_var > your_var):
    print('My var is bigger than yours')
    if (my_var-your_var) <= 1:
        print('... but not so much')
# esempio costrutto elif (comprime else if)
if (my_var > your_var):
    print('My var is bigger than yours')
    if (my_var-your_var) <= 1:
        print('... but not so much')
    elif (my_var-your_var) <= 5:
        print('...quite a bit')
    else:
        print('... a lot')

# cicli for e while
for item in my_list: # ogni item è preso in modo ordinato
    print(item)

i = 0
while i < 10:
    print(i)
    i = i+1

for i in range(10):
    print(i)
# funzione range(), crea una lista di numeri 
list_01 = range(10) # lista di numeri da 1 a 10
list_02 = range(3, 10) # lista di numeri da 3 a 9
list_03 = range(3, 10, 2) # lista di numeri da 3 a 9, con passo 2: [3,5,7,9]
# funzione enumerate(): ritorna sia l'elemento che il suo indice nella lista sotto forma di tupla (unione di 2 valori)
for i, item in enumerate(my_list):
    print('Poszione {}: {}' .format(i, item))

# funzioni: dichiarate con 'def' e seguite da i due punti, 'return' alla fine del blocco di istruzioni, precede i valori da ritornare alle chiamate
def mia_funzione(argomento1, argomento2):
    print('Argomenti: {} e {}' .format(argomento1, argomento2))
# chiamata
mia_funzione('Pippo', 'Pluto')
# funzione con return
def eleva_al_quadrato(numero):
    return numero*numero
#chiamata
risultato = eleva_al_quadrato(4)
print('Risultato: {}' .format(risultato))
#funzioni built-in: https://docs.python.org/3/library/functions.html

# SCOPE: local, enclosing, global, built-in

# funzione deve agire solo su variabili locali, esempio:
def eleva_al_quadrato(numero):
    risultato = numero*numero
    return risultato
# tornare sempre risultato della funzione con return(), esempio:
risultati = []
def eleva_al_quadrato(numero):
    risultato = numero*numero
    return risultato
risultati.append(eleva_al_quadrato(3))

# moduli
#esempio: importare funzione sqtr dal modulo math
import math
var = math.sqrt(4)
# oppure:
import math as m
var = m.sqrt(4)
# oppure:
from math import sqrt 
var = sqrt(4)

# controllare se c'è un elemento nella lista:
my_list = ['Marco', 'Irene', 'Paolo']
if 'Marco' in my_list:
        print('ho trovato Marco')