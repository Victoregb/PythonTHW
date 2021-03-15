ten_things = "pasta sopa leones garzas ornitorrincos romero"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')

more_stuff = ["lagartos", "tritornes", "lunes", "junio",
              "verano", "año", "anillo", "sopa"]


while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Añadimos: ", next_one)
    stuff.append(next_one)
    print(f"Ahora tenemos {len(stuff)} elementos.")
    
print(f"Ahí lo tenemos, {len(stuff)} elementos.")
print("Vamos a hacer alguna que otra cosa!")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(" ".join(stuff))
print('#'.join(stuff[3:5]))
