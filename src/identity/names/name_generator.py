from .female_names import names_list as female_names_list
from .male_names import names_list as male_names_list
from .surnames import surnames_list
import random

class NameGenerator:

    def __init__(self):
        self.names_dict = {
            'male': male_names_list,
            'female': female_names_list,
        }

        self.surnames_list = surnames_list

    def generate(self, gender: str, full_name: bool = True) -> str:
        name = random.choice(list(self.names_dict[gender]))

        if full_name:
            surname = random.choice(self.surnames_list)
            name = name + ' ' + surname

        return name