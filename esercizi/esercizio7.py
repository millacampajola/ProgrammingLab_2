import unittest
from esercizio6 import CSVFile
from esercizio6 import NumericalCSVFile

class TestCSVFile(unittest.TestCase):
    
    def test_init(self):
        csv_file = CSVFile('shampoo_sales.csv')
        self.assertEqual(csv_file.name, 'shampoo_sales.csv')

    def test_get_data(self):
        if type(csv_file.get_data()) is not list:
            raise Exception('Il tipo di valore tornato dalla funzione è errato')