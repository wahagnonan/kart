from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('nouveau/', views.nouveau, name='nouveau'),
    path('reponses/', views.reponses, name='reponses'),

    # Questions
    path('questions/', views.admin_questions, name='admin_questions'),
    path('questions/ajouter/', views.question_ajouter, name='question_ajouter'),
    path('questions/<int:pk>/modifier/', views.question_modifier, name='question_modifier'),
    path('questions/<int:pk>/toggle/', views.question_toggle, name='question_toggle'),
    path('questions/<int:pk>/supprimer/', views.question_supprimer, name='question_supprimer'),
    path('questions/<int:pk>/monter/', views.question_monter, name='question_monter'),
    path('questions/<int:pk>/descendre/', views.question_descendre, name='question_descendre'),

    # Export
    path('export/json/', views.export_json, name='export_json'),
    path('export/csv/', views.export_csv, name='export_csv'),
]
