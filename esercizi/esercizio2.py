def sum_list(the_list):
    if the_list is None:
        risultato = 0
    else:
        risultato = sum(the_list)
    return risultato

# my_list = [1,2,456,765,4,23,88]
# my_list = [None]
# risultato = sum_list(my_list)
# print('il risultato è: {}' .format(risultato))