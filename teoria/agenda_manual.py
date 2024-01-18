AGENDA = {
    "luan":{
        "tel":"9999-9999",
        "email": "luan@email.com",
        "enedereco": "av. 1"
    },
    "maria":{
        "tel":"9999-5555",
        "email": "maria@email.com",
        "endereco":"av. 2"
    }
}

AGENDA['luan']['endereco'] = "Av. 3"

AGENDA['Zé'] ={
    "tel": "9999-8888",
    "email": "ze@email.com",
    "enedereco": "av. 1",
}

AGENDA.pop("luan")

for contato in AGENDA:
    print(contato)