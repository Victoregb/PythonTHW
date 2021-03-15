#this is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that *args sobra, asi que fuera
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
    
#este toma solo un argumento
def print_one(arg1):
    print(f"arg1: {arg1}")
    
    
#este no tiene argumentos.
def print_none():
    print("No me dieron nada!")
    
print_two("Victor", "Gil")
print_two_again("Victor", "Gil")
print_one("Holaaaa!")
print_none()