from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def display(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis

    :param request:
    :return: HttpResponse
    """
    date = datetime.now()

    return render(request, "../templates/base.html", locals())
