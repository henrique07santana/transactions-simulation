from typing import List, Tuple
import random
import copy
from . import hash_algorithm as ha
from datetime import datetime

class CreditCardGenerator:

    def __init__(self):
        
        self.visa_prefix_list = [
                ['4', '5', '3', '9'],
                ['4', '5', '5', '6'],
                ['4', '9', '1', '6'],
                ['4', '5', '3', '2'],
                ['4', '9', '2', '9'],
                ['4', '0', '2', '4', '0', '0', '7', '1'],
                ['4', '4', '8', '6'],
                ['4', '7', '1', '6'],
                ['4']]

        self.mastercard_prefix_list = [
                ['5', '1'], ['5', '2'], ['5', '3'], ['5', '4'], ['5', '5']]

        self.amex_prefix_list = [['3', '4'], ['3', '7']]

        self.discover_prefix_list = [['6', '0', '1', '1']]

        self.diners_prefix_list = [
                ['3', '0', '0'],
                ['3', '0', '1'],
                ['3', '0', '2'],
                ['3', '0', '3'],
                ['3', '6'],
                ['3', '8']]

        self.en_route_prefix_list = [['2', '0', '1', '4'], ['2', '1', '4', '9']]

        self.jcb_prefix_list = [['3', '5']]

        self.voyager_prefix_list = [['8', '6', '9', '9']]

        self.brands = {
            'visa': self.visa_prefix_list,
            'mastercard': self.mastercard_prefix_list,
            'amex': self.amex_prefix_list,
            'discover': self.discover_prefix_list,
            'diners': self.diners_prefix_list,
            'jcb': self.jcb_prefix_list,
            'voyager': self.voyager_prefix_list,
            }

        self.brands_weights = {
            'visa': 0.4,
            'mastercard': 0.4,
            'amex':0.1,
            'discover': 0.025,
            'diners': 0.025,
            'jcb': 0.025,
            'voyager': 0.025,
            } 

    @property
    def brand_names(self):
        return list(self.brands.keys())
    
    def generate_randomly(self, 
                          quantity: int = 1, 
                          encrypted: bool = False
                        ) -> List[Tuple]:
        brand_names = random.choices(population=self.brand_names, 
                                    weights=self.brands_weights.values(), 
                                    k=quantity
                                    )
        
        credit_card_list = [self.generate(brand_name=brand,
                                         credit_card_number_length=random.choice([14,15,16]),
                                         quantity=1,
                                         encrypted=encrypted
                                         )[0]
                            for brand in brand_names
                            ]
        
        return credit_card_list
    
    def generate(self,
                 brand_name: str = 'mastercard', 
                 credit_card_number_length: int = 16,
                 quantity: int = 1,
                 encrypted: bool = False
                ) -> List[Tuple]:
        
        credit_card = self._credit_card_number(self.brands[brand_name], credit_card_number_length, quantity)
        expiration_list = self._generate_expiration(quantity)

        if encrypted:
            credit_card_hash = [ha.encrypt(card) for card in credit_card]
            return [(brand_name, card_number, expiration) for card_number, expiration in zip(credit_card_hash, expiration_list)]
        else:
            return [(brand_name, card_number, expiration) for card_number, expiration in zip(credit_card, expiration_list)] 
    
    def _generate_expiration(self, quantity: int = 1) -> List[str]:
        now = datetime.now()
        current_month = now.month
        next_month = current_month + 1
        annualy_months = 12
        current_year = now.year
        max_years_ahead = 6
        expiration_year_list = [random.randint(current_year, current_year+max_years_ahead) for i in range(quantity)]
        expiration_month_list = [random.choice(range(1, annualy_months+1))
                                if year != current_year 
                                else random.choice(range(next_month, annualy_months+1))
                                for year in expiration_year_list]
        #expiration_list = list(zip(expiration_month_list, expiration_year_list))
        expiration_list = [str(month) + '/' + str(year) for month,year in zip(expiration_month_list, expiration_year_list)]
        return expiration_list

    def _credit_card_number(self,  
                            prefix_list: List[List[str]], 
                            credit_card_number_length: int, 
                            quantity: int) -> List[str]:
        result: List[str] = []
        while len(result) < quantity:
            prefix = copy.copy(random.choice(prefix_list))
            result.append(self._complete_number(prefix, credit_card_number_length))
        
        return result

    def _complete_number(self, 
                          prefix: List[str], 
                          credit_card_number_length: int
                          ) -> str:

        credit_card_number = []
        credit_card_number.extend(prefix)

        # generate digits
        while len(credit_card_number) < (credit_card_number_length):
            digit = str(random.choice(range(0, 10)))
            credit_card_number.append(digit)

        return ''.join(credit_card_number)