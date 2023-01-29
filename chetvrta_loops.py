#Da se napravi programa vo koja korisnikot vo koja korisnikot ke moze da vnesuva 
# broevi se dodeka ne izbere deka poveke ne saka da vnesuva, da vnesuva licni podatoci na lica, 
# da se prebroi kolku se bile vneseni polnoletni kolku maloletni
print("Vnesuvanjeto na podatoci ke prestani vo momentot koga ke napishete stop")
polnoletni=0
maloletni=0
while True:
    ime=(input("Vnesete go vasheto ime\t"))
    godini=int(input("Vnesete gi vashite godini"))
    rabota=str(input("Vnesete ja vashata rabotna pozicija"))
    pol=str(input("Vnesete go vashiot pol"))
    
    if godini>18:
        polnoletni+1
    else:
        maloletni+1
    if ime=="stop":
    break
    print("Vkuplno bea vneseni {} polnoletni lica i {} maloletni lica".format(polnoletni,maloletni))
