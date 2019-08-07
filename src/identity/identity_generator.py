from .names.name_generator import NameGenerator
from .emails.email_generator import EmailGenerator
from .documents.document_generator import DocumentGenerator
from .ages.age_generator import AgeGenerator

import random
import copy
from typing import List, Tuple, Any

class IdentityGenerator:
    def __init__(self):
        self.domain_list = ['@gmail.com', 
                            '@hotmail.com',
                            '@outlook.com',
                            '@yahoo.com', 
                            '@aol.com', 
                            '@live.com']

        self.document_generator = DocumentGenerator()
        self.name_generator = NameGenerator()
        self.email_generator = EmailGenerator()
        self.age_generator = AgeGenerator()
        self.genders = ['male', 'female']

    def generate(self, quantity: int = 1) -> List[Tuple]:
        # Document Number
        document_list = self.document_generator.generate(quantity)

        # Name and Email
        name_list = []
        gender_list = []
        email_list = []
        
        for i in range(quantity):
            gender = random.choice(self.genders)
            full_name = self.name_generator.generate(gender)
            name_list.append(full_name)
            gender_list.append(gender)
            email_list.append(self.email_generator.generate_with_name(full_name))

        # Age
        birthday_list = self.age_generator.generate(quantity=quantity, birthday=True)
        
        return list(zip(document_list, name_list, gender_list, email_list, birthday_list))