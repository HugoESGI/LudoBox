from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis

    :param request:
    :return: HttpResponse
    """
    return HttpResponse("""
        <h1>Titre test</h1>
        <p>Paragraphe test</p>
    """)


def addition(request, n1, n2) -> int:
    """

    :param request:
    :param n1:
    :param n2:
    :return:
    """
    result = n1 + n2

    return render(request, '../templates/blog/addition.html', locals())
