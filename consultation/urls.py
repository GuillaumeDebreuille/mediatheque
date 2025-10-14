from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil_consul, name='accueil_consul'),
    path('medias/', views.liste_medias_public, name='liste_medias_public'),
]