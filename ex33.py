i = 0
numeros = []

while i < 6:
    print(f"At the top i is {i}.")
    numeros.append(i)
    
    i += 1
    print(f"Numeros ahor es:", numeros)
    print(f"At the bottom i is {i}")

print("The numbers:")
for num in numeros:
    print(num)