from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

def home(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("""
        <h1>Articles</h1>
        <p>Select an article</p>
    """)

def view_article(request, id_article: int):
    """

    :param request:
    :param id_article:
    :return:
    """
    if id_article < 100:
        return redirect("../article")

    return HttpResponse(f"""
        <h1>Article #{id_article}</h1>
    """)
