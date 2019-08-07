import sys
sys.path.append('.')
from src.transaction_generator import TransactionGenerator
import json
from azure.servicebus import ServiceBusService

transaction_generator = TransactionGenerator()
sbs = ServiceBusService(service_namespace='your-service-namespace', shared_access_key_name='your-key-name', shared_access_key_value='your-root-manage-shared-access-key')

for i in range(20):
    transaction = transaction_generator.generate()
    print(transaction)
    s = json.dumps(transaction)
    sbs.send_event('firsthub', s)
