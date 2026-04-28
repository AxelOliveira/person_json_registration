import json

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f'Nome: {self.name} | Idade: {self.age}.'
    
FILE_NAME = 'person_registration.json'

def is_duplicate(name, age, contacts):
    for contact in contacts:
        if contact['name'] == name and contact['age'] == age:
            return True
    return False

def save_contacts(new_contacts):
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            existing = json.load(file)
    except FileNotFoundError:
        existing = []  

    existing.extend(new_contacts)  

    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(
            existing,
            file,
            ensure_ascii=False,
            indent=2,
        )

def load_contacts():
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [Person(**person) for person in data]
    except FileNotFoundError:
        return []
    
def list_contacts(contacts):
    if not contacts:
        print('Nenhum contato cadastrado.')
        return
    
    print('\nContatos:')
    for contact in contacts:
        print(f'\t{contact.display()}')

while True:
    print('\nComandos: adicionar contato, listar contatos ou sair.')
    user_command = input('Digite um comando: ').lower()

    if user_command == 'adicionar contato':
        name = input('Digite o nome do contato: ')
        age = int(input('Digite a idade do contato: '))

        contacts = load_contacts()

        if is_duplicate(name, age, [vars(c) for c in contacts]):
            print('Contato já existe!')

        else:
            person = Person(name, age)
            save_contacts([vars(person)])
            print('Contato salvo com sucesso!')
            
    elif user_command == 'listar contatos':
        contacts = load_contacts()
        list_contacts(contacts)

    elif user_command == 'sair':
        print('Saindo do sistema...')
        break

    else:
        print('Comando inválido.')