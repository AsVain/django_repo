from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect #wbudowana klasa #not found - 404 error moze byc wyswietlony oraz klasa do przekierowywania


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
    "december": "Eat no meat for the entire month!"
}

def monthly_challenge(request, month):      #przyjmuje request od klienta oraz month (placeholder obojetnie jakiego URL)
    try: 
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)             #co zwraca użytkownikowi
    except:
        return HttpResponseNotFound("This month is not supported!")    

def monthly_challenge_by_number(request, month):        #redirections - numery na miesiące
    months = list(monthly_challenges.keys())                #.keys() - funkcja, która wypisuje keys ze słownika
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

    #response with code 3## to redirect 
    """
        responses:
        1 - informational responses
        2 - successful responses
        3 - redirection messages
        4 - client server responses
        5 - server error responses                                
                                        
    """






