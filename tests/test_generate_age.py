import pytest
import sys
sys.path.append('.')
from src.transactions.identity.ages import age_generator as ag

age_generator = ag.AgeGenerator()

def test_generate_15_ages():
    age_list = age_generator.generate(15)
    assert len(age_list) == 15 

if __name__ == '__main__':
    print(age_generator.generate(quantity=5, birthday=False))
    print(age_generator.generate(quantity=5, birthday=True))