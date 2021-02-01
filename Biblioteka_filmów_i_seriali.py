class Movie:
    def __init__(self, title, genre, year, views):
        self.title = title
        self.genre = genre
        self.year = year
        self.views = int(views)
    def __repr__(self):
        return f'{self.title} ({self.year}) zobaczono {self.views} razy.'
    def play(self, view = 1):
        self.views += view

class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode
    def __repr__(self):
        if self.season < 10 and self.episode < 10:
            return f"{self.title} S0{self.season}E0{self.episode} zobaczono {self.views} razy."
        elif self.season < 10 and self.episode >= 10:
            return f"{self.title} S0{self.season}E{self.episode} zobaczono {self.views} razy."
        elif self.season >= 10 and self.episode < 10:
            return f"{self.title} S{self.season}E0{self.episode} zobaczono {self.views} razy."
        else:
            return f"{self.title} S{self.season}E{self.episode} zobaczono {self.views} razy."
    def play(self, view = 1):
        self.views += view

import random
from datetime import date
day = date.today()
today = day.strftime("%d/%m/%Y")

collections = [] #lista zawierająca wszystkie filmy oraz seriale.

collections.append(Movie('Aligator 5','Prześmiewczy', '2000', 300))
collections.append(Series(1, 30 ,'Baaa!','Ironiczny', '2005', 30000))
collections.append(Movie('Mysz Komputerowa','Sci-fi', '1992', 1))
collections.append(Movie('Arbuz Powraca','Dramat', '2020', 123456))
collections.append(Series(20, 2, 'Eeee?', 'Komedia', '1999', 0))
collections.append(Series(3, 2, 'Hmm?', 'Komedia', '1993', 30))
collections.append(Series(12, 19, 'Zero Wyświetleń Dużo Sezonów', 'Kryminał', '1899', 0))


#Funkcja dodająca film.
def add_movie(collection):
    title = input("Nazwa filmu: ").title()
    genre = input("Gatunek: ").title()
    year = input("Rok wydania: ")
    collection.append(Movie(title, genre, year, views= 0))

# Funkcja dodająca serial (tyle odcinków ile wprowadzona wartość)
def add_series(collection):
    title = input("Nazwa serialu: ").title()
    genre = input("Gatunek: ").title()
    year = input("Rok wydania: ")
    season = int(input("Sezon: "))
    episode = int(input("Liczba odcinków do dodania: "))
    if episode > 1:
        for i in range(1, episode + 1):
            collection.append(Series(season, i, title, genre, year, views= 0))
    else:
        collection.append(Series(season, episode, title, genre, year, views= 0))

# Funkcja wyświetla tylko filmy alfabetycznie
def get_movie(collection):
    temp = []
    for movie in collection:
        if isinstance(movie, Series):
            pass
        else:
            temp.append(movie)
    by_title =  sorted(temp, key= lambda title: title.title)
    for i in by_title:
        print(i)

# Funkcja wyświetla tylko seriale alfabetycznie
def get_series(collection):
    temp = []
    for series in collection:
        if isinstance(series, Series):
            temp.append(series)
    by_title = sorted(temp, key= lambda title: title.title)
    for i in by_title:
        print(i)

# Funkcja wyświetla tytuł film/serialu jeśli znajduje się w bibliotece
def search(collection):
    user_input = input("Wprowadź szukany tytuł: ").title()
    for title in collection:
        if title.title == user_input:
            return title
    else:
        return f"Nie ma takiego filmu w bibliotece: {user_input} "

# Dodaje losową wartość do liczby wyświetleń
def generate_views(collection):
    temp = random.choice(collection)
    temp.views += random.randint(1, 101)

# Wykorzystuje funkcję dodająca wartość do l. wyświetleń wykonująć ją 10 razy
def multi_views(collection):
    for _ in range(1,11):
        generate_views(collection)

# Wyświetla top oglądanych seriali/filmów
def top_titles(collection, content_type):
    if content_type.lower().strip() == 'film':
        temp = []
        for movie in collection:
            if isinstance(movie, Series):
                pass
            else:
                temp.append(movie)
        by_views = sorted(temp, key= lambda views: views.views, reverse= True)
        num_of_top = int(input(f"Ile filmów chcesz wyświetlić(max {len(by_views)}): "))
        print(f"Top {num_of_top} filmów na dzień dzisiejszy {today} to: ")
        for i in range(1, num_of_top):
            print(by_views[i])
    elif content_type.lower().strip() == 'serial':
        temp = []
        for series in collection:
            if isinstance(series, Series):
                temp.append(series)
        by_views = sorted(temp, key= lambda views: views.views, reverse= True)
        num_of_top = int(input(f"Ile seriali chcesz wyświetlić(max {len(by_views)}): "))
        print(f"Top {num_of_top} seriali na dzień dzisiejszy {today} to: ")
        for i in range(1, num_of_top):
            print(by_views[i])
    else:
        print("Tylko film lub serial.")

# Wyświetla instrukcję
def show_info():
    print('''
    1: Wyświetlić całą biblioteke
    2: Dodać film
    3: Dodać serial
    4: Wyświetlić tylko filmy
    5: Wyświetlic tylko seriale
    6: Wyszukać film/serial
    7: Dodać wyświetleń
    8: Wyświetlić listę TOP względem wyświetleń
    9: Wyświetlić pomoc
    0: Zakończyć program''')

# Funkcja wywołująca powyższe funkcje
def interface(collection):
    while True:
        user_input = input("Co chcesz zrobić?: ")
        if user_input == '1':
            print('Moja Biblioteka:')
            for elements in collection:
                print(elements)
        elif user_input == '2':
            add_movie(collection)
        elif user_input == '3':
            add_series(collection)
        elif user_input == '4':
            get_movie(collection)
        elif user_input == '5':
            get_series(collection)
        elif user_input == '6':
            print(search(collection))
        elif user_input == '7':
            secound_input = input('1: Aby dodać jednorazowo, 2: Aby dodać x10 ')
            if secound_input == '1':
                generate_views(collection)
            else:
                multi_views(collection)
        elif user_input == '8':
            third_input = input("film: top filmów, serial: top seriali ")
            top_titles(collection, third_input)
        elif user_input == '9':
            show_info()
        elif user_input == '0':
            break
        else:
            print("Zły numer")
    
if __name__ == '__main__':
    show_info()
    interface(collections)