Vnum = []
a = " "

for i in range(20):
    Vnum.append(i + 1)
    print(Vnum[i], "\n")


for j in range(20):
    Vnum.append(j + 1)
    print(Vnum[j])
    for k in range(j):
        print(" ")
