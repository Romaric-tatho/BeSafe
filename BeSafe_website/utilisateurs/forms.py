from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.password_validation import (
#     MinimumLengthValidator,
#     CommonPasswordValidator,
#     NumericPasswordValidator,
#     UserAttributeSimilarityValidator
# )
from django.core.exceptions import ValidationError
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture']
        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirmer le mot de passe'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['user_type'].widget.attrs['readonly'] = True  # Rendre le type d'utilisateur non modifiable
        
        # Personnaliser les messages d'erreur pour les champs
        self.fields['username'].error_messages = {
            'required': "Le nom d'utilisateur est requis.",
            'max_length': "Le nom d'utilisateur ne peut pas dépasser 150 caractères.",
            'unique': "Ce nom d'utilisateur est déjà pris."
        }
        self.fields['email'].error_messages = {
            'required': "L'adresse email est requise.",
            'invalid': "Veuillez entrer une adresse email valide.",
            'unique': "Cette adresse email est déjà utilisée."
        }
        self.fields['password1'].error_messages = {
            'required': "Le mot de passe est requis."
        }
        self.fields['password2'].error_messages = {
            'required': "La confirmation du mot de passe est requise."
        }
        self.fields['profile_picture'].error_messages = {
            'invalid': "Veuillez sélectionner une image valide."
        }
        # self.fields['user_type'].error_messages = {
        #     'required': "Le type d'utilisateur est requis."
        # }

        # Utiliser les validateurs intégrés pour le mot de passe
        # self.fields['password1'].validators = [
        #     MinimumLengthValidator(min_length=8),
        #     CommonPasswordValidator(),
        #     NumericPasswordValidator(),
        #     UserAttributeSimilarityValidator()
        # ]

    def clean_password2(self):
        """Vérifier que password1 et password2 correspondent."""
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Les mots de passe ne correspondent pas.")
        return password2