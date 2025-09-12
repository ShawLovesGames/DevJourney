# ---Given t = (10, 20, 30, 40), use unpacking to store 10 in a, 20 in b, and the rest in a list rest---

t = (10, 20, 30, 40)

(one, two, *rest) = t

print(one, two, rest)