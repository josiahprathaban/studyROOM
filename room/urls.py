from django.urls import path

from . import views

app_name = 'room'
urlpatterns = [
    path('', views.index, name='index'),
    path('updated', views.update_question, name='update'),
]