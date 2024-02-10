# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:54:28 2023

@author: brams
"""


import numpy as np
from timeit import default_timer as timer

ds = np.random.randint(100, size=1000) # maak een dataset van 100 lang met getalen tussen 0 en 99

start1 = timer() # kijk wat de tijd is op dit moment

ds_gem1      = round(np.average(ds),2) # bereken het gemidelde van de dataset
ds_med1      = round(np.median(ds),2) # vind de median van de dataset
ds_std1      = round(np.std(ds),2) # bereken de standaarddeviatie van de dataset

end1  = timer() # kijk wat de tijd is op dit moment

tijd1 = end1 - start1 # bereken hoelang het duurde om de berekening te doen

def std(data): # functie voor het berekenen van de standaarddevatie
    x      = [] # maak een lege lijst
    
    for i in data:
        y = (i - ds_gem2) ** 2 # voor elke element in de dataset trek het gemidelde er van af en kwadrateer het 
        x.append(y) # voeg het boven stande getal toe aan de lege lijst
    
    z = (sum(x) / len(data)) ** (1/2) # van lijst x vind de som en deel het door de lengte, vervolgens neem de wortel
    return (z) # geef z

def gem(data): # functie voor het berekenen van het gemidelde 
    x = sum(data) # vind de som van de gegeven data
    y = len(ds) # vind hoeveel datapunten er zijn 
    return (x / y) # deel de som door de hoeveelheid data punten

def med(data): # functie voor het vinden van median
    x = sorted(data) # sorteer de data van klein naar groot
    y = len(data) # vind hoeveel datapunten er zijn
    if y % 2 == 0: # kijk of er een even of oneven aantal data punten zijn door te delen door twee en als er geen commagetal uit komt is het even
        a = x[int(y/2)] # als de hoeveelheid even is vind het eerst middelste getal door de hoeveelheid data punten door twee te delen 
        b = x[((int(y/2)) + 1)] # vind het tweede midelste getal door het volgende getal te paken vergelijken met het getal hier boven
        return ((a + b) / 2) # vind het gemidelde van de twee midelste getallen
    else:
        return (x[int((y/2) + .5)]) # als het een oneven getal is deel de hoeveelheid datapunten door twee en tel er een half bij op om het middelste getal te vinden
        
start2 = timer() # kijk wat de tijd is op dit moment

ds_gem2      = round(gem(ds),2) # bereken het gemidelde van de dataset
ds_med2      = round(med(ds),2) # vind de median van de dataset
ds_std2      = round(std(ds),2) # bereken de standaarddeviatie van de dataset

end2 = timer() # kijk wat de tijd is op dit moment

tijd2 = end2 - start2 # bereken hoelang het duurde om de berekening te doen

tijd_ = tijd2 / tijd1 # bereken de verhouding tussen de twee manieren van berekenen

print('Er is op twee manieren het gemiddelde, de median en de standaarddeviatie berekend.'
      'Eerst met de fucties van numpy en ten tweede met zelf geschreven functies.'
      f'Met de numpy functies duurde het {tijd1} seconde en met de zelf geschreven functies duurde het {tijd2} seconde.'
      f'Het is dus duidelijk te zien dat het met numpy functies veel sneller namelijke {tijd_} keer.')
print('Hier onder volgenden de waardes berekent met de numpy functies.')
print(f'Het berekende gemiddelde is {ds_gem1}')
print(f'De gevonden median is {ds_med1}')
print(f'De berekende standaarddeviatie is {ds_std1}')