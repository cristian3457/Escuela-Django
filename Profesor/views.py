from Materia.models import Unidad
from django.shortcuts import render
from .models import Profesor
from django.db import connection
# Create your views here.
def profesor(request):
    id = request.user.id
    usuario = Profesor.objects.get(usuario_id=id)
    return render(request,'profesor.html',{'usuario':usuario})
def carga_profesor(request):
    id = request.user.id
    profesor = Profesor.objects.get(usuario_id=id)
    cursor = connection.cursor()
    carga_profesor = cursor.execute('xp_consultar_materias_profesor %s', [profesor.id])
    longitud = cursor.rowcount
    return render(request,'carga_profesor.html',{'usuario':profesor,'carga_profesor':carga_profesor,'longitud':longitud})

def info_docente(request):
    id = request.user.id
    profesor = Profesor.objects.get(usuario_id=id)
    return render(request,'info_docente.html',{'usuario':profesor})

def alumnos_materia(request):
    id = request.user.id
    profesor = Profesor.objects.get(usuario_id=id)
    cursor = connection.cursor()
    carga_profesor = cursor.execute('xp_consultar_materias_profesor %s', [profesor.id])
    longitud = cursor.rowcount
    cursor = connection.cursor()
    # alumnos_materia = cursor.execute('xp_consultar_alumnos_materia %s,%s', [profesor.id,28])
    # longitud_alumnos = cursor.rowcount , 'alumnos_materia':alumnos_materia,'longitud_alumnos':longitud_alumnos
    return render(request,'alumnos_materia.html',{'usuario':profesor,'carga_profesor':carga_profesor,
                    'longitud':longitud})

def alumnos_materia_id(request, id_materia):
    id_materia = id_materia
    id = request.user.id
    profesor = Profesor.objects.get(usuario_id=id)
    cursor = connection.cursor()
    carga_profesor = cursor.execute('xp_consultar_materias_profesor %s', [profesor.id])
    longitud = cursor.rowcount
    cursor = connection.cursor()
    alumnos_materia = cursor.execute('xp_consultar_alumnos_materia %s,%s', [profesor.id,id_materia])
    longitud_alumnos = cursor.rowcount
    return render(request,'alumnos_materia.html',{'usuario':profesor,'carga_profesor':carga_profesor,
                    'longitud':longitud, 'alumnos_materia':alumnos_materia,'longitud_alumnos':longitud_alumnos,'id_materia':id_materia})
    
def subir_calificaciones(request):
    id = request.user.id
    profesor = Profesor.objects.get(usuario_id=id)
    cursor = connection.cursor()
    carga_profesor = cursor.execute('xp_consultar_materias_profesor %s', [profesor.id])
    longitud = cursor.rowcount
    return render(request,'subir_calificaciones.html',{'usuario':profesor,'carga_profesor':carga_profesor,
                    'longitud':longitud})

def subir_calificaciones_id(request, id_materia):
    id_materia = id_materia
    id = request.user.id
    profesor = Profesor.objects.get(usuario_id=id)
    cursor = connection.cursor()
    carga_profesor = cursor.execute('xp_consultar_materias_profesor %s', [profesor.id])
    longitud = cursor.rowcount
    cursor = connection.cursor()
    alumnos_materia = cursor.execute('xp_consultar_alumnos_materia %s,%s', [profesor.id,id_materia])
    longitud_alumnos = cursor.rowcount
    unidades = Unidad.objects.filter(materia_id = id_materia)

    if request.method == "POST":
            calificaciones = request.POST.getlist('calificacion[]')
            unidadesCalif = request.POST.getlist('unidad[]')
            alumnos = request.POST.getlist('alumno[]')
            iteracion = 0
            for calificacion in calificaciones:
                if calificacion:
                    cursor = connection.cursor()
                    cursor.execute('xp_subir_calificaciones %s,%s,%s', [calificacion,alumnos[iteracion],unidadesCalif[iteracion]])
                iteracion+=1
            return render(request,'subir_calificaciones.html',{'usuario':profesor,'carga_profesor':carga_profesor,'unidades':unidades,'unidadesCalif':unidadesCalif,'alumnos':alumnos[0],
                    'longitud':longitud, 'alumnos_materia':alumnos_materia,'longitud_alumnos':longitud_alumnos,'id_materia':id_materia,'calificaciones':calificaciones,'iteracion':iteracion})

    return render(request,'subir_calificaciones.html',{'usuario':profesor,'carga_profesor':carga_profesor,'unidades':unidades,
                    'longitud':longitud, 'alumnos_materia':alumnos_materia,'longitud_alumnos':longitud_alumnos,'id_materia':id_materia})


def subir(request, id_materia):
    id_materia = id_materia
    id = request.user.id
    profesor = Profesor.objects.get(usuario_id=id)
    cursor = connection.cursor()
    carga_profesor = cursor.execute('xp_consultar_materias_profesor %s', [profesor.id])
    longitud = cursor.rowcount
    cursor = connection.cursor()
    alumnos_materia = cursor.execute('xp_consultar_alumnos_materia %s,%s', [profesor.id,id_materia])
    longitud_alumnos = cursor.rowcount
    cursor = connection.cursor()
    calif_materia = cursor.execute('consultar_calif_materia_profesor %s,%s', [id_materia, profesor.id])
    longitud_calif_materia = cursor.rowcount

    unidades = Unidad.objects.filter(materia_id = id_materia)

    if request.method == "POST":
            calificaciones = request.POST.getlist('calificacion[]')
            unidadesCalif = request.POST.getlist('unidad[]')
            alumnos = request.POST.getlist('alumno[]')
            iteracion = 0
            for calificacion in calificaciones:
                if calificacion:
                    cursor = connection.cursor()
                    cursor.execute('xp_subir_calificaciones %s,%s,%s', [calificacion,alumnos[iteracion],unidadesCalif[iteracion]])
                iteracion+=1
            return render(request,'subir.html',{'usuario':profesor,'carga_profesor':carga_profesor,'unidades':unidades,'unidadesCalif':unidadesCalif,'alumnos':alumnos[0],
                    'longitud':longitud, 'alumnos_materia':alumnos_materia,'longitud_alumnos':longitud_alumnos,'id_materia':id_materia,'calificaciones':calificaciones,'iteracion':iteracion})

    return render(request,'subir.html',{'usuario':profesor,'carga_profesor':carga_profesor,'unidades':unidades,'calif_materia':calif_materia,
                    'longitud':longitud, 'alumnos_materia':alumnos_materia,'longitud_alumnos':longitud_alumnos,'id_materia':id_materia})