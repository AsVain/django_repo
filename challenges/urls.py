#Lista wszystkich URL, jakie są obsługiwane w aplikacji
from django.urls import path    #funkcja przyjmuje dwa argumenty: string - URL oraz wskaźnik na funkcje view, która powinna być wywołana
from . import views     #z tego samego folderu, gdzie jestem, użyj pliku views

urlpatterns = [
    #path("january", views.january),      #całe to wyrażenie tworzy tzw. URLconfig (URLConf)
    #path("february", views.february),
    #path("march", views.march),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge)  # <> - placeholder         #nie obchodzi mnie co tu jest napisane, wiem, że jest to miesiac, moze to byc kazdy miesiac, path("<month>", views.monthly_challenge)
    
]
#palceholder przyjmuje każde wartości, dlatego tak zsotawiony placeholder będzie przyjmował np słowa anything, koło, szkoła, wszystko...
#Można ograniczyć ten placeholder, np. poprzez typ danych, jakim musi być. path("<str:month>", views.monthly_challenge)

#mam URL, które są obsługiwane przez aplikację challenges w całym projekcie monthly_challenges.
#trzeba teraz połączyć aplikacje challenge z całym projektem
#Należy stworzyć URLconfig projektu, oprócz tego URLConfigu, który jest tutaj w tyej aplikacji


#Można tak dodawać mnóstwo tych urli manualnie, ale można też automatycznie.

#Jeśli wiem ile będzie URLi, można stworzyć URLPattern, który będzie dynamicznie przekazywał wartości. Jest View Funkcja, która skupia się na dynamicznych URLach.


#Jeśli nie wiem ile będzie URLi 