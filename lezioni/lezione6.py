# CONTROLLARE GLI INPUT
# per testare gli input si usano: 
# - operatori classici 
# - operatori di identità: IS, IS NOT
var = None
print(var is None) # True se var ha valore None
print(var is not None) # True se var non ha valore None
print(var == '') # True se var è una stringa vuota
# - operatori di membership: IN, NOT IN -> permettono di controllare che il valore della variabile sia presente all'interno di una sequenza
età = 57
print(età in range(30, 40)) # True se età ha un valore tra i 30 e i 39
lettera = 'parola di 7 lettere'
print(lettera not in 'parola') # True se la stringa lettera non è presente in 'parola'

# funzioni legate alla classe

# isinstance(): permette di controllare se un oggetto è istanza di una classe 
print(isinstance(nome_variabile, Classe)) # True se nome_variabile è istanza di Classe

# issubclass(): verifica se una classe è sottoclasse di un'altra, ossia se l'ha ereditata
print(issubclass(SuperClasse, SottoClasse))

# cosa fare se l'input non è corretto
# 1. stampare l'errore ed usare un default per aggirarlo -> errore recoverable
# 2. stampare l'errore o un'eccezione personalizzata ed uscire dal programma -> errore non recoverable (NON si fa MAI nelle funzioni o negli oggetti, SOLO se si sta scrivendo il corpo di un programma iterativo)
# 3. generare (alzare) una nostra eccezione:

# l'operatore RAISE consente di lanciare un'eccezione built-in o custom seguita da un messaggio personalizzato:
raise Exception('Messaggio di errore') # è la stringa che viene stampata a schermo quando l'eccezione sale fino l'interprete Python

# oppure:
raise Exception('Ho avuto un errore, ecco il parametro che lo ha generato: "{}"' .format(parametro))

# come creare un'eccezione:
# si crea l'eccezione custom definendola come classe
class Errore(Exception):
    pass
# si lancia un'eccezione custom
raise Errore('Messaggio di errore')

# sintetizzare gli input: quando sono in una forma simile ad una forma utile

# esempio 1: si vuole controllare se una stringa sesso appartiene ad una lista contenente ['M', 'F']
# si presenta un input con una lettera minuscola ed uno spazio
sesso ='m '

# si trasforma l'input in maiuscolo
sesso = sesso.upper()

# si rimuovono gli spazi
sesso = sesso.strip()

print(sesso in ['M', 'F']) # a questo punto è True
# dall'input sono stati rimossi eventuali errori di formattazione per intercettare l'informazione collegata alla stringa 'M'.