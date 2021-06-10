from django.shortcuts import redirect, render
from Alumno.models import Alumno,Carga_academica_alumno, Detalle_carga_alumno
from django.db import connection
# Create your views here.

def alumno(request):
    id = request.user.id
    usuario = Alumno.objects.get(usuario_id=id)
    cursor = connection.cursor()
    detalle_carga = cursor.execute('xp_consultar_carga_academica_alumno %s', [usuario.id])
    return render(request,'carga_academica.html',{'usuario':usuario,'detalle_carga':detalle_carga})

def carga_academica(request):
    id = request.user.id
    usuario = Alumno.objects.get(usuario_id=id)
    cursor = connection.cursor()
    detalle_carga = cursor.execute('xp_consultar_carga_academica_alumno %s', [usuario.id])
    longitud = cursor.rowcount
    return render(request,'carga_academica.html',{'usuario':usuario,'detalle_carga':detalle_carga,'longitud':longitud})

def info_alumno(request):
    id = request.user.id
    usuario = Alumno.objects.get(usuario_id=id)
    return render(request,'info_alumno.html',{'usuario':usuario})

def monitoreo_grupos(request):
    id = request.user.id
    alumno = Alumno.objects.get(usuario_id=id)
    cursor = connection.cursor()
    cursor.execute('xp_consultar_carga_academica_alumno %s', [alumno.id])
    longitud_detalle_carga = cursor.rowcount
    monitoreo_materias = cursor.execute('xp_consultar_materias_semestre %s,%s', [alumno.semestre, alumno.carrera_id])
    longitud = cursor.rowcount
    return render(request,'monitoreo_grupos.html',{'materias':monitoreo_materias,'longitud':longitud,'usuario':alumno,'longitud_detalle_carga':longitud_detalle_carga})

def inscripcion(request):
    id = request.user.id
    alumno = Alumno.objects.get(usuario_id=id)
    cursor = connection.cursor()
    cursor.execute('xp_consultar_carga_academica_alumno %s', [alumno.id])
    longitud_detalle_carga = cursor.rowcount
    if request.method == "POST":
        ids = request.POST.getlist('ids[]')
        cursor.execute('xp_insertar_carga_academica %s', [alumno.id])
        carga_academica = Carga_academica_alumno.objects.last()
        for id in ids:
            cursor.execute('xp_insertar_detalle_carga_academica %s,%s', [id, carga_academica.id])
        return redirect('/cargaAcademica/')
    monitoreo_materias = cursor.execute('xp_consultar_materias_semestre %s,%s', [alumno.semestre, alumno.carrera_id])
    longitud = cursor.rowcount
    return render(request,'inscripcion.html',{'materias':monitoreo_materias,'longitud':longitud,'usuario':alumno,'longitud_detalle_carga':longitud_detalle_carga})

def calificaciones_alumno(request):
    id = request.user.id
    alumno = Alumno.objects.get(usuario_id=id)
    cursor = connection.cursor()
    mat = cursor.execute('xp_materias_alumno_calif %s', [alumno.id])
    cursor = connection.cursor()
    cal = cursor.execute('xp_consultar_calif_alumno %s', [alumno.id])
    max_unidad = 0
    longitud = 0
    calificaciones = []
    materias = []
    for materia in mat:
        materias.append([materia.id, materia.materia])
        if max_unidad == 0:
            max_unidad = materia.max_unidad
            unidad = range(1,int(max_unidad+1))
    for calificacion in cal:
        longitud+=1
        calificaciones.append(calificacion)
    agrego = False
    id_materia = 0
    contador = 0
    for calificacion in calificaciones:
        contador+=1
        if agrego == False:
            indice = materias.index([calificacion[0],calificacion[1]])
            temp = materias[indice]
            temp.append(calificacion[2])
            materias[indice]=temp
            agrego = True;
            id_materia = calificacion[0]
        else:
            if id_materia == calificacion[0]:
                indice = materias.index(temp)
                temp = materias[indice]
                temp.append(calificacion[2])
                materias[indice]=temp
                indice_anterior = indice
            else:
                if longitud == contador:
                    indice = materias.index([calificacion[0],calificacion[1]])
                    temp = materias[indice]
                    temp.append(calificacion[2])
                    materias[indice]=temp
                    id_materia = calificacion[0]
                    agrego = False
                else:
                    indice = materias.index([calificacion[0],calificacion[1]])
                    temp = materias[indice]
                    temp.append(calificacion[2])
                    materias[indice]=temp
                    agrego = True;
                    id_materia = calificacion[0]
    for materia in materias:
        materia.pop(0)
    return render(request,'alumno_calificaciones.html',{'usuario':alumno,'unidad':unidad,'calificaciones':materias,'cal':calificaciones})