import random

states_dict = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}

weights_dict = {
    'AC': 0.005,
    'AL': 0.015,
    'AP': 0.005,
    'AM': 0.005,
    'BA': 0.05, 
    'CE': 0.03, 
    'DF': 0.05, 
    'ES': 0.025,
    'GO': 0.025,
    'MA': 0.025,
    'MT': 0.01, 
    'MS': 0.01, 
    'MG': 0.06, 
    'PA': 0.01, 
    'PB': 0.05, 
    'PR': 0.07, 
    'PE': 0.05, 
    'PI': 0.005,
    'RJ': 0.12, 
    'RN': 0.05, 
    'RS': 0.07, 
    'RO': 0.005,
    'RR': 0.005,
    'SC': 0.07, 
    'SP': 0.15, 
    'SE': 0.025,
    'TO': 0.005,
}

if __name__ == '__main__':
    a = random.choices(
            population=list(states_dict.values()),
            weights=list(weights_dict.values()),
            k=10
        )
    print(a)