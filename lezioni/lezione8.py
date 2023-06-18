# CREARE UN MODELLO
# modello: ipotesi di comportamento del mondo reale 
# modello fisico: rappresentazione concettuale (spesso una semplificazione che ammette una formalizzazione matematica) del mondo reale o di una sua parte, capace di spiegare un determinato fenomeno
# modello matematico: rappresentazione quantitativa di un fenomeno naturale
# modello statistico: modello matematico che incarna un insieme di ipotesi statistiche riguardanti la generazione dei dati campione -> generica ipotesi di come si crede che si comporti il mondo reale

# modello semplificato:
# vendite dello shampoo al tempo t+1 sono date da:
# - l'incremento medio negli n mensi precdenti 
# - applicato sulle vendite al tempo t

# tipo di modello "a finestra" (di lunghezza n)

# creiamo un oggetto Model come base, avrà 2 metodi principali:
# - metodo "FIT" per fittare il modello su dei dati
# - metodo "PREDICT" per ottenere delle previsioni a partire da altri dati

class Model():

    def fit(self, data):
        # fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
       # predict non implementato nella classe base 
        raise NotImplementedError('Metodo non implementato')