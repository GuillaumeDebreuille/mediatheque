from django.contrib import admin
from .models import Media, Livre, Dvd, Cd, JeuDePlateau, Membre

admin.site.register(Media)
admin.site.register(Livre)
admin.site.register(Dvd)
admin.site.register(Cd)
admin.site.register(JeuDePlateau)
admin.site.register(Membre)
