from sys import exit

def salon(inventario):
    """La primera sala, puedes coger una lupa, o varias. Es magia!!!"""
    elementos = [["Una silla", "junto a la mesa", "no "], 
                 ["Un señor en un cuadro", "mirandote", "no "], 
                 ["Una lupa", "sobre un neceser", "" ]]
    inv = inventario 
    
    print("El salon parece normal.")
    print("Quieres investigar?\nsi o no")
    investiga = input(">")
    if investiga == "si":
        for i in elementos:
            print("{} esta {}, {}parece interesante.".format(*i))
            input()
        print("Te acercas a la mesa.")
        accion = input("Quieres cojer la lupa? si o no\n> ")
        if accion == "si":
            lupa = True
            inv.append("lupa")
        else:
            lupa = False
        
    else:
        print("Pero que aburrido eres.")
        exit(0)
        
    if lupa == True:
        print("Con la lupa en tus manos te acercas al cuadro.")
        print("El señor del cuadro se muestra contrariado.")
        print("Te señala la puerta.")
        accion = input("Ir a la puerta. Seguir en el salon.\n> ")
        if accion == "ir a la puerta":
            cocina(inv)
        else:
            salon(inv)
    else:
        print("Hay tambien una puerta.\nQue quieres hacer? quedarte o seguir")
        accion = input("> ")
        if accion == "quedarme":
            salon(inv)
        elif accion == "seguir":
            cocina(inv)
        else:
            print("Te has tropezado. Y caes…")
            muerte(inv)
        
def cocina(inventario):
    """La cocina, un sitio donde pondás a prueba tus habilidades. Pero no las que tu piensas"""
    inv = inventario
    print("Entras en la concina. Esta vacia.")
    puzzle_uno(inv)
    if "lupa" in inv:
        accion = input("Quieres investi  la cocina? si o no\n> ")
        if accion == "si":
            print("Bien, eres toda una exploradora!")
            exit(0)
        else:
            print("Buuuu!")
            exit(0)
    else:
        print("Igual deverías volver al salón.\nZas!")
        salon(inv)
        
def muerte(inventario):
    """La muerta nos llega a todos. Es una forma de escapar. Y si necesitas escapar, pide ayuda."""
    print("... en la oscuridad.")
    print("Pese a contar con: ")
    for i in inventario:
        print(f"{i}\n")
    print("No has logrado superar la prueba. Quizás... en otra vida.")
    exit(0)
    
def puzzle_uno(inventario):
    """El primer reto, pa' tontos"""
    print("En el aire frente a ti aparece 3 + 2")
    print("'Responde', resuena una voz en tu cabeza")
    respuesta = input("> ")
    if respuesta == "5" or respuesta == "cinco":
        print("Correcto.")
        return inventario
    else:
        print("Ahora lo perderás todo.")
        inventario = []
        return puzzle_dos(inventario)
    
def puzzle_dos(inventario):
    """El segundo reto, fracasar es una salida rápida."""
    print("Esta es para ti, venga, 1 + 1")
    respuesta = input("> ")
    if respuesta == "2" or respuesta == "dos":
        print("Correcto, puedes seguir.")
        return 0
    else:
        print("No te da... te ahorraré sufrimientos.")
        print("De repente no sientes nada y estas...")
        return muerte(inventario)
    
    
        
salon(inventario=[])
