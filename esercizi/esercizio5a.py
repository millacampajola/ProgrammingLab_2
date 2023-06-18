class CSVFile():
    
    def __init__(self, name):
        self.name = name
        
    def get_data(self):
        try: # apro il file, se è vuoto catturo l'errore
            my_file = open(self.name, 'r')
        except Exception as e:
            print('Errore: {}' .format(e))
        
        lista = []
        
        for line in my_file:
            elements = line.split(',')
            
            if line == 'Date,Sales\n':
                elements = None
            else:
                line = line.strip('\n')
                elements = line.split(',')
                lista.append(elements)

        my_file.close()
        return lista

# csv_file = CSVFile('shampoo_sales.csv')
# csv_file = CSVFile('vuoto.csv')
# dati = csv_file.get_data()
# print(dati)

# controllo nell' __init__:
# def __init__(self, name):
# self.name = name
# try:
# self.my_file = open(self.name ,'r')
# except Exception as e:
# print('il mio errore è: "{}".'.format(e))