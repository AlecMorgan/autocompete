import fileinput

def listify(string):
    return sorted(list(string))

inp = fileinput.input()
anamaybes = []
for line in inp:
    new_anamaybe = sorted(list(map(listify, line[:-1])))
    anamaybes.append(new_anamaybe)

n_anagrams = 0
while anamaybes != []:
    potential_anagram = anamaybes.pop()
    for anamaybe in anamaybes:
        if anamaybe == potential_anagram:
            n_anagrams += 1

print(n_anagrams)