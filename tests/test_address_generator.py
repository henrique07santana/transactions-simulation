import pytest
import sys
sys.path.append('.')
from src.transactions.address import address_generator as ag

address_generator = ag.AddressGenerator()

def test_generate_10_addresses():
    address_list = address_generator.generate(10)
    assert len(address_list) == 10 

if __name__ == '__main__':
    print(address_generator.generate(5))