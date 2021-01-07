'''
Funkcja sprawdzająca czy podane słowo jest palindromem
'''
def is_palindrome(word):
  return word == word[::-1]

word_given = input("Podaj słowo: ")
if is_palindrome(word_given):
  print(f"Tak, {word_given} to palindrom")
else:
  print(f"{word_given} nie jest palindromem")



  
