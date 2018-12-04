#by reddit user: makinbakonpancakes
#retrieved from https://www.reddit.com/r/adventofcode/comments/a20646/2018_day_1_solutions/ on 02/12/18 @ 3am UTC



import itertools
data = [int(x) for x in open("1-1-input.txt").readlines()]
print(sum(data))

freq = 0
seen = {0}
for num in itertools.cycle(data):
    freq += num
    if freq in seen:
        print(freq); break
    seen.add(freq)
