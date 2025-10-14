
from .models import Livre, Dvd, Cd, JeuDePlateau, Membre
from django.shortcuts import render, redirect
from .forms import MembreForm, LivreForm, DvdForm, CdForm, EmpruntLivreForm, EmpruntDvdForm, EmpruntCdForm
from datetime import date, timedelta

def accueil_biblio(request):
    if not request.session.get('biblio_connected'):
        return redirect('/')
    return render(request, 'biblio.html')


"""
1/ Création de l'affichage
LISTE DES MEDIAS
"""


def liste_medias(request):
    if not request.session.get('biblio_connected'):
        return redirect('/')

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
    return render(request, 'liste_medias.html', context)


"""
2/ Création de l'affichage
LISTE DES MEMBRES
"""


def liste_membres(request):
    if not request.session.get('biblio_connected'):
        return redirect('/')

    membres = Membre.objects.all()
    context = {
        'membres': membres
    }
    return render(request, 'liste_membres.html', context)


"""
4/ Création d'un ajout
MEMBRE
NOM + BLOQUE?
"""


def creer_membre(request):
    if not request.session.get('biblio_connected'):
        return redirect('/')

    if request.method == 'POST':
        form = MembreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bibliothecaire/membres/')
    else:
        form = MembreForm()

    return render(request, 'creer_membre.html', {'form': form})


"""
5/ Création d'un ajout
LES 3 MEDIAS
"""


def ajouter_livre(request):
    if not request.session.get('biblio_connected'):
        return redirect('/')

    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bibliothecaire/medias/')
    else:
        form = LivreForm()

    return render(request, 'ajouter_livre.html', {'form': form})


def ajouter_dvd(request):
    if not request.session.get('biblio_connected'):
        return redirect('/')

    if request.method == 'POST':
        form = DvdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bibliothecaire/medias/')
    else:
        form = DvdForm()

    return render(request, 'ajouter_dvd.html', {'form': form})


def ajouter_cd(request):
    if not request.session.get('biblio_connected'):
        return redirect('/')

    if request.method == 'POST':
        form = CdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bibliothecaire/medias/')
    else:
        form = CdForm()

    return render(request, 'ajouter_cd.html', {'form': form})


"""
6/ Modifications
Modification ou suppression d'un utilisateur
"""


def modifier_membre(request, membre_id):
    if not request.session.get('biblio_connected'):
        return redirect('/')

    membre = Membre.objects.get(id=membre_id)
    if request.method == 'POST':
        form = MembreForm(request.POST, instance=membre)
        if form.is_valid():
            form.save()
            return redirect('/bibliothecaire/membres/')
    else:
        form = MembreForm(instance=membre)

    return render(request, 'modifier_membre.html', {'form': form, 'membre': membre})


def supprimer_membre(request, membre_id):
    if not request.session.get('biblio_connected'):
        return redirect('/')

    membre = Membre.objects.get(id=membre_id)
    if request.method == 'POST':
        membre.delete()
        return redirect('/bibliothecaire/membres/')

    return render(request, 'confirmer_suppression.html', {'membre': membre})


"""
7/ EMPRUNT
Créer un emprunt
"""

