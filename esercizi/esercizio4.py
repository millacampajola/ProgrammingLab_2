class CSVFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):
        my_file = open(self.name, 'r')
        lista = [] 

        if my_file == []:
            return None
            
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
# dati = csv_file.get_data()
# print(dati)

                