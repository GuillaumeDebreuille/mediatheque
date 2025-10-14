from django.shortcuts import render, redirect

def accueil(request):
    return render(request, 'accueil.html')


def login_biblio(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'biblio41':
            request.session['biblio_connected'] = True
            return redirect('/bibliothecaire/')
        else:
            return render(request, 'accueil.html', {'erreur': 'Identifiants incorrects'})

    return redirect('/')