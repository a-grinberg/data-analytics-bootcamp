import datetime as d

birthday = list(input("Enter the date of your birthday (dd/mm/yyyy): ").split("/"))
age = int(d.datetime.now().year) - int(birthday[-1])
candles = int(str(age)[-1])

print(f"""     ___{'i' * candles}___
    |:H:a:p:p:y:|
  __|___________|__
 |^^^^^^^^^^^^^^^^^|
 |:B:i:r:t:h:d:a:y:|
 |                 |
 ~~~~~~~~~~~~~~~~~~~""")