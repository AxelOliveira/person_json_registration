import json

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f'Nome: {self.name} | Idade: {self.age} anos.'
    
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age
        }
    
FILE_NAME = 'person_registration.json'

def is_duplicate(name, age, contacts):
    for contact in contacts:
        if contact['name'].lower() == name.lower() and contact['age'] == age:
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

def search_contact(contacts):
    search_name = input('Digite o nome do contato que deseja procurar: ').lower().strip()
    found = False

    for contact in contacts:
        if search_name == contact.name.lower():
            found = True
            print(contact.display())

    if not found:
            print('Contato não encontrado')

def normalize_name(name):
    return name.strip().title()

while True:
    print('\n===== SISTEMA DE CONTATOS =====')
    print('1 - Adicionar contato')
    print('2 - Listar contatos')
    print('3 - Buscar contatos')
    print('4 - Sair')

    user_command = input('Digite um comando: ')

    if user_command == '1':
        name = normalize_name(input('Digite o nome do contato: '))
        try: 
            age = int(input('Digite a idade do contato: '))
            if age < 0:
                print('Idade inválida.')
                continue

        except ValueError:
            print('Digite somente números!')
            continue

        contacts = load_contacts()

        if is_duplicate(name, age, [c.to_dict() for c in contacts]):
            print('Contato já existe!')

        else:
            person = Person(name, age)
            save_contacts([person.to_dict()])
            print('Contato salvo com sucesso!')
            
    elif user_command == '2':
        contacts = load_contacts()
        list_contacts(contacts)

    elif user_command == '3':
        contacts = load_contacts()
        search_contact(contacts)

    elif user_command == '4':
        print('Saindo do sistema...')
        break

    else:
        print('Comando inválido.')