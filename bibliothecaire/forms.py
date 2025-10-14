from django import forms
from .models import Membre, Livre, Dvd, Cd

"""
Formulaire 1

Ajout d'un membre
+ bloque oui/non
"""

class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ['nom', 'bloque']


"""
Formulaire 2
Ajout d'un media

3 formulaires car 3 médias
"""

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'auteur']

class DvdForm(forms.ModelForm):
    class Meta:
        model = Dvd
        fields = ['titre', 'realisateur']

class CdForm(forms.ModelForm):
    class Meta:
        model = Cd
        fields = ['titre', 'artiste']


"""
Formulaire 3
Créer un emprunt

3 class car 3 médias différents
(choisir le membre + medias)
"""

class EmpruntLivreForm(forms.Form):
    membre = forms.ModelChoiceField(
        queryset=Membre.objects.filter(bloque=False),
        empty_label="Choisir un membre"
    )
    livre = forms.ModelChoiceField(
        queryset=Livre.objects.filter(disponible=True),
        empty_label="Choisir un livre disponible"
    )

class EmpruntDvdForm(forms.Form):
    membre = forms.ModelChoiceField(
        queryset=Membre.objects.filter(bloque=False),
        empty_label="Choisir un membre"
    )
    dvd = forms.ModelChoiceField(
        queryset=Dvd.objects.filter(disponible=True),
        empty_label="Choisir un DVD disponible"
    )

class EmpruntCdForm(forms.Form):
    membre = forms.ModelChoiceField(
        queryset=Membre.objects.filter(bloque=False),
        empty_label="Choisir un membre"
    )
    cd = forms.ModelChoiceField(
        queryset=Cd.objects.filter(disponible=True),
        empty_label="Choisir un CD disponible"
    )
