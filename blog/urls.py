from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('addition/<int:n1>/<int:n2>', views.addition)
]
