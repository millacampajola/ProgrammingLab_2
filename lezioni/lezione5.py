# eccezioni (errori)
# esempi di eccezzioni:
# ArithmeticError: problemi con il calcolo numerico (FloatingPointError; OverflowError; ZeroDivisionError)
# AttributeError: l'attributo dell'oggetto non esiste
# NameError: variabile non definita, es:
my_var = 'Ciao'
print(mia_variabile) 
#ValueError: la funzione riceve un valore inappropriato, es:
my_var = 'Ciao'
float(my_var)
# SyntaxError
# TypeError

# TRACEBACK: report automatico di Python che serve ad identificare dove è avvenuto un errore -> l'ultima riga mostra l'errore, mentre le righe precedenti mostrano le chiamate delle funzioni che hanno portato alla funzione con l'errore 

# costrutto TRY-EXCEPT: permette di gestire le eccezioni
# la struttura try prova ad eseguire il blocco di istruzioni indentato:
# - se non ci sono errori lo esegue, poi salta alla prima istruzione successiva alla struttura
# - se si presenta un errore, l'istruzione try verifica se il codice di errore corrisponde a quello documentato dopo la clausola except:
# *** se corrisponde, esegue la relativa istruzione indentata, poi salta alla prima istruzione successiva alla struttura try-except, senza bloccare l'esecuzione
# *** se non corrisponde, l'interprete Python va in errore e blocca l'esecuzione del programma
my_var = 'Ciao'

try:
    my_var = float(my_var)
except:
    print('Non posso convertire "my_var" a valore numerico!')
# oppure:
my_var = 'Ciao'

try:
    my_var = float(my_var)
except:
    print('Non posso convertire "my_var" a valore numerico!')
    print('Uso il valore di default "0.0" per "my_var"')
    my_var = 0.0
# gestisco l'errore in modo diverso a seconda dell'eccezione:
try:
    my_var = 'Ciao'
except ValueError:
    print('Non posso convertire "my_var" a valore numerico!')
    print('Ho avuto un errore di VALORE. "my_var" valeva {}' .format(my_var))
except TypeError:
    print('Non posso convertire "my_var" a valore numerico!')
    print('Ho avuto un errore di TIPO. "my_var" era di tipo {}' .format(type(my_var)))
except Exception as e: # Exception intercetta tutti i tipi di eccezione -> è la classe base
    print('Non posso convertire "my_var" a valore numerico!')
    print('Ho avuto un errore GENERICO: "{}".' .format(e))
