import pytest
from django.test import Client


@pytest.mark.django_db
#Autorisation BDD

def test_creer_membre_protection():

    print("test 1")
    print("Page Créer-membre. Avec ou sans connexion")

    #Création du faux navigateur
    client = Client()

    #test connexion (non connecté)
    response = client.get('/bibliothecaire/creer-membre/')

    #Bonne réponse : Pas de conexion donc redirection accueil
    if response.url == '/':
        print("OK : (non connecté) redirection accueil")
    else:
        print("ERREUR : Mauvaise redirection")
        assert False

    #Ajout de la connexion
    session = client.session
    session['biblio_connected'] = True
    session.save()

    # test connexion (connecté)
    response = client.get('/bibliothecaire/creer-membre/')

    # Bonne réponse : Une conexion donc page demandée
    if not hasattr(response, 'url'):
        print("OK : (connecté) Page affichée ")
    else:
        print("ERREUR : Ne devrait pas rediriger")
        assert False