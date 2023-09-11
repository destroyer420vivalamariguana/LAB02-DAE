from django.urls import path
from . import views

app_name = 'encuesta'

urlpatterns = [
    # ex: /encuesta/
    path('', views.index, name = 'index'),
    path('enviar', views.enviar, name = 'enviar'),
    path('calculo/', views.calculo, name='calculo'),
    path('calculo/resultado/', views.calculo_resultado, name='calculo_resultado'),
    path('cilindro/', views.cilindro, name='cilindro'),
    path('cilindro/resultado/', views.cilindro_resultado, name='cilindro_resultado'),
]
