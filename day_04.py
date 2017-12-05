with open("inputs/day_04.txt") as f:
    lines = f.readlines()

total = 0
for line in lines:
    words = line.split()
    wordSet = set(words)
    if len(words) == len(wordSet): total += 1


print(total)

total = 0
# lines = ["oiai ibii icoi idio",
# "vxjtwn vjnxtw sxibvv mmws wjvtxn icawnd rprh",
# "fhaa qwy vqbq gsswej lxr yzl wakcige mwjrl",
# "bhnlow huqa gtbjc gvj wrkyr jgvmhj bgs umo ikbpdto"]
for line in lines:
    words = line.split()
    wordLists = []
    valid = True
    for word in words:
        wordLists.append(list(word))
    for i, word1 in enumerate(wordLists):
        for j, word2 in enumerate(wordLists):
            if i == j:
                continue
            if sorted(word1) == sorted(word2):
                valid = False
                break
        if not valid:
            break
    if valid:
        total += 1
print(total)