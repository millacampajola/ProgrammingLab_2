from datetime import datetime

class ExamException(Exception):
    pass


# classe CSVFile per leggere e memorizzare i dati da un generico file CSV
class CSVFile:

    def __init__(self, name):
        # setto il nome del file
        self.name = name

    def get_data(self):
        # inizializzo una lista vuota denominata 'lines' per salvare tutti i dati
        lines = []
        try:
            # provo ad aprire il file
            with open(self.name,'r') as my_file:
                # con il ciclo 'for' leggo il file linea per linea
                for line in my_file:
                    # utilizzo la funzione strip() per rimuovere spazi e caratteri di 
                    # newline; faccio lo split di ogni linea sulla virgola
                    line = line.strip().split(',')
                    lines.append(line)
        
        except Exception as e:
            raise ExamException('Errore nella lettura del file: "{}"'.format(e))

        # ottengo il numero di colonne dando per corretta la prima riga (intestazione)
        columns = len(lines[0]) 
        new_lines = []
        # ciclo sulla lista "line" e nella nuova lista conservo solo il numero di colonne 
        # corretto per ogni riga (se ci sono caratteri in più li "taglio")
        for line in lines:
            new_lines.append(line[:columns])
        
        return new_lines


# Classe CSVTimeSeriesFile per leggere e memorizzare serie storiche di dati da un file CSV
class CSVTimeSeriesFile(CSVFile):

    def __init__(self, name):
        super().__init__(name)

    # converto le date (da stringhe a datetime) e il numero di passeggeri (da stringhe ad 
    # interi), rimuovo le righe che hanno problemi
    def _cast_data(self, data):
        # separo l'intestazione dai dati
        header = data[0]
        data = data[1:]
        
        # controllo il formato dei dati e lo coverto, se possibile
        converted_data = []
        for line in data:
            converted_line = self._check_line(line)
            converted_data.append(converted_line)
        # creo una nuova lista dove appendo solo le righe che rispettano la condizione (se 
        # la lista non è vuota)
        new_data = []
        for line in converted_data:
            if line:
                new_data.append(line)
        # rimetto l'intestazione ai dati
        new_data = [header] + new_data
        data = new_data
        
        return data

    # controllo e coverto i valori riga per riga
    def _check_line(self,line):
        new_line = line
        # provo a convertire gli elementi di line
        try:
            # trasformo il primo elemento in un oggetto datetime
            date = datetime.strptime(line[0], '%Y-%m')
            # assegno a value il valore del secondo elemento trasformato in intero 
            value = int(line[1])
            # se value è negativo alzo un errore
            if value < 0:
                raise ValueError
            # se la differenza tra il valore convertito in float e 'value' (parte intera) è 
            # diverso da zero significa che il numero dei passeggeri non è intero
            if float(line[1]) - value != 0:
                raise ValueError
            # assegno a new_line una lista con gli elementi date e value convertiti
            new_line = [date, value]
        # catturo le eccezioni: in questo caso ignoro la riga perché non soddisfa le 
        # condizioni e assegno a 'new_line' una lista vuota
        except ValueError:
            new_line = []
        
        return new_line

    # eseguo i controlli sulle date
    def _check_dates(self, dates):
        # controllo che non ci siano date duplicate usando la funzione set(): se la 
        # lunghezza della lista convertita in insieme è diversa dalla lista significa che 
        # ci sono duplicati, in questo caso alzo un'eccezione 
        if len(set(dates)) != len(dates):
            raise ExamException('Errore: ci sono date duplicate')
        # controllo se le date sono ordinate, altrimenti alzo un'eccezione
        for i in range(len(dates)-1):
            if dates[i] > dates[i+1]:
                raise ExamException('Errore: le date non sono ordinate')
        
        return dates

    def get_data(self):
        # chiamo il metodo get_data del genitore 
        data = super().get_data()

        # trasformo i valori nella lista 'data' con il metodo cast_data
        data = self._cast_data(data)

        # creo una lista 'dates' dove salvo solo la prima colonna, senza l'intestazione
        dates = []
        for line in data[1:]: # salto l'intestazione
            dates.append(line[0])
        # controllo la consistenza delle date con il metodo 'check_dates'
        dates = self._check_dates(dates)

        # ritorno la lista 'data' "pulita"
        return data


# metodo esterno per calcolare, per un dato intervallo di anni, la variazione media del 
# numero di passeggeri per ogni mese  
def compute_avg_monthly_difference(time_series, first_year, last_year):
    # provo a convertire 'first_year' e 'last_year' in interi, altrimenti alzo un'eccezzione
    try:
        first_year = int(first_year)
        last_year =  int(last_year)
    except ValueError:
        raise ExamException('Errore: anno in formato non valido')
    # gli anni devono essere positivi, altrimenti alzo un'eccezione
    if first_year < 0 or last_year < 0:
        raise ExamException('Errore: anno in formato non valido')
    # 'first_year' deve essere inferiore a 'last_year', altrimenti alzo un'eccezione 
    if first_year > last_year:
        raise ExamException('Errore: anni in ordine non valido')
    # controllo se il range di anni in input è presente in time_series, altrimenti alzo 
    # un'eccezione
    if not time_series[1][0].year <= first_year <= last_year <= time_series[-1][0].year:
        raise ExamException('Errore: anni non presenti nella serie storica')

    # converto la lista di liste in un dizionario dove la chiave corrisponde alla data e il 
    # valore al numero di passeggeri
    dict_time_series = {}
    for line in time_series[1:]: # salto l'intestazione
        date = line[0]
        value = line[1]
        dict_time_series[date] = value

    # ottengo il sottoinsieme del dizionario per il range di anni che mi inetressa
    time_series_subset = {}
    for key in dict_time_series:
        if first_year <= key.year <= last_year:
            time_series_subset[key] = dict_time_series[key]

    # creo un dizionario di 12 elementi, dove la chiave è il mese e il valore è una lista 
    # contenente il numero di passeggeri di ogni anno (del range) per quel mese
    months = {}
    for i in range(1,13):
        months[i] = []
    # ciclo sulle chiavi del dizionario 'time_series_subset' e estraggo il mese dalla chiave 
    # utilizzando key.month assegnando il risultato a month, accedo alla lista 
    # corrispondente al mese all'interno del dizionario 'months' e appendo 'value' (valore 
    # associato a key nel dizionario time_series_subset) alla lista del mese corrispondente 
    # in 'months'
    for key in time_series_subset:
        month = key.month
        value = time_series_subset[key]
        months[month].append(value)
    
    # CALCOLO LA DIFFERENZA MEDIA PER OGNI MESE
    def media(months):
        # come da consegna, se la lista dei valori per ogni mese è vuota oppure ho un solo 
        # valore ritorno 0
        if len(months) <= 1:
            return 0
        # altrimenti cacolo la media: faccio la differenza tra l'ultimo e il primo valore 
        # per ogni mese e poi divido la differenza per la lunghezza della lista 'months' -1
        else:
            return (months[-1] - months[0] )/(len(months)-1)

    # creo una lista vuota per salvare le medie dei valori per ogni mese
    months_avg = []
    # ciclo sui valori del dizionario 'months' e usando il metodo 'media' calcolo la 
    # differenza media per ogni mese e poi la appendo alla lista 'avg'
    for value in months.values():
        months_avg.append(media(value))

    # finalmente ritorno la lista
    return months_avg