import random
from random import choice

#Definicja skinow
CaseItems  = ["AK 47 Frontside Misty","AK 47 Urban Hazard","Glock-18 Bunseen Burner","P250 Business class","USP-S Neo-Noir","AWP Dragon Lore","Desert Eagle Shade", "Glock-18 Night fight","Galil AR Cerberus"]

def LosujSkrzynke():
    randomitem = choice(CaseItems)
    print(randomitem)


#Pobranie iw alidacja liczby do otwarcia
def PobierzLiczbeSkrzynek():
    global CaseCount
    CaseCount = int(input("How many chests do you want to open?[1-5]: "))
    while CaseCount <= 0 or CaseCount > 5:
        CaseCount = int(input("Type in 1 to 5: "))
    return CaseCount


while True:
    try:
        PobierzLiczbeSkrzynek()
    except ValueError:
        print("You need to privde valid input, try again")
        PobierzLiczbeSkrzynek()
    else:
        #correct input
        break

CaseOpened = 0
while CaseOpened != CaseCount:
    LosujSkrzynke()
    CaseOpened += 1