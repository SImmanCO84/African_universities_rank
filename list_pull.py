
import pandas as pd

def data_list():
    data = pd.read_csv("C:/Users/IMMAN.S.C.OGAL/Downloads/african-university-rankings/ScimagoIR 2023 - Overall Rank - Universities - Africa.csv")
    data = data.set_index('Rank')
    data = data.drop(['Sector','Best Country Quartile'],axis=1)
    # create a list from the dataframe
    univ_data = data.values.tolist()

    return univ_data

    
    
