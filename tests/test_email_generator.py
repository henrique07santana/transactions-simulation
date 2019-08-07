import pytest
import sys
sys.path.append('.')
from src.transactions.identity.emails import email_generator as eg

email_generator = eg.EmailGenerator()

def test_generate_sanitized_email():
    name = 'Íris Conceição'
    email = email_generator.generate_with_name(name)
    email_identification = email.split('@')[0]
    assert email[:len(email_identification)] == 'iris.conceicao' 

def test_generate_random_email_completion():
    name = 'Fábio'
    email = email_generator.generate_with_name(name)
    email_identification = email.split('@')[0]
    assert len(email_identification) > len(name) 

if __name__ == '__main__':
    print(email_generator.generate_with_name('Henríque Çantana'))
    print(email_generator.generate_with_name('Henríque'))
    print(email_generator.generate_randomly())