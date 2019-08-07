from typing import List
import random
from datetime import datetime

class AgeGenerator:
    def __init__(self):
        pass
    
    def generate(self, 
                 quantity: int = 1, 
                 birthday: bool = True, 
                 youngest_age: int = 18, 
                 oldest_age: int = 50
                 ) -> List['str']:

        current_year = datetime.now().year
        age_list = [random.choice(range(youngest_age, oldest_age, 1)) for i in range(quantity)]

        if birthday:
            birthday_list = [self._calculate_birthday(current_year - age) for age in age_list]
            return birthday_list
        
        return age_list
    
    def _calculate_birthday(self, year: int) -> str:
        days_in_a_year = 365
        birthday = datetime.strptime('{} {}'.format(random.randint(1, days_in_a_year), year), '%j %Y').strftime("%d/%m/%Y")
        return birthday