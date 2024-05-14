#Lista wszystkich URL, jakie są obsługiwane w aplikacji
from django.urls import path    #funkcja przyjmuje dwa argumenty: string - URL oraz wskaźnik na funkcje view, która powinna być wywołana
from . import views     #z tego samego folderu, gdzie jestem, użyj pliku views

urlpatterns = [

    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge)  # <> - placeholder         #nie obchodzi mnie co tu jest napisane, wiem, że jest to miesiac, moze to byc kazdy miesiac, path("<month>", views.monthly_challenge)
                                                  #placeolder, który trzyma obojętnie jakie wartości jest nazwany month. path odnosi się do funkcji view monthly_challange
]
