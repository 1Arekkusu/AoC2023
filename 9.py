
def difference(Numbers):
    v = []
    stop = True
    for i in range(0, len(Numbers) - 1):
        v.append(Numbers[i+1] - Numbers[i])
        if v[i] != 0:
            stop = False
    if stop == True:
        return v[len(v) - 1]
    else:
        return v[len(v)-1] + difference(v)

def reversedifference(Numbers):
    v = []
    stop = True
    for i in range(0, len(Numbers) - 1):
        v.append(Numbers[i+1] - Numbers[i])
        if v[i] != 0:
            stop = False
    if stop == True:
        return v[0]
    else:
        return v[0] - reversedifference(v)
        
        

ans1 = 0
ans2 = 0

with open("advent2023\input.txt", 'r') as f:
    for line in f:
        line = line.strip()
        Numbers = []
        StringNumbers = line.split()
        for i in range(0,len(StringNumbers)):
            Numbers.append(int(StringNumbers[i]))
        ans1 += difference(Numbers) + Numbers[len(Numbers)-1]
        ans2 += Numbers[0] - reversedifference(Numbers)

print(ans1)
print(ans2)
