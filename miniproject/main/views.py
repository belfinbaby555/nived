from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.template import loader
from django.middleware.csrf import get_token
from django.contrib.auth.hashers import make_password, check_password
import time
from .models import Data


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())  
from django.db.models import Q

def search_teachers(request, place=None, season=None, category=None, type=None, stars=None):
    print(f"Received parameters: place={place}, season={season}, category={category}, type={type}, stars={stars}")

    # Convert 'None' strings to actual None values
    if place == 'None':
        place = None
    if season == 'None':
        season = None
    if category == 'None':
        category = None
    if type == 'None':
        type = None
    if stars == 'None':
        stars = None

    print(f"After conversion: place={place}, season={season}, category={category}, type={type}, stars={stars}")

    # Convert place parameter to lowercase
    if place:
        place = place.lower()

    # Initialize an empty query list
    queries = []

    # Add parameters to the query list if they are not None
    if place is not None:
        queries.append(Q(place=place))
    if season is not None:
        queries.append(Q(season=season))
    if category is not None:
        queries.append(Q(category=category))
    if type is not None:
        queries.append(Q(type=type))
    if stars is not None:
        queries.append(Q(stars=stars))

    print("Constructed queries:", queries)

    # If no parameters are provided, return an empty response
    if not queries:
        return JsonResponse({'message': 'No parameters provided for search'})

    # Create a combined query using 'AND' logic
    combined_query = Q()
    for query in queries:
        combined_query &= query

    print("Combined query:", combined_query)

    # Filter data based on the combined query
    data = Data.objects.filter(combined_query)

    print("Filtered data:", data)

    # Check if any data match the query
    if data.exists():
        # Serialize the queryset into JSON
        data_data = [{'uid': teacher.uid,
                          'place': teacher.place,
                          'image': teacher.image,
                          'season': teacher.season,
                          'category': teacher.category,
                          'type': teacher.type,
                          'stars': teacher.stars} for teacher in data]
        return JsonResponse({'data': data_data})
    else:
        return JsonResponse({'message': 'No data found with the given criteria'})
