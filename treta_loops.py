#Da se napravi programa vo koja korisnikot kolku pati da se povtoruva ciklusot, 
# da se ispecatat site parni broevi do brojot koj go vnel korisnikot

pati=int(input("Vnesete kolku pati sakate da se povtori ciklusot"))
for i in range(pati):
    broj=int(input("Vnesete broj"))
    for y in range(broj):
        if y%2==0:
         print("{}".format(y))
    else:
        break