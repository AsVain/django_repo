from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound #wbudowana klasa #not found - 404 error moze byc wyswietlony


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
# Create your views here.

#Pierwszy widok, na request do serwera, zwracam stringa. Póki co nie robię nic z requestem
"""def january(request):
    return HttpResponse("Eat no meat for the entire month!")

def february(request):
    return HttpResponse("Walk for at least 20 minutes every day!")

#kiedy mamy to wywołać? Musimy to zdefininiować w urls.py, który stworzyłem. Mamy też folder urls.py w katalogu głównym projektu "monthly challenges", 
#                                                                   ale musimy mieć zdefiniowany URL w pliku urls.py w katalogu aplikacji, jaką tworzę

def march(request):
    return HttpResponse("Learn Django for at least 20 minutes every day!")
"""
def monthly_challenge(requeste, month):
    
    """
    challange_text = None   #by default będzie przyjmować wartość None
   
    if month == 'january':
        challange_text = "Eat no meat for the entire month!"
    
    elif month == 'february':
        challange_text = "Walk for at least 20 minutes every day!"
        
    elif month == 'march':
        challange_text = "Learn Django for at least 20 minutes every day!"
        
    elif month == 'april':
        challange_text = "Walk for a"
        
    elif month == 'may':
        challange_text = " every day!"
        
    elif month == 'june':
        challange_text = "20 minutes every day!"
        
    elif month == 'july':
        challange_text = "Walk  20 minutes every day!"
        
    elif month == 'august':
        challange_text = "Walk for at least 20 minutes day!"
        
    elif month == 'september':
        challange_text = "Walk for at least 20 minutes every day"
        
    elif month == 'october':
        challange_text = "Walk for at  20 minutes every day!"
        
    elif month == 'november':
        challange_text = "Walk for at least  minutes every day!"
        
    elif month == 'december':
        challange_text = " for at least 20 minutes every !"
      
    else:
        return HttpResponseNotFound("This month is not supported!")   

    return HttpResponse(challange_text)
"""
    try: 
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")    

def monthly_challenge_by_number(request, month):
    months = monthly_challenges.keys()
    
    return HttpResponse(month)








