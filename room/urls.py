from django.urls import path

from . import views

app_name = 'room'
urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('login', views.login_user, name='login'),
    path('question_updated', views.update_question, name='update_question'),
    path('<int:question_id>/answer_updated', views.update_answer, name='update_answer'),
]