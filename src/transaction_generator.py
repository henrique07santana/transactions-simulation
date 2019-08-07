from .identity.identity_generator import IdentityGenerator
from .credit_card.credit_card_generator import CreditCardGenerator
from .address.address_generator import AddressGenerator

from typing import List, Dict
import uuid
import random
from datetime import datetime

class TransactionGenerator:
    def __init__(self):
        self.credit_card_generator = CreditCardGenerator()
        self.identity_generator = IdentityGenerator()
        self.address_generator = AddressGenerator()
    
    def generate(self, quantity: int = 1) -> List[Dict]:
        transaction_list = []
        id_list = self._generate_id(quantity=quantity)
        identity_list = self.identity_generator.generate(quantity=quantity)
        credit_card_list = self.credit_card_generator.generate_randomly(quantity=quantity)
        address_list = self.address_generator.generate(quantity=quantity)
        
        amount_list = self._generate_amount(quantity=quantity)
        installments_list = [self._generate_installments(amount) for amount in amount_list]

        for i in range(quantity):
            transaction_id = id_list[i]
            document, name, gender, email, birthday = identity_list[i]
            brand, credit_card, expiration = credit_card_list[i]
            cep, city, state = address_list[i]
            amount = amount_list[i]
            installments = installments_list[i]
            now = self._generate_date()
            transaction = {
                            "Transaction": {
                                "Id": transaction_id,
                                "Order": "123456789AB",
                                "Date": str(now),
                                "Amount": amount
                            },
                            "Card": {
                                "Holder": name.upper(),
                                "Number": credit_card,
                                "Expiration": expiration,
                                "Brand": brand
                            },
                            "Customer": {
                                "Name": name,
                                "Identity": document,
                                "BirthDate": birthday,
                                "Email": email,
                                "Billing": {
                                    "City": city,
                                    "State": state,
                                    "ZipCode": cep,
                                    "Country": "BR"
                                },
                                "Shipping": {
                                    "City": city,
                                    "State": state,
                                    "ZipCode": cep,
                                    "Country": "BR"
                                }
                        }
                    }

            transaction_list.append(transaction)

        return transaction_list
    
    def _generate_id(self, quantity: int) -> List[str]:
        id_list = [str(uuid.uuid4()) for i in range(quantity)]
        return id_list

    def _generate_date(self) -> datetime:
        return datetime.utcnow()

    def _generate_installments(self, amount: int) -> int:
        max_cost_cheap_purchase = 100
        min_cost_expensive_purchase = 800
        installments = 1
        if amount > max_cost_cheap_purchase and amount < min_cost_expensive_purchase:
            installments = random.randint(1,4)
        if amount > min_cost_expensive_purchase:
            installments = random.randint(1,14)
        return installments
    
    def _generate_amount(self, quantity:int = 1) -> List:
        cheapest_product_amount = 1000
        most_expensive_product_amount = 250000
        amount_list = [random.randint(cheapest_product_amount, most_expensive_product_amount) for i in range(quantity)]
        return amount_list

if __name__ == '__main__':
    trx_generator = TransactionGenerator()
    print(trx_generator.generate())