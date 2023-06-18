# TESTING: fase in cui si verifica il corretto funzionamento del tutto o delle parti in varia condizioni di interesse
# - testing end to end: test automatico che determina se l'intero codice funziona nel modo corretto 
# - Unit testing: testing di un'unità minima del programma
# pseudocodice: esempio di un generico concetto di testing
# dato un input e un output noto
# input noto -> CODICE -> output  
# if output != output noto:
#    errore!
# si confronta un output con uno precalcolato che si considera corretto, se non corrispondonok, si lancia un errore

# esempio:
def somma(a, b):
    return a+b
# testing
if not somma(1,1) == 2:
    raise Exception('Test 1+1 non passato')
if not somma(1.5, 2.5) == 4:
    raise Exception('Test 1.5+2.5 non passato')

# ----------------------------------------------
# test lezione7.py

import unittest 
from lezione7 import somma 

# testing 
class TestSomma(unittest.TestCase):

    def test_somma(self):
        self.assertEqual(somma(1,1), 2)
        self.assertEqual(somma(1.5,2.5), 4)
#-----------------------------------------------
# assertEqual() si può anche sostituire con assertTrue() -> per verificare una condizione booleana; oppure assertRaises() -> per verificare che una particolare eccezione viene lanciata

# per lanciare un processo di test si scrive da linea di comando:
# python -m unittest discover 
# per avere più informazioni posso aggiungere '-v'

# esempio con oggetto CSVFile:
import unittest 
from esame import CSVFile

class TestCSVFile(unittest.TestCase):

    def test_init(self):

        csv_file = CSVFile('shampoo_sales.csv')
# controllo che il nome del file sia stato salvato in un attributo dell'oggetto di nome "name"
        self.assertEqual(csv_file.name, 'shampoo_sales.csv')

# test-driven: prima scrivo i test, poi il codice
