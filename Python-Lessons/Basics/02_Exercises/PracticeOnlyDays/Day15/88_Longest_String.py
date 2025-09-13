# ---Create a tuple with string elements, then find the longest string in the tuple---

lst = ['apple', 'banana', 'orange']
current = len(lst[0])
longest = ""

for i in lst:
    if len(i) > current:
        current = len(i)
        longest = i

print(f"{longest} is the largest string.")