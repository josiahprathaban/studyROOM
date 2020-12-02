from django.urls import path

from . import views

app_name = 'room'
urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('question', views.your_question, name='question'),
    path('answers', views.your_answer, name='answer'),
    path('login', views.login_user, name='login'),
    path('question_updated', views.update_question, name='update_question'),
    path('<int:question_id>/answer_updated', views.update_answer, name='update_answer'),
    path('<int:answer_id>/answer_liked', views.like, name='like'),
]
