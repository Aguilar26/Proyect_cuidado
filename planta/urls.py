from django.urls import path
from . import views

urlpatterns = [
    path('', views.sugerencia_form, name='sugerencia_form'),
    path('<int:plant_id>/', views.sugerencia_resultados, name='sugerencia_resultados'),
]
