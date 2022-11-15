# lezione 2
def sum_list(the_list):
    if(len(the_list) == 0):
        return None
    risultato = 0
    for item in the_list:
        risultato = risultato + item
    return risultato    

my_list = []
l = sum_list(my_list)
print(l)