from .models import Direccion, Profesor, Estudiante, Curso, Inscripcion
from datetime import date

def crear_direccion(calle, numero, dpto, comuna, ciudad, region, estudiante_rut):
    estudiante = Estudiante.objects.get(rut=estudiante_rut)
    direccion = Direccion.objects.create(
        calle=calle, numero=numero, dpto=dpto, comuna=comuna,
        ciudad=ciudad, region=region, estudiante=estudiante
    )
    return direccion

def crear_profesor(rut, nombre, apellido, creado_por):
    profesor = Profesor.objects.create(
        rut=rut, nombre=nombre, apellido=apellido, creado_por=creado_por
    )
    return profesor

def crear_estudiante(rut, nombre, apellido, fecha_nac, creado_por):
    estudiante = Estudiante.objects.create(
        rut=rut, nombre=nombre, apellido=apellido,
        fecha_nac=fecha_nac, creado_por=creado_por
    )
    return estudiante

def crear_curso(codigo, nombre, version, profesor_rut=None):
    profesor = Profesor.objects.get(rut=profesor_rut) if profesor_rut else None
    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, version=version, profesor=profesor
    )
    return curso

def obtener_estudiante(rut):
    return Estudiante.objects.get(rut=rut)

def obtener_profesor(rut):
    return Profesor.objects.get(rut=rut)

def obtener_curso(codigo):
    return Curso.objects.get(codigo=codigo)

def agregar_profesor_a_curso(codigo_curso, rut_profesor):
    curso = Curso.objects.get(codigo=codigo_curso)
    profesor = Profesor.objects.get(rut=rut_profesor)
    curso.profesor = profesor
    curso.save()
    return curso

def agregar_cursos_a_estudiante(rut_estudiante, codigos_cursos):
    estudiante = Estudiante.objects.get(rut=rut_estudiante)
    for codigo in codigos_cursos:
        curso = Curso.objects.get(codigo=codigo)
        Inscripcion.objects.create(estudiante=estudiante, curso=curso)
    return estudiante

def imprime_estudiante_cursos(rut_estudiante):
    estudiante = Estudiante.objects.get(rut=rut_estudiante)
    inscripciones = Inscripcion.objects.filter(estudiante=estudiante)
    for inscripcion in inscripciones:
        print(f"Estudiante: {estudiante.nombre} {estudiante.apellido} - Curso: {inscripcion.curso.nombre}")
