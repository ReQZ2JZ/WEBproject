from django.urls import path
from . import views

app_name = 'game_builds'

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('game/<slug:slug>/', views.game_detail, name='game_detail'),
    path('game/<slug:slug>/generate/', views.generate_random_build, name='generate_build'),
    path('register-admin/', views.register_admin, name='register_admin'),
    path('activate-admin/<uuid:code>/', views.activate_admin_invite, name='activate_admin'),
    path('register/', views.register, name='register'),
] 