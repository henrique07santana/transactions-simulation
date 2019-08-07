import sys
sys.path.append('.')
from .brazilian_states import states_dict, weights_dict
from .brazilian_cities import cities_dict
from typing import List
import random
import pandas as pd
import os 

class AddressGenerator:
    def __init__(self):
        path = os.getcwd()
        self.states_dict = states_dict
        self.weights_dict = weights_dict
        self.cities_data_frame = pd.read_csv(path + '/src/transactions/address/brazilian_zip_codes.csv', sep=',')

    def generate(self, quantity: int = 1) -> List[str]:
        uf_list = random.choices(
                                    population=list(states_dict.keys()),
                                    weights=list(weights_dict.values()),
                                    k=quantity
                                )
        
        cep_list = []
        city_list = []
        #address_list = [random.choice(self.data_frame_get_cities_from_uf(uf)) + ', ' + self.states_dict[uf] for uf in uf_list]
        for uf in uf_list:
            uf_data_frame = self.data_frame_get_info_from_uf(uf)
            random_index = random.choice(uf_data_frame.index)
            random_row = uf_data_frame.loc[random_index]
            cep_list.append(random.randint(random_row['FIRST_CEP'], random_row['LAST_CEP']))
            city_list.append(random_row['CITY'])

        address_list = list(zip(cep_list,city_list,uf_list))

        return address_list
    
    def data_frame_get_info_from_uf(self, uf:str) -> List['str']:
        uf_info_data_frame = self.cities_data_frame[self.cities_data_frame['UF'] == uf]
        return uf_info_data_frame
    
