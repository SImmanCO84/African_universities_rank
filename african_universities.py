from list_pull import data_list 
from random import sample

def univ_rank(sublist_size,number_of_universities): 
    #sub-lists of universities  
    univ_list = [data_list[x:x+sublist_size] for x in range(0, len(data_list), sublist_size)] 
    # n random number of universities from all sub-lists 
    random_universities = [sample(sublist,number_of_universities) for sublist in univ_list]
    return  random_universities