def creer_emprunt(request):
    if not request.session.get('biblio_connected'):
        return redirect('/')

    livre_form = EmpruntLivreForm()
    dvd_form = EmpruntDvdForm()
    cd_form = EmpruntCdForm()
    erreur = None  #Variable pour stocker les erreurs

    if request.method == 'POST':
        if 'emprunter_livre' in request.POST:
            livre_form = EmpruntLivreForm(request.POST)
            if livre_form.is_valid():
                membre = livre_form.cleaned_data['membre']
                livre = livre_form.cleaned_data['livre']

                if peut_emprunter(membre):  #Ajout méthode controle
                    livre.disponible = False
                    livre.emprunteur = membre.nom
                    livre.dateEmprunt = date.today()
                    livre.save()
                    return redirect('/bibliothecaire/medias/')
                else:
                    erreur = "Ce membre ne peut pas emprunter"  #Ajout mess erreur controle

        elif 'emprunter_dvd' in request.POST:
            dvd_form = EmpruntDvdForm(request.POST)
            if dvd_form.is_valid():
                membre = dvd_form.cleaned_data['membre']
                dvd = dvd_form.cleaned_data['dvd']

                if peut_emprunter(membre):  #Ajout méthode controle
                    dvd.disponible = False
                    dvd.emprunteur = membre.nom
                    dvd.dateEmprunt = date.today()
                    dvd.save()
                    return redirect('/bibliothecaire/medias/')
                else:
                    erreur = "Ce membre ne peut pas emprunter"  #Ajout mess erreur controle

        elif 'emprunter_cd' in request.POST:
            cd_form = EmpruntCdForm(request.POST)
            if cd_form.is_valid():
                membre = cd_form.cleaned_data['membre']
                cd = cd_form.cleaned_data['cd']

                if peut_emprunter(membre):  #Ajout méthode controle
                    cd.disponible = False
                    cd.emprunteur = membre.nom
                    cd.dateEmprunt = date.today()
                    cd.save()
                    return redirect('/bibliothecaire/medias/')
                else:
                    erreur = "Ce membre ne peut pas emprunter"  #Ajout mess erreur controle

    context = {
        'livre_form': livre_form,
        'dvd_form': dvd_form,
        'cd_form': cd_form,
        'erreur': erreur
    }
    return render(request, 'creer_emprunt.html', context)


"""
8/ RENDRE

Une vue qui filtre les médias empruntés

+ Les 3 vues pour rendre les 3 médias 
"""


def rentrer_emprunts(request):
    if not request.session.get('biblio_connected'):
        return redirect('/')

    # Traitement des retours
    if request.method == 'POST':
        if 'rendre_livre' in request.POST:
            livre_id = request.POST.get('livre_id')
            livre = Livre.objects.get(id=livre_id)
            livre.disponible = True
            livre.emprunteur = ""
            livre.dateEmprunt = None
            livre.save()

        elif 'rendre_dvd' in request.POST:
            dvd_id = request.POST.get('dvd_id')
            dvd = Dvd.objects.get(id=dvd_id)
            dvd.disponible = True
            dvd.emprunteur = ""
            dvd.dateEmprunt = None
            dvd.save()

        elif 'rendre_cd' in request.POST:
            cd_id = request.POST.get('cd_id')
            cd = Cd.objects.get(id=cd_id)
            cd.disponible = True
            cd.emprunteur = ""
            cd.dateEmprunt = None
            cd.save()

        return redirect('/bibliothecaire/rentrer-emprunts/')

    """
    Affichage des médias empruntés
    """

    livres_empruntes = Livre.objects.filter(disponible=False)
    dvds_empruntes = Dvd.objects.filter(disponible=False)
    cds_empruntes = Cd.objects.filter(disponible=False)

    context = {
        'livres': livres_empruntes,
        'dvds': dvds_empruntes,
        'cds': cds_empruntes
    }
    return render(request, 'rentrer_emprunts.html', context)



"""
---------------------------------------------------------------------------
---------------------------------------------------------------------------
---------------------------------------------------------------------------
9/ LES REGLES
---------------------------------------------------------------------------
---------------------------------------------------------------------------
---------------------------------------------------------------------------
"""


def peut_emprunter(membre):



#Compter les emprunts actuels

    emprunts_actuels = (
            Livre.objects.filter(emprunteur=membre.nom, disponible=False).count() +
            Dvd.objects.filter(emprunteur=membre.nom, disponible=False).count() +
            Cd.objects.filter(emprunteur=membre.nom, disponible=False).count()
    )


#Règle 1: Max 3 emprunts

    if emprunts_actuels >= 3:
        return False


#Règle 2: Vérifier les retards (plus de 7 jours)

    limite_retour = date.today() - timedelta(days=7)

    retards_livres = Livre.objects.filter(emprunteur=membre.nom, disponible=False, dateEmprunt__lt=limite_retour).exists()
    retards_dvds = Dvd.objects.filter(emprunteur=membre.nom, disponible=False, dateEmprunt__lt=limite_retour).exists()
    retards_cds = Cd.objects.filter(emprunteur=membre.nom, disponible=False, dateEmprunt__lt=limite_retour).exists()

    if retards_livres or retards_dvds or retards_cds:
        return False


#Si tout est bon, fonction peut_emprunter = ok

    return True