def solicitar_notas():
    notas = []
    for curso in range(3):
        print(f"\nCurso {curso + 1}:")
        curso_notas = []
        for estudiante in range(5):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota del estudiante {estudiante + 1}: "))
                    curso_notas.append(nota)
                    break
                except ValueError:
                    print("Error: Ingrese un valor numérico válido.")
        notas.append(curso_notas)
    return notas

def calcular_promedio_total(notas):
    total_notas = [nota for curso_notas in notas for nota in curso_notas]
    promedio_total = sum(total_notas) / len(total_notas)
    return promedio_total

def calcular_promedio_por_grupo(notas):
    promedios_grupo = []
    for curso_notas in notas:
        promedio_curso = sum(curso_notas) / len(curso_notas)
        promedios_grupo.append(promedio_curso)
    return promedios_grupo

def calcular_porcentaje_aprobados(notas):
    aprobados_por_grupo = []
    for curso_notas in notas:
        aprobados = sum(nota >= 70 for nota in curso_notas)
        porcentaje_aprobados = (aprobados / len(curso_notas)) * 100
        aprobados_por_grupo.append(porcentaje_aprobados)
    return aprobados_por_grupo

def obtener_notas_extremas_por_grupo(notas):
    notas_maximas = []
    notas_minimas = []
    for curso_notas in notas:
        max_nota = max(curso_notas)
        min_nota = min(curso_notas)
        notas_maximas.append(max_nota)
        notas_minimas.append(min_nota)
    return notas_maximas, notas_minimas

def mostrar_informacion(notas):
    print("\n--- Notas de los estudiantes ---")
    for curso in range(len(notas)):
        print(f"\nCurso {curso + 1}:")
        for estudiante in range(len(notas[curso])):
            print(f"Estudiante {estudiante + 1}: {notas[curso][estudiante]}")
    print("\n--- Información general ---")
    promedio_total = calcular_promedio_total(notas)
    print(f"Promedio total: {promedio_total:.2f}")

    promedios_grupo = calcular_promedio_por_grupo(notas)
    for curso in range(len(promedios_grupo)):
        print(f"Promedio del Curso {curso + 1}: {promedios_grupo[curso]:.2f}")

    porcentajes_aprobados = calcular_porcentaje_aprobados(notas)
    for curso in range(len(porcentajes_aprobados)):
        porcentaje = porcentajes_aprobados[curso]
        print(f"Porcentaje de aprobados en el Curso {curso + 1}: {porcentaje:.2f}%")

    notas_maximas, notas_minimas = obtener_notas_extremas_por_grupo(notas)
    for curso in range(len(notas_maximas)):
        print(f"Nota máxima en el Curso {curso + 1}: {notas_maximas[curso]}")
    for curso in range(len(notas_minimas)):
        print(f"Nota mínima en el Curso {curso + 1}: {notas_minimas[curso]}")

def menu():
    notas = solicitar_notas()
    mostrar_informacion(notas)

if __name__ == "__main__":
    menu()

