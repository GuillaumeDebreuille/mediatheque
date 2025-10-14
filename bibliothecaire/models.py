from django.db import models



class Media(models.Model):
    titre = models.CharField(max_length=100)
    dateEmprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.CharField(max_length=100, blank=True)


class Livre(Media):
    auteur = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titre} - {self.auteur}"


class Dvd(Media):
    realisateur = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titre} - {self.realisateur}"


class Cd(Media):
    artiste = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titre} - {self.artiste}"


class JeuDePlateau(models.Model):
    titre = models.CharField(max_length=100)
    createur = models.CharField(max_length=100)

class Membre(models.Model):
    nom = models.CharField(max_length=100)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return self.nom