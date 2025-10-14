from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil_biblio, name='accueil_biblio'),
    path('medias/', views.liste_medias, name='liste_medias'),
    path('membres/', views.liste_membres, name='liste_membres'),
    path('creer-membre/', views.creer_membre, name='creer_membre'),
    path('ajouter-livre/', views.ajouter_livre, name='ajouter_livre'),
    path('ajouter-dvd/', views.ajouter_dvd, name='ajouter_dvd'),
    path('ajouter-cd/', views.ajouter_cd, name='ajouter_cd'),
    path('modifier-membre/<int:membre_id>/', views.modifier_membre, name='modifier_membre'),
    path('supprimer-membre/<int:membre_id>/', views.supprimer_membre, name='supprimer_membre'),
    path('creer-emprunt/', views.creer_emprunt, name='creer_emprunt'),
    path('rentrer-emprunts/', views.rentrer_emprunts, name='rentrer_emprunts'),
]