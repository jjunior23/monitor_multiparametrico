from django.shortcuts import render, redirect
from .models import Parametro

# Create your views here.
def home(request):
    parametros = Parametro.objects.all()

    return render(request, "index.html", {"parametros":parametros})

def inserir(request):
    vnome = request.POST.get("nome")

    Parametro.objects.create(nome=vnome)
    parametros = Parametro.objects.all()
    return render(request, "index.html",{"parametros":parametros})

def editar(request,id):
    parametro = Parametro.objects.get(id=id)
    return render(request, "update.html", {"parametro":parametro})

def update(request, id):
    vvalor = request.POST.get("valor")
    parametro = Parametro.objects.get(id=id)
    parametro.valor = vvalor
    parametro.save()
    return redirect(home)

def editar(request,id):
    parametro = Parametro.objects.get(id=id)
    return render(request, "update.html", {"parametro":parametro})

def delete(request, id):
    parametro = Parametro.objects.get(id=id)
    parametro.delete()
    return redirect(home)

