from django.shortcuts import render
from django.http import HttpResponse #wbudowana klasa

# Create your views here.

#Pierwszy widok, na request do serwera, zwracam stringa. Póki co nie robię nic z requestem
def index(request):
    return HttpResponse("This works!")

#kiedy mamy to wywołać? Musimy to zdefininiować w urls.py, który stworzyłem. Mamy też folder urls.py w katalogu głównym projektu "monthly challenges", ale musimy mieć zdefiniowany URL w pliku urls.py w katalogu aplikacji, jaką tworzę













