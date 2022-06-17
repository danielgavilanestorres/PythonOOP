from clases.jugador import jugador
from clases.pirata import pirata
from clases.ninja import ninja

print("Juego NINJAS VS PIRATAS")
print("Jugador N°1")

pirata1 = pirata("Jack")
jug1Pirata = jugador.jugadorPirata("Daniel", 34, "M", pirata1)

ninja1 = ninja("Eloy")
jug2Ninja = jugador.jugadorNinja("Paty", 30, "F", ninja1)


print("INICIANDO EL JUEGO....\n")

while (jug2Ninja.ninjas.salud >= 0 or jug1Pirata.piratas.salud <= 0):
    
    if (jug2Ninja.ninjas.salud <= 0):
        print(f"JUEGO FINALIZADO, el ganador es {jug1Pirata.nombre}")
        break
    else:
        print(f"Jugador 1 {jug1Pirata.nombre}- Ataca ")
        ataqueJug1 = int(input("Valor Ataque: "))
        jug1Pirata.piratas.atacar(ataqueJug1, ninja1)
        jug2Ninja.ninjas.mostrarEstado()

    if (jug1Pirata.piratas.salud <= 0):
        print(f"JUEGO FINALIZADO, el ganador es {jug2Ninja.nombre}")
        break
    else:
        print(f"Jugador 2 {jug2Ninja.nombre}- Ataca")
        ataqueJug2 = int(input("Valor Ataque: "))
        jug2Ninja.ninjas.atacar(ataqueJug1, pirata1)
        jug1Pirata.piratas.mostrarEstado()








