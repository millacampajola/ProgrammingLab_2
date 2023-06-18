def sum_csv(file_name):
    my_file = open(file_name, 'r')
    values = []
    for line in my_file:
        elements = line.split(',')

        if elements[0] != 'Date':
            valore = elements[1]
            values.append(float(valore))

    risultato = sum(values)
    my_file.close()
    return risultato

somma_valori = sum_csv('shampoo_sales.csv')
print('la somma dei valori è: {}' .format(somma_valori))