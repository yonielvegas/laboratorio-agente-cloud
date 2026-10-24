from tasks import agregar_tarea, completar_tarea, editar_tarea, eliminar_tarea, pendientes

tareas = []

agregar_tarea(tareas, "Estudiar agentes cloud", "Estudio")
agregar_tarea(tareas, "Preparar laboratorio", "Trabajo")
editar_tarea(tareas, 2, "Preparar laboratorio final", "Estudio")
completar_tarea(tareas, 1)
eliminar_tarea(tareas, 1)

for tarea in pendientes(tareas):
    print(f'- {tarea["id"]}: {tarea["titulo"]}')