def agregar_tarea(tareas, titulo, categoria):
    titulo = titulo.strip()
    categoria = categoria.strip()
    if not titulo:
        raise ValueError("El título es obligatorio")
    if not categoria:
        raise ValueError("La categoría es obligatoria")

    tarea = {
        "id": max((t["id"] for t in tareas), default=0) + 1,
        "titulo": titulo,
        "categoria": categoria,
        "completada": False
    }
    tareas.append(tarea)
    return tarea


def editar_tarea(tareas, tarea_id, titulo, categoria):
    titulo = titulo.strip()
    categoria = categoria.strip()

    if not titulo:
        raise ValueError("El título es obligatorio")
    if not categoria:
        raise ValueError("La categoría es obligatoria")

    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea["titulo"] = titulo
            tarea["categoria"] = categoria
            return tarea

    raise ValueError("Tarea no encontrada")


def eliminar_tarea(tareas, tarea_id):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == tarea_id:
            return tareas.pop(index)

    raise ValueError("Tarea no encontrada")


def completar_tarea(tareas, tarea_id):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea["completada"] = True
            return tarea

    raise ValueError("Tarea no encontrada")


def pendientes(tareas, categoria=None):
    tareas_pendientes = [t for t in tareas if not t["completada"]]
    if categoria is None:
        return tareas_pendientes

    categoria = categoria.strip().lower()
    return [t for t in tareas_pendientes if t["categoria"].lower() == categoria]