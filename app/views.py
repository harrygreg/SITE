from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def disciplina(request):
    return render(request,"disciplina.html")

def detalhe_curso(request):
    return render(request,"detalhe_curso.html")

def lista_cursos(request):
    return render(request,"lista_cursos.html")

def noticias(request):
    return render(request,"noticias.html")