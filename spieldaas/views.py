from django.shortcuts import render
from django.http import HttpResponse
from spieldaas.models import Game, News

# Create your views here.
def mainPage(request):
    return render(request, 'index.html')

def news(request):
    newsData = News.objects.all()
    data = {
        'newsData': newsData
    }
    return render(request, 'news.html', data)

def store(request):
    gamesData = Game.objects.all()
    data = {
        'gamesData': gamesData
    }
    return render(request, 'store.html', data)

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')