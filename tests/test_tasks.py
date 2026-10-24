import unittest
from tasks import agregar_tarea, completar_tarea, editar_tarea, eliminar_tarea, pendientes


class TestTasks(unittest.TestCase):

    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación", "Estudio")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertEqual(tarea["categoria"], "Estudio")
        self.assertFalse(tarea["completada"])

    def test_agregar_tarea_categoria_vacia(self):
        tareas = []
        with self.assertRaises(ValueError):
            agregar_tarea(tareas, "Leer documentación", "   ")

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "Estudio")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])

    def test_pendientes_filtra_por_categoria_sin_mayusculas(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "Estudio")
        agregar_tarea(tareas, "Revisar correo", "Trabajo")
        agregar_tarea(tareas, "Leer", "ESTUDIO")

        resultado = pendientes(tareas, "eStuDio")
        self.assertEqual(len(resultado), 2)

    def test_pendientes_categoria_inexistente_devuelve_vacio(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "Estudio")
        agregar_tarea(tareas, "Revisar correo", "Trabajo")

        resultado = pendientes(tareas, "Salud")
        self.assertEqual(resultado, [])

    def test_editar_tarea_actualiza_titulo_y_categoria(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "Estudio")

        tarea = editar_tarea(tareas, 1, "Practicar Python", "Trabajo")

        self.assertEqual(tarea["titulo"], "Practicar Python")
        self.assertEqual(tarea["categoria"], "Trabajo")

    def test_editar_tarea_id_inexistente(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "Estudio")

        with self.assertRaises(ValueError):
            editar_tarea(tareas, 99, "Practicar Python", "Trabajo")

    def test_editar_tarea_titulo_o_categoria_vacios(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "Estudio")

        with self.assertRaises(ValueError):
            editar_tarea(tareas, 1, "   ", "Trabajo")
        with self.assertRaises(ValueError):
            editar_tarea(tareas, 1, "Practicar Python", "   ")

    def test_eliminar_tarea_por_id(self):
        tareas = []
        agregar_tarea(tareas, "Tarea 1", "Estudio")
        agregar_tarea(tareas, "Tarea 2", "Trabajo")
        agregar_tarea(tareas, "Tarea 3", "Salud")

        tarea_eliminada = eliminar_tarea(tareas, 2)

        self.assertEqual(tarea_eliminada["id"], 2)
        self.assertEqual([t["id"] for t in tareas], [1, 3])

    def test_eliminar_tarea_id_inexistente(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "Estudio")

        with self.assertRaises(ValueError):
            eliminar_tarea(tareas, 99)


if __name__ == "__main__":
    unittest.main()
