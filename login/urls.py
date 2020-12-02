from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('success', views.success, name='success'),
    path('logout', views.logout_user, name='logout'),
]
