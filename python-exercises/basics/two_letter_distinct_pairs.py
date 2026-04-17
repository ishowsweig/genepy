from string import ascii_lowercase as abc

pairs = []
for i in range(len(abc)):
    for j in range(len(abc)):
        if abc[i] != abc[j]:
            pairs.append(abc[i] + abc[j])

for pair in sorted(pairs):
    print(pair)
