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