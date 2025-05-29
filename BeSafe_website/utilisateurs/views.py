from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser
from .forms import CustomUserCreationForm

def home(request):
    """Vue pour la page d'accueil."""
    return render(request, 'utilisateurs/home.html')

def register(request):
    """Vue pour l'inscription d'un nouvel utilisateur."""
    if request.user.is_authenticated:
        messages.info(request, "Vous êtes déjà connecté.")
        return redirect('home')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Bienvenue, {user.username} ! Votre compte a été créé avec succès.")
            return redirect('home')
        else:
            messages.error(request, "Erreur lors de l'inscription. Veuillez vérifier les informations saisies.")
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'utilisateurs/register.html', {'form': form})

def login_view(request):
    """Vue pour la connexion d'un utilisateur."""
    if request.user.is_authenticated:
        messages.info(request, "Vous êtes déjà connecté.")
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Connexion réussie, bienvenue {user.username} !")
            return redirect('home')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            return render(request, 'utilisateurs/login.html', {'username': username})
    return render(request, 'utilisateurs/login.html')

@login_required
def logout_view(request):
    """Vue pour la déconnexion d'un utilisateur."""
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('home')

@login_required
def user_profile(request):
    """Vue pour afficher le profil de l'utilisateur connecté."""
    return render(request, 'utilisateurs/profile.html', {'user': request.user})