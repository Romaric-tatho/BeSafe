from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Route pour la page d'accueil
    path('register/', views.register, name='register'),  # URL pour l'inscription
    path('login/', views.login_view, name='login'),      # URL pour la connexion
    path('logout/', views.logout_view, name='logout'),   # URL pour la déconnexion
    path('profile/', views.user_profile, name='profile'),  # URL pour le profil utilisateur
]