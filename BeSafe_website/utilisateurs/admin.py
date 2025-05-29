
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    # Liste des champs à afficher dans l'interface d'administration
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type', 'is_active')
    list_filter = ('user_type', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

    # Configuration des champs visibles lors de l'ajout ou de la modification d'un utilisateur
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type', 'profile_picture')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type', 'profile_picture')}),
    )

# Enregistrer le modèle et l'administrateur personnalisé
admin.site.register(CustomUser, CustomUserAdmin)