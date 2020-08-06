from django.shortcuts import render
import random

# Create your views here.


def Home(request):
    return render(request, "Password_Generator/index.html")


def about(request):
    return render(request, "Password_Generator/about.html")


def pas(request):
    Characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        Characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('number'):
        Characters.extend(list('1234567890'))

    if request.GET.get('special'):
        Characters.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length', 12))
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(Characters)

    password = {'password': thepassword}

    return render(request, "Password_Generator/password.html", password)
