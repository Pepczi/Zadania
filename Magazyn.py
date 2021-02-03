"""
POKAŻ MI SWOJE TOWARY --- Czyli prosty symulator handlu w typowej grze RPG.
Tym razem to my jesteśmy NPC-tem, więc na zysk niestety nie możemy liczyć ;)
Funkcje:
- Wyświetlanie stanu sklepu 
- Historia transakcji 
- Kupowanie przedmiotów 
- Sprzedawanie przedmiotów 
"""

shop_stock = [
    {'name': 'Health Potion', 'quantity': '20', 'unit': 'bottle', 'unit_price': '50'},
    {'name': 'Mana Potion', 'quantity': '55', 'unit': 'bottle', 'unit_price': '35'},
    {'name': 'Corrupted Powder', 'quantity': '500', 'unit': 'gram', 'unit_price': '5'},
    {'name': 'Boots of Speed', 'quantity': '3', 'unit': 'item', 'unit_price': '1000'},
    {'name': 'Herbs', 'quantity': '999', 'unit': 'gram', 'unit_price': '420'}
    ]
shop_history = []

def items_list(stock):
    """Zwraca listę list w której elementy to wartości kluczy z listy słowników."""
    temp_value = []
    for i in range(len(stock)):
        temp_value.append(list(stock[i].values()))
    return temp_value


def table_size(stock):
    """Zwraca liste 4 elementów, w którym każdy z elementów odpowiada za najdłuższy ciąg tekstowy w danej kolumnie."""
    colWidth = [0] * len(stock[0])
    list_of_items = items_list(stock)
    for i in range(len(list_of_items[0])):
        for j in range(len(list_of_items)):
            if len(list_of_items[j][i]) > colWidth[i]:
                colWidth[i] = len(list_of_items[j][i])
    return colWidth


def table_print(stock):
    """Print tabeli z przedmiotami, problem przy dostosowywaniu odległości."""
    table_adjust = table_size(stock)
    sum_of_elements = sum(table_adjust)
    if stock == shop_stock:
        print('Oto lista moich towarów'.center(sum_of_elements + 23, '-'))
    if stock == shop_history:
        print('Lista sprzedanych towarów'.center(sum_of_elements + 23, '-'))
    print('Name'.ljust(table_adjust[0] + 4, ' ') + 'Quantity'.rjust(table_adjust[1] + 8, ' '), end = '')
    print('Unit'.rjust(table_adjust[2] + 4, ' ') + 'Unit Price'.rjust(table_adjust[3] + 10, ' '))
    list_of_items = items_list(stock)
    for i in range(len(list_of_items)):
        for j in range(len(list_of_items[0])):
            print(list_of_items[i][j].ljust(table_adjust[j] + 8, ' '), end = '')
        print(end = '\n')


def greetings():
    """Wydrukowanie powitania."""
    print('''I wtedy ona mi mówi...
O! Nie zauważyłem Cię. Mam nadzieję, że nie usłyszałeś za dużo...
Witaj w moim małym sklepiku, chętnie ubiję z Tobą ofertę.
Aby... Wpisz:
    - Pokazać Ci moje towary: show
    - Sprzedać przedmioty: sell
    - Kupić przedmioty: buy
    - Zobaczyć historię transakcji: history
    - Sprawdzić moje dochody: revenue
            ''')


def selling(stock):
    """Sprzedaż przedmiotów ze sklepu."""
    client_input = input('Który z moich towarów Cię interesuje?').title()
    list_of_items = items_list(stock)
    item_detail = []
    for i in range(len(list_of_items)):
        for names in list_of_items[i]:
            if names == client_input:
                index_in_stock = i
                item_detail = list_of_items[i]
    quant_input = input(f'Posiadam {item_detail[1]} {item_detail[2]} {item_detail[0]}, jaka ilośc Cię interesuje?')
    client_confirmation = input(f'Chcesz kupić {quant_input} {client_input} za {int(quant_input) * int(item_detail[3])}?').lower()
    if client_confirmation == 'tak':
        print('Świetnie! Miło mieć takich klientów')
        shop_history.append({'name':client_input, 'quantity': quant_input, 'unit': item_detail[2], 'unit_price': item_detail[3]})
        shop_stock[index_in_stock] = ({'name':client_input, 'quantity': str(int(item_detail[1]) - int(quant_input)), 'unit': item_detail[2], 'unit_price': item_detail[3]})
    else:
        print('Przemyśl to jeszcze, poczekam')


def buying():
    """Kupowanie przedmiotów przez sklep."""
    print('Zawsze kupię coś od zacnych poszukiwaczy, muszę tylko poznać szczegóły tego przedmiotu...')
    name_input = input('Nazwa przedmiotu: ')
    quantity_input = input('Ilość jaką chcesz sprzedać: ')
    unit_input = input('Jednostka: gramy, butelki, szczypta czy po prostu sztuka: ')
    unit_price_input = input('Ile sobie życzysz za jedną jednostkę tego przedmiotu: ')
    new_item = {'name': name_input.title(), 'quantity': quantity_input, 'unit': unit_input, 'unit_price': unit_price_input}
    shop_stock.append(new_item)
    print('Handel z Tobą to czysta przyjemność')

def revenue():
    """Obliczanie salda."""
    items_bought = items_list(shop_stock)
    bought = 0
    for i in range(len(items_bought)):
        bought += (int(items_bought[i][1]) * int(items_bought[i][3]))
    items_sold = items_list(shop_history)
    sold = 0
    for i in range(len(items_sold)):
        sold += (int(items_sold[i][1]) * int(items_sold[i][3]))
    print(f'Na towar wydałem {bought}, a sprzedałem za {sold}')
    print(f'Łączne saldo to {sold - bought}')

#TO DO: EKSPORT I IMPORT DO PLIKÓW CSV
def export_items_to_csv():
    raise NotImplementedError
    
def export_sales_to_csv():    
    raise NotImplementedError

def load_items_from_csv():    
    raise NotImplementedError



def interface():
    """Główna pętla programu."""
    greetings()
    client_input = ''
    while client_input != 'exit':
        client_input = input('Co zatem chcesz zrobić? ').lower().strip()
        if client_input == 'show':
            table_print(shop_stock)
        if client_input == 'sell':
            buying()
        if client_input == 'buy':
            selling(shop_stock)
        if client_input == 'history':
            table_print(shop_history)
        if client_input == 'revenue':
            print('Nie powinno Cie to interesować, ale co mi tam..')
            revenue()  
    print('Do zobaczenia!')

if __name__ == "__main__":
    interface()

