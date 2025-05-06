import re
N=3
Cows=["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
Cows.sort()
Orders=[]
restrictions = []
lines = [
    "Buttercup must be milked beside Bella",
    "Blue must be milked beside Bella",
    "Sue must be milked beside Beatrice"
]

for line in lines:
    parts = line.split()
    a = parts[0]
    b = parts[-1]
    restrictions.append((a, b))
    
    
def P(anOrder):
    if len(anOrder)==8:
         Orders.append(anOrder.copy())
         return
    
    for i in Cows:
        if i not in anOrder:
            anOrder.append(i)
            P(anOrder)
            anOrder.pop()

P([])
for j in Orders:
    for a, b in restrictions:
        if abs(j.index(a) - j.index(b)) > 1:
            break
    else:
        for i in j:
            print(i)
        break