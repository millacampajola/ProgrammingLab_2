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

class FitIncrementModel(IncrementModel):

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

        return prediction
    
    def fit(self, data1, data2):    
        p_1 = self.predict(data1)
        p_2 = self.predict(data2)
        prediction = (p_1 + p_2)/2
        prediction = prediction + data2[-1]
        
        return prediction

data = [8,19,31,41,50,52,60]
lista_1 = [8,19,31,41]
lista_2 = [50,52,60]
previsione = FitIncrementModel()
previsione_fit = previsione.fit(lista_1, lista_2)
print(previsione_fit)