# ---Create a tuple with string elements, then find the longest string in the tuple---

tup = ('apple', 'banana', 'orange')
longest = tup[0]

for i in tup:
    if len(i) > len(longest):
        longest = i

print(f"{longest} is the largest string.")