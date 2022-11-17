def sum_csv(file_name): 
    values = []
    my_file = open(file_name ,'r')
    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
            date = elements[0]
            value = elements[1]
            values.append(float(value))
            
        somma = sum(values)
    return somma
    
