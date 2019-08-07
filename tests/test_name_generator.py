import pytest
import sys
sys.path.append('.')
from src.transactions.identity.names import name_generator as ng, male_names
name_generator = ng.NameGenerator()
male_names_list = male_names.names_list

def test_generate_male_name():
    name = name_generator.generate(gender='male', full_name=False)
    assert name in male_names_list

def test_generate_full_name():
    name = name_generator.generate(gender='female', full_name=True)
    assert len(name.split(' ')) > 1

if __name__ == '__main__':
    print(name_generator.generate('female').split(' '))