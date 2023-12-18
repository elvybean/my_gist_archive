## python script that calculates the number of possible serial numbers for 
# Star Wars Astromech Droids from the same line as R2-D2 (P, Q and R series)
letters = ["P", "Q", "R"]
Astromechs = []

for i in letters:
    for j in range(1, 100):
        for k in letters:
            for l in range(1, 100):
                tempStr = i + str(j),"-",k + str(l)
                Astromechs.append(tempStr)

print(len(Astromechs))
print(Astromechs)