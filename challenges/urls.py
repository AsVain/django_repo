#Lista wszystkich URL, jakie są obsługiwane w aplikacji
from django.urls import path    #funkcja przyjmuje dwa argumenty: string - URL oraz wskaźnik na funkcje view, która powinna być wywołana
from . import views     #z tego samego folderu, gdzie jestem, użyj pliku views

urlpatterns = [
    #path("january", views.january),      #całe to wyrażenie tworzy tzw. URLconfig (URLConf)
    #path("february", views.february),
    #path("march", views.march),
    path("<month>", views.monthly_challenge)  # <> - placeholder         #nie obchodzi mnie co tu jest napisane, wiem, że jest to miesiac, moze to byc kazdy miesiac
]

#mam URL, które są obsługiwane przez aplikację challenges w całym projekcie monthly_challenges.
#trzeba teraz połączyć aplikacje challenge z całym projektem
#Należy stworzyć URLconfig projektu, oprócz tego URLConfigu, który jest tutaj w tyej aplikacji


#Można tak dodawać mnóstwo tych urli manualnie, ale można też automatycznie.

#Jeśli wiem ile będzie URLi, można stworzyć URLPattern, który będzie dynamicznie przekazywał wartości. Jest View Funkcja, która skupia się na dynamicznych URLach.


#Jeśli nie wiem ile będzie URLi 