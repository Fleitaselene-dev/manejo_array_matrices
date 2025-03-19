print("--Registro de personas--")
print("Si desea terminar escriba 'finalizar' en el campo nombre.")

personas = []
    

    
while True: 
        nombre = input("Nombre: ")
        if nombre.lower() == "finalizar":
            break
        edad = (input("Edad: "))
        nota = int(input("Nota: "))

        personas.append([nombre, edad, int(nota)])
      


print("Lista de personas: ")
for persona in personas:
    print(f"Nombre: {persona[0]}, Edad: {persona[1]}, Nota: {persona[2]}")


notas = sorted(personas, key=lambda x: int(x[2]), reverse=True)


print("\nLista por nota: ")
for persona in notas:
    print(f"Nombre: {persona[0]}, Edad: {persona[1]}, Nota: {persona[2]}")