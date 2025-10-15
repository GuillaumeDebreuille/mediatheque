# mediatheque

### Étapes d'installation

1. Cloner le repository
```bash
git clone https://github.com/GuillaumeDebreuille/mediatheque.git
cd mediatheque
```

2. Créer et activer l'environnement virtuel
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. Installer les dépendances
```bash
pip install Django pytest pytest-django
```

4. Appliquer les migrations
```bash
python manage.py migrate
```

5. Créer un superutilisateur (optionnel)
```bash
python manage.py createsuperuser
```

6. Lancer le serveur de développement
```bash
python manage.py runserver
```