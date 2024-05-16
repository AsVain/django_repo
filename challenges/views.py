from django.shortcuts import render #zamienia funkcję render_to_string i wysyła z powrotem odpowiedź. 
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect #wbudowana klasa #not found - 404 error moze byc wyswietlony oraz klasa do przekierowywania
from django.urls import reverse #pozwala tworzyć ścieżki (paths) poprzez odsyłanie do nazw ścieżek tych URL
#from django.template.loader import render_to_string #generowanie czegoś do stringa


monthly_challenges = {                  #słownik z miesiącami, po to by zautomatyzować proces i skrócić działanie kodu
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Eat no meat for the entire month!",
    "july": "Learn Django for at least 20 minutes every day!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Eat no meat for the entire month!",
    "october": "Learn Django for at least 20 minutes every day!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}

def index(request):      #lista miesięcy na stronie głównej
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge(request, month):      #przyjmuje request od klienta oraz month (placeholder obojetnie jakiego URL)
    try: 
        challenge_text = monthly_challenges[month]  
        return render(request, "challenges/challenge.html", {       #ten słownik jest nazwany contextem templatki lub generowanie templatki
            "text": challenge_text,
            "month_name": month
            })                                                      #render() potrzebuje 2 argumentow, request oraz sciezka do pliku
                                                                    #response_data = render_to_string("challenges/challenge.html")    #f"<h1>{challenge_text}</h1>"    #f-string -> dzieki temu mozna zawrzec miedzy cudzyslowiem wartosci, zmienne jakie chcemy
                                                                    #return HttpResponse(response_data)             #co zwraca użytkownikowi    #musi tu być trzeci argument - słownik, zeby zrobic dynamiczny plik html
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")    


def monthly_challenge_by_number(request, month):        #redirections - numery na miesiące
    months = list(monthly_challenges.keys())                #.keys() - funkcja, która wypisuje keys ze słownika
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])          #/challenge/january      #dzieki temu mozemy zmienic url w projekcie jak i kiedy chcemy
    return HttpResponseRedirect(redirect_path)    #challanges są zahardkodowane w urlach całego projektu, nie chcemy tego.







