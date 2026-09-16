from django.urls import path
from agendamento import views

app_name = 'agendamento'

urlpatterns = [
    path('', views.index, name='index'),
]