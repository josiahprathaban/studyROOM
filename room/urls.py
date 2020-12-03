from django.urls import path

from . import views

app_name = 'room'
urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('question', views.your_question, name='question'),
    path('<int:question_id>/question_deleted', views.delete_question, name='delete_question'),
    path('<int:answer_id>/answer_deleted', views.delete_answer, name='delete_answer'),
    path('topquestion', views.top_questions, name='top_question'),
    path('latestquestion', views.latest_questions, name='latest_question'),
    path('answers', views.your_answer, name='answer'),
    path('login', views.login_user, name='login'),
    path('question_updated', views.update_question, name='update_question'),
    path('<int:question_id>/answer_updated', views.update_answer, name='update_answer'),
    path('<int:question_id>/question', views.to_question, name='to_question'),
    path('<int:answer_id>/to_edit', views.to_edit, name='to_edit'),
    path('<int:answer_id>/answer_edited', views.edit_answer, name='edit_answer'),
    path('<int:answer_id>/answer_liked', views.like, name='like'),
]
