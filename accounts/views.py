from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def login(request):
    if request.method == 'POST':

        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Helytelen felhasználónév vagy jelszó!")
            return redirect('login')

    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1 == password2:
            if first_name == "":
                messages.info(request, 'Nem adott meg Vezetéknevet!')
                return redirect('register')
            elif last_name == "":
                messages.info(request, 'Nem adott meg keresztnevet!')
                return redirect('register')
            elif username == "":
                messages.info(request, 'Nem adott meg felhasználónevet!')
                return redirect('register')
            elif email == "":
                messages.info(request, 'Nem adott meg emailcímet!')
                return redirect('register')
            elif password1 == "":
                messages.info(request, 'Nem adott meg jelszót!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'A felhasználónév foglalt!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Az email foglalt!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'A két jelszó nem egyezik!')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')