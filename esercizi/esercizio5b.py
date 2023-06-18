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

class NumericalCSVFile(CSVFile):

    def get_data(self):
        # chiamo la get_data del genitore
        string_data = super().get_data()
        
        # preparo la lista per contenere i dati in formato numerico
        numerical_data = []

        # ciclo su tutte le "righe" corrispondenti al file originale 
        for string_row in string_data:
            
            # preparo una lista di supporto per salvare la riga in "formato" nuumerico (tranne il primo elemento)
            numerical_row = []
            
            # ciclo su tutti gli elementi della riga con un enumeratore: così ho gratis l'indice "i" della posizione dell'elemento nella riga.
            for i, element in enumerate(string_row):
                
                if i == 0:
                    # il primo elemento della riga lo lascio in formato stringa
                    numerical_row.append(element)
                    
                else:
                    # converto a float tutto gli altri. Ma se fallisco, stampo l'errore e rompo il ciclo (e poi salterò la riga)
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break
                
            # alla fine aggiungo la riga in formato numerico alla lista "esterna", ma solo se sono riuscito a processare tutti gli elementi. Qui controllo per la lunghezza, ma avrei anche potuto usare una variabile di supporto o fare due break in cascata.
            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)

        return numerical_data
        
# csv_file = NumericalCSVFile('shampoo_sales.csv') 
# dati = csv_file.get_data()
# print(dati)