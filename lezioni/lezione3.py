# files:
# estensioni più comuni .csv, .txt
# CSV: ogni riga è una entry, è possibile inserire un'intestazione per dare un nome alle colonne
# open('nome_file', 'modalità'): per aprire un file
# modalità: 'r' -> read, 'w' -> write (sovrascrivo il file), 'rw' -> read and write, 'a' -> append (le entry vengono aggiunte alle fine del file)
# close(): per chiudere un file
# read(): legge l'intero file e lo passa sotto forma di stringa
# readline(): legge una riga per volta e la passa sotto forma di stringa
# apro il file in modalità lettera e ne stampo i primo 50 caratteri e lo chiudo
my_file = open('shampoo_sales', 'r')
print(my_file.read()[0:50])
my_file.close()
# oppure:
my_file = open('shampoo_sales', 'r')
my_file_contents = my_file.read() # leggo contenuto
if len(my_file_contents) > 50:
    print(my_file_contents[0:50] + '...')
else:
    print(my_file_contents)
my_file.close()
# oppure: (leggo riga per riga)
my_file = open('shampoo_sales.csv', 'r')
for i in range(5):
    print(my_file.readline())
# oppure:
my_file = open('shampoo_sales', 'r')
for line in my_file:
    print(line)
my_file.close()

# per scrivere su un file dopo averlo aperto in modalità 'w', uso la funzione write() 

# leggere i valori di un file CSV:
# 1. metodo '.split' per separare le stringhe su uno specifico carattere
mia_stringa = 'Ciao, come va?'
lista_elementi = mia_stringa.split(',')
# 2. conversione di una stringa a valore numerico (casting)
mia_stringa = '5.5'
mio_numero = float(mia_stringa) # oppure: int, str
# 3. saper aggiungere un elemento ad una lista
mia_lista = [1,2,3]
mia_lista.append(4) # aggiunge un elemento alla fine della lista, modificandone la lunghezza

# leggere informazioni da un file CSV e trascriverle su una lista
values = []
dates = [] # inizializzo liste vuote per saolvare i valori
my_file = open('shampoo_sales.csv', 'r')
for line in my_file:
    elements = line.split(',')
# se non sto processando l'intestazione...
    if elements[0] != 'Date':
        date = elements[0]
        value = elements[1]

        dates.append(date)
        values.append(value)
