x, y=int(3), int(6)
currentposition=x
totaldistance=0
i=0
while True:
    if i%2==0:
        move=x+2**i
    else:
        move=x-2**i
    
    if min(currentposition, move)<=y<=max(currentposition, move):
        totaldistance+=abs(currentposition-y)
        break
    else:
        totaldistance+=abs(move-currentposition)
        currentposition=move
        i+=1

print(totaldistance)

