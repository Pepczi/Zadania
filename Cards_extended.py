class BaseContact:
    def __init__(self, f_name, l_name, phone, mail):
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
        self.mail = mail
        self._name_length = ''
    def __repr__(self):
        return f'{self.f_name} {self.l_name} {self.mail} {self.phone}'
    def contact(self):
        return f'Wybieram numer: {self.phone} i dzwonię do... {self.f_name} {self.l_name}.'
    @property
    def name_length(self):
        self._name_length = f'{len(self.f_name)} {len(self.l_name)}'
        return self._name_length

class BuisnessContact(BaseContact):
    def __init__(self, position, company,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self._name_length = ''
    def contact(self):
        return f'Wybieram numer: {self.phone} i dzwonię do... {self.f_name} {self.l_name}.'
    @property
    def name_length(self):
        super()._name_length(self)

# Tworzenie losowych wizytówek prywatnych oraz służbowych 
from faker import Faker
fake = Faker()

private_cards = []
buisness_cards = []

def new_private():
    private_cards.append(BaseContact(fake.first_name(), fake.last_name(), fake.phone_number(), fake.ascii_email()))

def new_buisness():
    buisness_cards.append(BuisnessContact(fake.job(), fake.company_suffix(), fake.first_name(), fake.last_name(), fake.phone_number(), fake.ascii_email()))

def show_buisness():
    for v, card in enumerate(buisness_cards):
        print(f"{v} : {card}")

def show_private():
    for v, card in enumerate(private_cards):
        print(f"{v} : {card}")


while True:
    user_input = input("""
    1: Dodaj wizytówkę prywatną,
    2: Dodaj wizytówkę służbową, 
    3: Wyświetl prywatne,
    4: Wyświetl służbowe, 
    5: Aby zadzwonić, 
    0: Zakończ
    """)

    if user_input == '1':
        new_private()
    elif user_input == '2':
        new_buisness()
    elif user_input == '3':
        show_private()
    elif user_input == '4':
        show_buisness()
    elif user_input == '5':
        secound_input = input("1: Prywatnie, 2: Służbowo: ")
        if secound_input == '1':
            show_private()
            third_input = input("Wybierz pozycję z listy: ")
            print(private_cards[int(third_input)].contact())
        else:
            show_buisness()
            third_input = input("Wybierz pozycję z listy: ")
            print(buisness_cards[int(third_input)].contact())
    elif user_input == '0':
        exit(0)
    else:
        print('Zły symbol')