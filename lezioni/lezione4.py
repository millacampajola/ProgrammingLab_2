# OGGETTI (schema che permette di generare un elemento con le caratteristiche desiderate)
# oggetti definiti con le CLASSI, una volta inizializzati diventano ISTANZE
# METODI: funzioni negli oggetti/classi
# ATTRIBUTI: variabili negli oggetti/classi
# si usano principalemnte perché: permettono di rappresentare bene delle gerarchie (sfruttando caratteristiche comuni); una volta istanziati permettono di mantenere facilmente lo stato

# notazione CamelCase -> per il nome delle classi
# notazione snakecase (caratteri minuscoli e underscore) -> per i nomi dei metodi e delle variabili
# doppi underscore prima e dopo il nome di un metodo -> metodo ad uso esclusivamente interno
# apici: singoli per il codice, doppi nelle stringhe, es:
mystring = 'Il mio nome è "mario" e sono una persona'

# funzione dir(): ritorna una lista con tutti gli attributi di un oggetto
# funzione type(): ritorna la classe dell'oggeto

# operazione in-place -> modifica l'oggetto ritornando None 
my_string = 'a, b, c'
print(my_string.split(',')) # operazione che torna il risultato
print(my_string) # my_string rimane invariata

my_list = [1,2,3,4]
print(my_list)
print(my_list.reverse()) # operazione che modifica l'oggetto, ma non torna niente (None) -> [4,3,2,1]
print(my_list) # my_list modificata

# definire oggetti
# si usa la keyword 'class'
# il costruttore, ossia il metodo usato per inizializzare gli attributi di una classe, si definisce usando __init__
class Person():
    pass # istruzione che serve per avere un blocco vuoto

person = Person() # istanzio una classi di oggetto, creo uno specifico oggetto da una generica definizione 
print(person)

class Person():

    def __init__(self, name, surname): # self "me istanza di classe" -> è obbligatorio come parametro in tutti i metodi degli oggetti

        self.name = name
        self.surname = surname

person = Person('Mario', 'Rossi')
print(person)
print(person.name)
print(person.surname)
#--------------------------------------------------#
class Person():

    def __init__(self, name, surname):

        self.name = name
        self.surname = surname

    def __str__(self): # funzione ad uso interno, è responsabile della rappresentazione in formato stringa dell'oggetto
        return 'Person "{} {}"' .format(self.name, self.surname)

person = Person('Mario', 'Rossi')
print(person)

import random

class Person():

    def __init__(self, name, surname):

        self.name = name
        self.surname = surname

    def __str__(self):
        return 'Person "{} {}"' .format(self.name, self.surname)

    def say_hi(self): # funzione/metodo dell'oggetto (o interfaccia)
        random_number = random.randint(0,2)

        if random_number == 0:
            print('Hello, I am {} {}.' .format(self.name, self.surname))
        elif random_number == 1:
            print('Hi, I am {}!' .format(self.name))
        elif random_number == 2:
            print('Yo bro! {} here!' .format(self.name))

person = Person('Mario', 'Rossi')
person.say_hi()

# estendere oggetti: concetto di ereditarietà -> permette, a partire da una classe genitore, di creare classi figlie che ereditano tutti gli attributi e metodi dalla classe genitore

class Student(Person): # estendo l'oggetto Persona declinandolo in Studente e Professore 

    def __str__(self):
        return 'Student "{} {}"' .format(self.name, self.username)

class Professor(Person):
    def __str__(self): # sovrascrivo la rappresentazione in stringa ell'oggetto Persona
        return 'Prof. "{} {}"' .format(self.name, self.surname)
        
    def say_hi(self): # sovrascrivo il metodo che saluta
        print('Hello, I am professor {} {}.' .format(self.name, self.surname))

# funzione .super() chiama il metodo della classe padre su cui è chiamato

class Professor(Person):
    def __str__(self):
        return 'Prof. "{} {}"' .format(self.name, self.surname)
        
    def say_hi(self):
        print('Hello, I am professor {} {}.' .format(self.name, self.surname))

    def original_say_hi(self):
        super().say_hi()

print('-------------------------------------------')

person = Person('Mario', 'Rossi')
print(person)
person.say_hi()

print('-------------------------------------------')

prof = Professor('Pippo', 'Baudo')

print(prof)
prof.say_hi()
prof.original_say_hi()

print('-------------------------------------------')