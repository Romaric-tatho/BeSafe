from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

def user_directory_path(instance, filename):
    """Génère un chemin unique pour les images de profil des utilisateurs."""
    ext = filename.split('.')[-1]
    return f'profile_pics/user_{instance.username}/{uuid.uuid4()}.{ext}'

class CustomUser(AbstractUser):
    # Champ pour la photo de profil
    profile_picture = models.ImageField(
        upload_to=user_directory_path,  # Utilisation de la fonction personnalisée
        blank=True,
        null=True,
        verbose_name="Photo de profil"
    )
    
    # Champ pour le type d'utilisateur
    user_type = models.CharField(
        max_length=50,
        choices=[
            ('simple', 'Utilisateur Simple'),
            ('teacher', 'Enseignant')
        ],
        default='simple',
        verbose_name="Type d'utilisateur"
    )

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        return self.username