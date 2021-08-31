from django.http import  HttpResponse
from django.shortcuts import render

from .models import Market


def index(request):
   market = Market.objects.all()
   return render(request, 'market/index.html', {'market': market})


