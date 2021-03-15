the_count = [1, 2, 3, 4, 5, 6, 7]
frutas = ['manzanas', 'peras', 'naranjas', 'albaricoques']
cambio = [1, 'centimos', 2, 'duros', 3, 'denarios']

# this first kind of for-loop goes through a list
for num in the_count:
    print(f"This is count {num}.")

for frut in frutas:
    print(f"A fruit of type: {frut}")

for i in cambio:
    print(f"Tengo {i}.")

elementos = []

for i in range(0,6):
    print(f"Adding {i} to the list.")
    elementos.append(i)

print(f"Y los elementos que tengo son:\n")
for i in elementos:
    print(f" ->  {i}")
    
lista = [[1,2,3], [4,5,6]]

for i in lista:
    print(f" -> {i}")
    for j in i:
        print(f" -> {j}\n")
    
