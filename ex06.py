#Declara una variable
type_of_people = 10

#Usa el valor de la variable en la string 
x = f"There are {type_of_people} type of people"

#Declara dos variables, y las usa en una string. // Dos
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

#Imprime las variables.
print(x)
print(y)

#Cuatro?
print(f"I said {x}")
print(f"I said {y}")


#No es una string, sino bolean
hilarius = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarius))

#Junta dos strings, no pone una dentro de otra
w = "This is the left side of…"
e = "a string with a right side"

print(w+e)