from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    context = {
        "nome_pagina": "VISITANTES",
    }


    return render(request, 'usuarios/index.html', context)



