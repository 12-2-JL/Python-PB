
def bubblesort(victim):
    for i in range(len(victim)):
        j=i+1  
        for j in range(len(victim)):
            if victim[i]>victim[j]:
                victim[i], victim[j]=victim[j], victim[i]
                
        print(victim)   

things=[10, 2, 6, 3, 8, 7, 14]
print("unsorted list:", things)
print(bubblesort(things))
