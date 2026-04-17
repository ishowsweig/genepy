from string import ascii_lowercase

pairs = []

for i in range(len(ascii_lowercase)):
    for j in range(len(ascii_lowercase)):
        pair = ascii_lowercase[i] + ascii_lowercase[j]
        pairs.append(pair)

for pair in sorted(pairs):
    print(pair)
e
