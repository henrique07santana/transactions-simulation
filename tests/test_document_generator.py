import pytest
import sys
sys.path.append('.')
from src.transactions.identity.documents import document_generator as dg

document_generator = dg.DocumentGenerator()

def test_cpf_length():
    cpf_list = document_generator.generate(quantity=1, document_type='CPF ')
    cpf = cpf_list[0]
    assert len(cpf) == 11

def test_generate_10_documents():
    document_list = document_generator.generate(10)
    assert len(document_list) == 10

if __name__ == '__main__':
    print(document_generator.generate(5))
    print(document_generator.document_type_list)