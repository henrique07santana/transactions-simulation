import pytest
import sys
sys.path.append('.')
from src.transactions.credit_card import credit_card_generator as ccg

credit_card_generator = ccg.CreditCardGenerator()

def test_generate_15_card_numbers():
    credit_card_list = credit_card_generator.generate(quantity=15)
    assert len(credit_card_list) == 15 

def test_generate_amex_length_13():
    credit_card_list = credit_card_generator.generate('amex', 13)
    assert (
            credit_card_list[0][0] == 'amex'
            and credit_card_list[0][1][0] in ['3','4'] 
            and len(credit_card_list[0][1]) == 13 
    )

def test_generate_encrypted():
    credit_card_number_length = 16
    credit_card_list = credit_card_generator.generate(credit_card_number_length=credit_card_number_length, encrypted=True)
    assert len(credit_card_list[0][1]) > credit_card_number_length
 

if __name__ == '__main__':
    #print(credit_card_generator.generate('mastercard'))
    #print(credit_card_generator.generate('visa', encrypted=True))
    #print(credit_card_generator.brand_names)
    print(credit_card_generator.generate_randomly(quantity=5))