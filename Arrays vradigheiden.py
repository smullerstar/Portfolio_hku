"""
Created on Tue Jan  2 12:05:40 2024
@author: brams
"""
import numpy as np

def matrix (m, n, Min, Max): # random matrix maken / m = rij, n = colom, mi = minimum, ma = maximum
    trix = np.random.randint(Min, Max, size = (m,n))
    return(trix)

def matrix_0 (m, n): # matrix maken met alleen nullen / m = rij, n = colom
    trix = np.zeros((m,n))
    return(trix)

# opdracht 1 

invoer = matrix(5,5,0,20) # input array

uitvoer = np.amax(invoer, axis=1) # zoek het maximum en plaats het in een lijst
    
print('Opdracht 1: Hier wordt de hoogste waarde van elke rij in een nieuwe array gezet.')
print("Input")
print(invoer)
print("Output")
print(f"{uitvoer}\n")

# opdracht 2

invoer = matrix(3,3,-10,10) # input array
uitvoer = invoer
N = 3
for i in range (0, N, 1) :
    uitvoer =  np.append(uitvoer, invoer, axis=1) # verander de matrix door zich zelf toe te voegen N keer

print(f"Opdracht 2: Zet de array {N} keer achter zich zelf")
print("Input")
print(invoer)
print("Output")
print(f"{uitvoer}\n")

# opdracht 3

invoer =  matrix(5, 5, -10, 10)

uitvoer = np.fliplr(invoer) # deze fuctie spiegelt de matrix automaties

print("Opdracht 3: Spiegel de array.")
print("Input")
print(invoer)
print("Output")
print(f"{uitvoer}\n")


# opdracht 4

invoer =  matrix(5, 5, 0, 40)
min_ = 10
max_ = 30
print(f"Opdracht 4: Vervang waarders onder de {min_} met {min_} en waarders boven de {max_} met {max_}")
print("Input")
print(invoer)
invoer[invoer < min_] = min_ # als het kleiner is dan 10 vervang het voor 10
invoer[invoer > max_] = max_ # als het groter is dan 30 vervang het voor 30
print("Output")
print(f"{invoer}\n")


# opdracht 5

M = 15 # M input
N = 8  # N input
start = matrix_0(M, N) # maak een array aan van M bij N met alleen nullen

for i in range(N): # zorgt dat alle rijen op lopen van nul tot N
    start[:,i] = i

for i in range(M): # tel steets een meer op bij alle rijen 
    start[i] += i

print(f"Opdracht 5: Maake een array {M} by {N} en vul dit met het onder staande patroon.")
print(f"{start}\n")

# opdracht 6

M = 10 # M input
N = 7 # N input
start = matrix_0(M, N) # maak een array aan van M bij N met alleen nullen

for i in range(N): # zorgt dat alle rijen op lopen van nul tot N
    start[:,i] = i

for i in range(M):
    for x in range(M):
        if i + x + 1 < M and i + x + 1 <= N: # als het x coordinaat in de array kleiner is dan de het aantal rijen en het is kleiner of gelijk aan het aantal colomen ga verder
            start[i+x+1][i] = 0 # vul het coordinaat [i+x+1][i] met 0 waarbij i en x steeds een groter worden met dat i één groter wordt wanneer x van 0 t/m M is gegaan  
    if i > N: # als i groter is dan N vul de hele rij met 0en 
        start[i] = 0

print(f"Opdracht 6: Maake een array {M} by {N} en vul dit met het onder staande patroon.")
print(f"{start}\n")

