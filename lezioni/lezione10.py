# come valutare un modello
# per valutare un modello lo si semplicemente applica su un dataset noto e si “vede come va”. Per ottenere questo dataset in genere si estrae una parte del dataset originale, di solito il 20-30 %
# esempio: se ho 36 mesi di dati di vendite di shampoo, ne userò solo i primi 24 per il fit, mentre ne estrarrò gli ultimi 12 per valutare il modello: (*) fit (training) dataset; (*) evaluation (test) dataset
# per "vedere come va" il modello sul test set vado a confrontare le sue predizioni con i dati veri

# il confronto fra le predizioni del modello ed i dati veri sul dataset di test lo si fa calcolando la differenza fra la predizione stessa ed il dato, ovvero calcolando l'errore
# infine si fa la media degli errori per avere un'idea di come va genericamente il modello su tutto il dataset di test