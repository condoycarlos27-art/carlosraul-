# Plan de materias según semestre y rendimiento
semestre = int(input("Semestre actual (1-4): "))
promedio = float(input("Promedio actual: "))
match semestre:
    case 1 | 2: materias = 5
    case 3 | 4: materias = 4
    case _: print("Semestre inválido"); exit()
if promedio >= 8.5: materias += 1
elif promedio < 7: materias -= 1
materias = max(3, min(6, materias))
print(f"Materias recomendadas: {materias}")
