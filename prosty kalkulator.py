import logging

logging.basicConfig(level=logging.INFO)

while True:
  operator = input("""Podaj działanie, posługując się odpowiednią liczbą:
  1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie, 5 WYJŚCIE:""")
  if operator == "5":
    break
  
  list_of_num = input("Podaj dwie lub więcej liczb oddzielonych spacją: ").split()
  result = float(list_of_num[0])

  for numbers in list_of_num[1:]:
    if operator == "1":
      logging.info(f"Dodaję {result} i {numbers}")
      result += float(numbers)
    elif operator == "2":
      logging.info(f"Odejmuję {result} i {numbers}")
      result -= float(numbers)
    elif operator == "3":
      logging.info(f"Mnożę {result} i {numbers}")
      result *= float(numbers)
    else:
      logging.info(f"Dzielę {result} i {numbers}")
      result /= float(numbers)


  print(result)
    
  
