#importeert de functies die nodig zijn voor het gebruiken van de microbit en importeert de randint functie voor het rollen van een dobbelsteen
from microbit import *
from random import randint

#het diceroller programma bestaat uit twee compartimenten:
#1. het kiesgedeelte. Hierin kan de gebruiker van het programma het type dobbelsteen kiezen dat hij/zij wil gebruiken om een random getal te genereren. wanneer de dobbelsteen gekozen is, komt de gebruiker in
#2. het rolgedeelte. Hierin schudt de gebruiker om de gekozen dobbelsteen te rollen en drukt de knoppen in om de advantage of disadvantage functies te gebruiken.

#een lijst met alle type dobbelstenen die we willen kunnen gaan rollen
dicebag = [2, 4, 6, 8, 10, 12, 20, 100]
#i is de variabele waarmee we door met 1 omhoog of omlaag te veranderen de plek in de lijst waar we 'nu' zijn kunnen veranderen
i = 0
#door p (i modulo lengte van de lijst met alle opties) te nemen krijgen we de plek in de lijst. Omdat i groter dan het aantal items in de lijst gaat worden hebben we p nodig om nog steeds een plek in de lijst aan te geven.
p = i%len(dicebag)

#de functie updateVar update alle variabelen die nodig zijn na het kiezen van een nieuwe i. Deze hebben we in een functie gestopt omdat 1 regel code om alle variabelen te updaten uiteindelijk minder regels is dan iedere keer a[art alle variabelen te updaten.
#als eerste updaten we p om van i een plek in de lijst 'dicebag' te maken. Daarna stellen we het 'type' dobbelsteen gelijk aan de waarde die de plek op de lijst die p aangeeft heeft. Dan laten we type zien o[ het scherm van de microbit.
def updateVar():
    p = i%len(dicebag)
    type = dicebag[p]
    display.scroll(type)
    
#dit is de hoofdloop van het kiesgedeelte van het programma.
while True:
    #wanneer de microbit geschud wordt berekenen we het type dobbelsteen dat gekozen is in de lijst met de updateVar() functie en laten we deze zien. dan stellen we d (voor Dice) gelijk aan type, wat gelijk is aan het item op plek p (die we gekozen hebben door middel van i) in de lijst dicebag
    if accelerometer.was_gesture("shake"):
        updateVar()
        d = type
        break
    #als de microbit niet geschud wordt gaan we door naar als knop b wordt ingedrukt. Hiermee veranderen we i met een waarde van 1 en berekenen we daarna het item in de lijst dicebag dat we nu zouden kunnen kiezen door te schudden.
    elif button_b.is_pressed():
        i += i
        updateVar()
    #wanneer op knop a gedrukt wordt doen we hetzelfde als bij knop b, maar dan gaan we een item terug in de lijst.    
    elif button_a.is_pressed():
        i -= i
        updateVar()
        
#functies definieren voor rolgedeelte
#roll() is een functie die een random getal tussen 1 en de variabele d toewijst aan de variabele r en die vervolgens laat zien op het scherm. d was gelijk aan het type dobbelsteen, dus als we een d20 gekozen hebben kiest randint(1, d) een getal tussen 1 en 20.
def roll():
    r = randint(1, d)
    display.scroll(r)

#advantage() is een functie die twee random getallen tussen 1 en d kiest voor de variabelen r1 en r2. vervolgens vergelijkt de functie deze en laat de hoogste zien. Gebruikmaken van de advantagefunctie geeft dus een grotere kans op een hoger getal.
def advantage():
    r1 = randint(1, d)
    r2 = randint(1, d)
    if r1 > r2:
        display.scroll(r1)
    else:
        display.scroll(r2)

#disadvantage() is een functie die exact hetzelfde doet als de advantage() functie, maar laat dan de laagste van r1 en r2 zien. Gebruikmaken van de disadvantage functie geeft dus een grotere kans op een lager getal.
def disadvantage():
    r1 = randint(1, d)
    r2 = randint(1, d)
    if r1 < r2:
       display.scroll(r1)
    else:
        display.scroll(r2)
        
#hoofdloop van rolgedeelte
while True:
    #als knop a wordt ingedrukt en tegelijkertijd geschud dan voert het programma de functie advantage() uit.
    if button_a.is_pressed() and accelerometer.was_gesture("shake"):
        advantage()
    #als de knop b wordt ingedrukt en tegelijkertijd geschud dan voert het programma de functie disadvantage() uit.
    elif button_b.is_pressed() and accelerometer.was_gesture("shake"):
        disadvantage()
    #als de microbit geschud wordt zonder een knop in te drukken dan voert het programma de gewone roll() uit.
    elif accelerometer.was_gesture("shake"):
        roll()
    #de loop stopt wanneer knop a en b tegelijkertijd worden ingedrukt. Het programma gaat dan verder naar display.clear, wat een zwart scherm geeft. Dit is als het ware een 'uit-knop'.
    elif button_a.is_pressed() and button_b.is_pressed():
        break
display.clear()