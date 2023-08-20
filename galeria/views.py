from django.shortcuts import render

def index(request):

    dados = {
        1: {"nome": "Nebulosa de carina",
            "legenda": "webbtelescope.org / NASA / James Webb"},
        2: {"nome": "Galaxia mgc1079",
            "legenda": "NASA.org / NASA / Huble"}
    }

    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')


#