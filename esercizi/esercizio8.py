# idea di iterare sui valori e misurare differenza tra t e t-1 ogni volta, sommare le differenze e arrivati alla fine dividere la somma ottenuta per il numero di valori -1 e sommarci l'ultimo valore visto 
class Model():

    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data): 
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):

    def predict(self, data):

        for item in data:
            if item < 0:
                raise Exception('Non è possibile avere un numero < 0')

        prediction = 0
        prev_value = data[0]

        for i in range(len(data)):
            prediction = (data[i] - prev_value) + prediction
            prev_value = data[i]

        prediction = prediction / (len(data) - 1)
        prediction = prediction + data[-1] # data[-1]: ultimo valore di data

        return prediction

lista = [50, 54, 80]
previsione = IncrementModel()
print(previsione.predict(lista))

# if not previsione == 95.0:
#     raise Exception('Test non passato')