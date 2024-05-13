#Lista wszystkich URL, jakie są obsługiwane w aplikacji
from django.urls import path    #funkcja przyjmuje dwa argumenty: string - URL oraz wskaźnik na funkcje view, która powinna być wywołana
from . import views     #z tego samego folderu, gdzie jestem, użyj pliku views

urlpatterns = [
    path("january", views.index)      #całe to wyrażenie tworzy tzw. URLconfig (URLConf)
]

#mam URL, które są obśługiwane przez aplikację challenges w całym projekcie monthly_challenges.
#trzeba teraz połączyć aplikacje challenge z całym projektem
#Należy stworzyć URLconfig projektu, oprócz tego URLConfigu, który jest tutaj w tyej aplikacji