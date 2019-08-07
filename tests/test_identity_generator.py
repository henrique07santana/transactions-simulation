import pytest
import sys
sys.path.append('.')
from src.transactions.identity import identity_generator as ig

identity_generator = ig.IdentityGenerator()

def test_generate_10_identities():
    identity_list = identity_generator.generate(quantity=10)
    assert len(identity_list) == 10

if __name__ == '__main__':
    print(identity_generator.generate(25))