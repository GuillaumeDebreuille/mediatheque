
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='accueil'),
    path('bibliothecaire/', include('bibliothecaire.urls')),
    path('consultation/', include('consultation.urls')),
    path('login-biblio/', views.login_biblio, name='login_biblio'),
]
