from django.shortcuts import render, redirect
from django.core import serializers
from django.contrib.messages import constants as messages
from django.http import HttpRequest, HttpResponse
import json
import requests 

ERROR = 40
###################################################################
#Function to do a search using user entered "searchKeyWord"
###################################################################
def get_json_from_query(request):
    #default is set to mars
    keyword = request.GET.get('p','xyz')
    search_url = "https://images-api.nasa.gov/search?keywords=%s&media_type=image"%(keyword)
    image_results = requests.get(search_url)
    results_as_json = image_results.json()
    #get to the 'items' elements in the returned json. 'items' is a list 
    items = results_as_json['collection']['items']
    details = []
    #iterate through the items from json to get to  the image. Usually it's set to 100 images
    for item in items:
        data = item['data'][0]
        links = item['links'][0]     
        item_data = { 
                "title": data['title'], 
                "description":data['description'],
                "date_created":data['date_created'], 
                "image":links['href']
        }
        
        details.append(item_data)
    if items is None:
        messages.ERROR(request, f'Three credits remain in your account.')
        return redirect('home')

    # result = json.dumps(details)
    return render(request, 'search/index.html', {
        'result_items': details
    })

def home(request):
    return render(request, 'search/index.html')

def about(request):
    return render(request, 'search/about.html')

