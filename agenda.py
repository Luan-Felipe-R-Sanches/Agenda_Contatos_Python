AGENDA = {}

AGENDA['luan'] = {
    'telefone': '99999-8888',
    'email': 'luan@email.com',
    'endereco': 'Av 1'
}
AGENDA['maria'] = {
    'telefone': '98765-4321',
    'email': 'maria@email.com',
    'endereco': 'Rua 2'
}
AGENDA['joao'] = {
    'telefone': '77777-9999',
    'email': 'joao@email.com',
    'endereco': 'Travessa 3'
}

def mostrar_contatos():
    for contato in AGENDA:
        print('Nome:', contato)
        print('Telefone:',AGENDA[contato]['telefone'])
        print('Email:',AGENDA[contato]['email'])
        print('Endereço:',AGENDA[contato]['endereco'])
        print("########################")
mostrar_contatos()