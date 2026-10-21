from django.urls import path

from . import views

urlpatterns = [
    path("", views.CarroListView.as_view(), name="lista"),
    path("carro/<int:pk>/", views.CarroDetailView.as_view(), name="detalhe"),
    path("contato/", views.contato, name="contato"),
]
