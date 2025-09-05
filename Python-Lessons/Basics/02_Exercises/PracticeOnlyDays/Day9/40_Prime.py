# ---Check if a number is prime---

n = int(input("Enter the number: "))
prime = False
if n < 2:
    print("The number is not prime.")
else:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print("The number is not prime.")
            break
    else: 
        prime = True
if prime:
    print("The number is prime.")