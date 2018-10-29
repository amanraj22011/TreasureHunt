from django.shortcuts import render, redirect
from .models import TreasureGram
from. forms import TreasureForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm



def Home(request):
    all_treasures = TreasureGram.objects.all()
    return render(request,'Treasures/home.html',{'all_treasures':all_treasures})


def detail(request, val):
    treasure = TreasureGram.objects.get (id=val)
    return render(request, 'Treasures/detail.html', {'treasure':treasure})


def add_new(request):
    if request.method =='POST':
        form =TreasureForm(request.POST)
        if form.is_valid():
            treasure = form.save()
            treasure.save()
            return redirect('/')
    else:
        form = TreasureForm()
        return render(request, "Treasures/new_treasures.html", {'form':form})


def treasure_edit(request,val):
    treasure = get_object_or_404(TreasureGram , pk=val)
    if request.method =='POST':
        form = TreasureForm(request.POST , instance=treasure)
        if form.is_valid():
            treasure =  form.save()
            treasure.save()
            return redirect('Treasures:detail', val = treasure.pk)
    else:
        form = TreasureForm(instance=treasure)
    return render(request, 'Treasures/new_treasures.html',{'form':form})



def LoginForm(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_pasword = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_pasword)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render (request, 'Treasures/login.html', {'form':form})


def LogoutForm(request):
    logout(request)
    return redirect('/')


