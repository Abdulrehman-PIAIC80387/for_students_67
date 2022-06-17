from distutils.spawn import spawn
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from bs4 import BeautifulSoup
import requests



# Create your views here.
def home(request):
    

    obj = Text.objects.create()
	


    if request.method == "POST":
        word = request.POST['word']
        
        url = 'https://www.dictionary.com/browse/'+word
        r = requests.get(url)

       
        data = r.content

        
        
        
        soup = BeautifulSoup(data, 'html.parser')

        #print(soup)

       
        span = soup.find_all('span', {"class": "one-click-content"})
       
       

        obj.word = word
        obj.save()
        
        refined=span[0].text

        print(refined)
        obj.result = refined
        obj.save()
     	
        queryset = Text.objects.all()

        param = {'text': span[0].text, 'word': word,'queryset':queryset}
        return render(request, 'index.html', param)
    else:
        return render(request, 'index.html')
