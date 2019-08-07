import random
from typing import List, Any

class DocumentGenerator:
    def __init__(self):
        self._document_type_list = ['CPF']
    
    @property
    def document_type_list(self):
        return self._document_type_list

    def generate(self, quantity: int = 1, document_type: str = 'CPF') -> List[str]:
        # TODO: Accept other document types
        #if document_type == 'CPF':
        document = [self._generate_cpf() for i in range(quantity)]
        return document
    
    def _generate_cpf(self) -> str:
        cpf_length_without_digits = 9                                                                      
        numbers_list = [random.randrange(10) for i in range(cpf_length_without_digits)]
        numbers_list.append(self._calculate_cpf_digit(numbers_list))
        numbers_list.append(self._calculate_cpf_digit(numbers_list))
        document = ''.join([str(n) for n in numbers_list])
        return document

    def _calculate_cpf_digit(self, numbers_list: List[int]) -> int:
        cpf_length = 11
        total_sum = 0
        number_list_length = len(numbers_list)
        for i in range(len(numbers_list)):
            total_sum += numbers_list[i] * (1 + number_list_length - i)
        result = cpf_length - total_sum % cpf_length
        if result >= cpf_length - 1: 
            return 0
        return result