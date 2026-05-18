from django.contrib import admin
from .models import Question, Artisan, Reponse

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'ordre', 'texte', 'active']
    list_display_links = ['id']
    list_editable = ['ordre', 'active']

@admin.register(Artisan)
class ArtisanAdmin(admin.ModelAdmin):
    list_display = ['id', 'contact', 'ville', 'metier', 'created_at']

@admin.register(Reponse)
class ReponseAdmin(admin.ModelAdmin):
    list_display = ['artisan', 'question', 'contenu']
