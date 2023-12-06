from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from web.back4app import login_api, obtener_datos_api

usuario: str = ""


# Create your views here.
def login(request):
    user: str = ""
    if request.method == 'POST':
        usuarioF = request.POST.get('username')
        codigo = request.POST.get('password')
        usuario = usuarioF
        user = login_api(usuario=usuario, codigo=codigo)
        if user == usuario:
            return HttpResponseRedirect('/dashboard/')
            # return render(request, 'dashboard.html', {'usuario': usuario})
        else:
            messages.add_message(request, messages.ERROR, 'Usuario o clave invalido')
            # return render(request, 'login.html')

    return render(request, 'login.html', {'message': user})


def dashboard(request):
    # usuario = request.POST.get('usuario')
    datos = obtener_datos_api("52153517")

    return render(request, 'dashboard.html', {'data': datos})


def contenido_datos(request):
    nombre = request.POST.get('nombre')
    contenido = request.POST.get('contenido')
    id = request.POST.get('id')
    categoria = request.POST.get('categoria')
    celdas = request.POST.get('id_datos')
    extra1 = request.POST.get('extra1')
    extra2 = request.POST.get('extra2')
    extra3 = request.POST.get('extra3')
    descripcion = request.POST.get('descripcion')

    return render(request, 'contenido.html',
                  {'nombre': nombre,
                   'contenido': contenido,
                   'id': id,
                   'categoria': categoria,
                   'celdas': celdas,
                   'extra1': extra1,
                   'extra2': extra2,
                   'extra3': extra3,
                   'descripcion': descripcion
                   })
