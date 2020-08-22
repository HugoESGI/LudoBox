from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('<int:id_article>', views.view_article)
]
