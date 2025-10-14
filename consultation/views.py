from django.shortcuts import render
from bibliothecaire.models import Livre, Dvd, Cd, JeuDePlateau

def accueil_consul(request):
    return render(request, 'consul.html')


"""
3/ Afficher la liste
Pour les clients
"""

def liste_medias_public(request):
    livres = Livre.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()
    jeux = JeuDePlateau.objects.all()

    context = {
        'livres': livres,
        'dvds': dvds,
        'cds': cds,
        'jeux': jeux
    }
    return render(request, 'medias_public.html', context)