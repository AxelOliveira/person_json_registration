import json

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def salvar(self):
        return f'{self.name} salvo na lista.'

person1 = Person('Wonwoo', 27)
person2 = Person('Jaemin', 28)
person3 = Person('San', 26)

people = [vars(person1), vars(person2), vars(person3)]

def salvar_contatos(contatos):
    with open('person_registration.json', 'w', encoding='utf-8') as arquivo:
        json.dump(
            contatos,
            arquivo,
            ensure_ascii=False,
            indent=2,
        )

def retorno_contatos():
    with open('person_registration.json', 'r', encoding='utf-8') as arquivo:
        dados_pessoas = json.load(arquivo)
        return [Person(**dados) for dados in dados_pessoas]

person_objects = retorno_contatos()

for person in person_objects:
    print(vars(person))
    print(person.salvar())