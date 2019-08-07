import random
import string
from unicodedata import normalize as norm

class EmailGenerator:
    def __init__(self):
        self.domain_list = ['@gmail.com', 
                            '@hotmail.com',
                            '@outlook.com',
                            '@yahoo.com', 
                            '@aol.com', 
                            '@live.com']

        self.random_numbers_list = range(6,15,1)
    
    def generate_randomly(self) -> str:
        random_characters = random.choice(self.random_numbers_list)       
        email_identification = self._generate_random_identification(random_characters=random_characters)
        random_email = self._add_domain(email_identification)
        return random_email

    def generate_with_name(self, name:str) -> str:
        norm_name = self._normalize(name)
        if len(name.split()) > 1:
            email_identification = norm_name.replace(' ','.')
        else:
            random_bits = random.choice(self.random_numbers_list)  
            email_identification = self._random_complete(norm_name, random_bits)

        email = self._add_domain(email_identification) 
        return email
    
    def _generate_random_identification(self, random_characters: int):
        random_identification = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(random_characters))
        return random_identification

    def _random_complete(self, identification: str, random_bits: int):
        random_identification = identification + str(random.getrandbits(random_bits))
        return random_identification

    def _add_domain(self, identification):
       return identification + random.choice(self.domain_list)
   
    def _normalize(self, name):
        lower_name = name.lower()
        norm_name = norm('NFKD', lower_name).encode('ASCII', 'ignore').decode('ASCII')
        return norm_name