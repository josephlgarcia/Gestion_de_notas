
# Mensaje de bienvenida alprograma
print("")
print("="*100)
print("                Bienvenido al programa de gestión de calificaciones")
print("="*100)
print("")



#Bucle infinito para ingresar las calificaciones, solo se detiene cuando se ingresan correctamente
while True:
    # Listas necesarias para almacenar las notas
    notas_verificadas = [] 
    notas_verificadas_numericamente = [] 
    notas_invalidadas_por_caracter = [] 
    notas_invalidadas_por_rango = [] 

    notas = input("Ingrese sus calificaciones, del 1 al 100, separadas por comas (ej: 40, 20, 90, ...): ") 
    notas = notas.split(",") # separa las notas por comas

    for nota in notas:
        try:
            nota_float = float(nota.replace(" ", ""))
            notas_verificadas_numericamente.append(nota_float)
        except ValueError:
            notas_invalidadas_por_caracter.append(nota) # si no se puede convertir a float, se agrega a la lista de notas inválidas por carácter
    
    if len(notas_invalidadas_por_caracter) != 0:
        print(f"{notas_invalidadas_por_caracter} no es un número") # En caso de existir caracteres no numéricos, se imprime el mensaje mostrando la lista de notas inválidas
        print("Ingrese solo números que representen sus calificaciones para poder gestionarlas ")
    else:
        # Verifica si las notas están dentro del rango permitido
        for nota in notas_verificadas_numericamente:
            if nota < 0 or nota > 100:
                notas_invalidadas_por_rango.append(nota)
            else:
                notas_verificadas.append(nota)

    # Si hay notas inválidas por rango, se imprime el mensaje y se solicita nuevamente la entrada
    if len(notas_invalidadas_por_rango) != 0:
        print(f"{notas_invalidadas_por_rango} se encuentra fuera del rango (0, 100), ingrese solo datos que estén comprendidos entre 0 y 100")

    if not notas_invalidadas_por_caracter and not notas_invalidadas_por_rango:
        break # Si no hay notas inválidas, se sale del bucle



print(f"\nSus notas agregadas fueron: {notas_verificadas}") # imprime las notas válidas

suma = 0

for nota in notas_verificadas: 
    suma = suma + nota

promedio = (suma / len(notas_verificadas)) # calcula el promedio de las notas

# Imprime el resultado según el promedio
if promedio >= 80:
    print(f"\nFelicidades, aprobó con excelencia :). Su promedio es {promedio:.2f}")
elif promedio >= 60 and promedio < 80:
    print(f"\nAprobó, pero se puede mejorar :). Su promedio es {promedio:.2f}")
elif promedio >= 40 and promedio < 60:
    print(f"\nReprobó, todavía se puede :). Su promedio es {promedio:.2f}")
else:
    print(f"\nReprobó, debe esforzarse un poco más. Su promedio es {promedio:.2f}")


while True:
    try:
        nota_especifica = input("Ingrese la nota para saber cuántos números en la lista son mayores a ella: ")
        nota_especifica = float(nota_especifica)
        if nota_especifica < 0 or nota_especifica > 100:
            print(f"{nota_especifica} se encuentra fuera del rango (0, 100), ingrese solo datos que estén comprendidos entre 0 y 100")
        else:
            break
    except ValueError:
        print("Ingrese un valor numérico")


i = 0
contador1 = 0

# Recorre la lista de notas verificadas y cuenta cuántas son mayores a la nota específica
while i < len(notas_verificadas):
    if nota_especifica < notas_verificadas [i]:
        contador1 += 1
    i += 1

# Imprime el resultado según la cantidad de notas mayores a la nota específica
if contador1 == 0:
    print(f"\nNo existen calificaciones mayores a {nota_especifica}")
elif contador1 == 1:
    print(f"\nHay una calificación mayor a {contador1}")
else:
    print(f"\nExisten {contador1} calificaciones mayores a {nota_especifica}")


while True:
    try:
        nota_especifica = input("Ingrese una nota para saber cuántas veces aparece: ")
        nota_especifica = float(nota_especifica)
        if nota_especifica < 0 or nota_especifica > 100:
            print(f"{nota_especifica} se encuentra fuera del rango (0, 100), ingrese solo datos que estén comprendidos entre 0 y 100")
        else:
            break
    except ValueError:
        print("Ingrese un valor numérico")


contador2 = 0

# Recorre la lista de notas verificadas y cuenta cuántas veces aparece la nota específica
for nota in notas_verificadas:
    if nota_especifica not in notas_verificadas:
        break
    elif nota_especifica != nota:
        continue
    else:
        contador2 +=1

# Imprime el resultado según la cantidad de veces que aparece la nota específica
if contador2 == 0:
    print(f"\nLa nota {nota_especifica} no se encuentra en la lista")
elif contador2 == 1:
    print(f"\nLa nota {nota_especifica} se repite {contador2} vez")
else:
    print(f"\nLa nota {nota_especifica} se repite {contador2} veces")


# Fin del programa con mensaje de despedida
print("Gracias por usar el programa, hasta luego... :)\n")