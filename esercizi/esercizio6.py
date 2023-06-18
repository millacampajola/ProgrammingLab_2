class CSVFile:

    def __init__(self, name):
        self.name = name

        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))

        if isinstance(self.name, int):
            raise Exception('Il nome del file non è una stringa')
        
    def get_data(self, start=None, end=None):
        if not self.can_read: # se ritorna False significa che nell' __init__ non è stato aperto il file correttamente
            print('Errore, file non aperto o illeggibile')
            return None

        else:
            data = []
            my_file = open(self.name, 'r')
            
            for line in my_file:
                line = line.strip('\n')
                elements = line.split(',')
                if elements[0] != 'Date':
                    data.append(elements)
            
            my_file.close()
            return data

class NumericalCSVFile(CSVFile):
    
    def get_data(self):
        string_data = super().get_data()
        numerical_data = []
        
        for string_row in string_data:
            numerical_row = []
            
            for i, element in enumerate(string_row):
                
                if i == 0:
                    numerical_row.append(element)
                    
                else:
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break
                
            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)

        return numerical_data

csv_file = CSVFile('shampoo_sales.csv')
print('Nome del file: "{}"'.format(csv_file.name))
print('Dati contenuti nel file: "{}"'.format(csv_file.get_data()))

csv_file_numerico = NumericalCSVFile('shampoo_sales.csv')
print('Nome del file: "{}"'.format(csv_file_numerico.name))
print('Dati contenuti nel file: "{}"'.format(csv_file_numerico.get_data()))