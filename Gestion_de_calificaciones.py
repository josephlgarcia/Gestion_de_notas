
while True:
    notas_verificadas = []
    notas_verificadas_numericamente = []
    notas_invalidadas_por_caracter = []
    notas_invalidadas_por_rango = []

    notas = input("Ingrese sus calificaciones, del 1 al 100, separadas por comas (ej: 40, 20, 90, ...): ")
    notas = notas.split(",")

    for nota in notas:
        try:
            nota_float = float(nota.replace(" ", ""))
            notas_verificadas_numericamente.append(nota_float)
        except ValueError:
            notas_invalidadas_por_caracter.append(nota)
    
    if len(notas_invalidadas_por_caracter) != 0:
        print(f"{notas_invalidadas_por_caracter} no es un número")
        print("Ingrese solo números que representen sus calificaciones para poder gestionarlas ")
    else:
        for nota in notas_verificadas_numericamente:
            if nota < 0 or nota > 100:
                notas_invalidadas_por_rango.append(nota)
            else:
                notas_verificadas.append(nota)

    if len(notas_invalidadas_por_rango) != 0:
        print(f"{notas_invalidadas_por_rango} se encuentra fuera del rango (0, 100), ingrese solo datos que estén comprendidos entre 0 y 100")

    if not notas_invalidadas_por_caracter and not notas_invalidadas_por_rango:
        break



print(f"Sus notas agregadas fueron: {notas_verificadas}")

suma = 0

for nota in notas_verificadas:
    suma = suma + nota

promedio = (suma / len(notas_verificadas))


if promedio >= 80:
    print(f"Felicidades, aprobó con excelencia :). Su promedio es {promedio:.2f}")
elif promedio >= 60 and promedio < 80:
    print(f"Aprobó, pero se puede mejorar :). Su promedio es {promedio:.2f}")
elif promedio >= 40 and promedio < 60:
    print(f"Reprobó, todavía se puede :). Su promedio es {promedio:.2f}")
else:
    print(f"Reprobó miserablemente. Su promedio es {promedio:.2f}")


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

while i < len(notas_verificadas):
    if nota_especifica < notas_verificadas [i]:
        contador1 += 1
    i += 1

if contador1 == 0:
    print(f"No existen calificaciones mayores a {nota_especifica}")
elif contador1 == 1:
    print(f"Hay una calificación mayor a {contador1}")
else:
    print(f"Existen {contador1} calificaciones mayores a {nota_especifica}")


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

for nota in notas_verificadas:
    if nota_especifica not in notas_verificadas:
        break
    elif nota_especifica != nota:
        continue
    else:
        contador2 +=1

if contador2 == 0:
    print(f"La nota {nota_especifica} no se encuentra en la lista")
elif contador2 == 1:
    print(f"La nota {nota_especifica} se repite {contador2} vez")
else:
    print(f"La nota {nota_especifica} se repite {contador2} veces")