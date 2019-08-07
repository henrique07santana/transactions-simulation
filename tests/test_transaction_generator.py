import pytest
import sys
sys.path.append('.')
from src.transactions import transaction_generator as tg

transaction_generator = tg.TransactionGenerator()

def test_generate_20_transactions():
    transaction_list = transaction_generator.generate(20)
    assert len(transaction_list) == 20 

if __name__ == '__main__':
    print(transaction_generator.generate())