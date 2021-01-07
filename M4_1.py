'''
Funkcja sprawdzająca czy podane słowo jest palindromem
'''
def is_palindrome(word):
  print(word == word[::-1])

word_given = input("Podaj słowo: ")
is_palindrome(word_given)



  
