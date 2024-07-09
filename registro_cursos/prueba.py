from gestion.services import *

crear_estudiante('12345678A', 'Juan', 'Perez', '2000-05-01', 'Admin')
crear_estudiante('23456789B', 'Ana', 'Lopez', '2001-06-02', 'Admin')

crear_direccion('Calle Falsa', '123', 'A', 'Comuna 1', 'Ciudad 1', 'Region 1', '12345678A')
crear_direccion('Avenida Siempre Viva', '742', None, 'Comuna 2', 'Ciudad 2', 'Region 2', '23456789B')

crear_profesor('34567890C', 'Luis', 'Garcia', 'Admin')
crear_profesor('45678901D', 'Maria', 'Fernandez', 'Admin')

crear_curso('MAT101', 'Matemáticas', 1)
crear_curso('HIS202', 'Historia', 1)

agregar_profesor_a_curso('MAT101', '34567890C')
agregar_profesor_a_curso('HIS202', '45678901D')

agregar_cursos_a_estudiante('12345678A', ['MAT101', 'HIS202'])
agregar_cursos_a_estudiante('23456789B', ['MAT101'])

imprime_estudiante_cursos('12345678A')
imprime_estudiante_cursos('23456789B')
