from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework import generics
from .serializers import YelpYelpScrapingSerializer
from .models import YelpYelpScraping
from tallylib.scraper import yelpScraper

import requests
import json


def index(request):
    return HttpResponse("Hello, world. You're at the Yelp Scraping app index page.")

def profile(request, business_id):
    # return HttpResponse('<h1> test {}.</h1>'.format(business_id))
    API_KEY = '-Io9W4bQSEfc3BxAwTvOV3B-aU9oS5j0F7LB7mWTXA79cRlMEmJzI7b_xIlqzSZd4b6IHiOlfp5APBsWNJt8cQRTV61u-r7DTKBCy1QTt91H9jjNjAEi0P6pjCTwXXYx'
    HEADERS = {'Authorization': f'Bearer {API_KEY}'}

    BUSINESS_ID = business_id
    URL = f'https://api.yelp.com/v3/businesses/{BUSINESS_ID}/reviews'
    req = requests.get(URL, headers=HEADERS)
    parsed = json.loads(req.text)
    reviews = parsed['reviews']
    reviews_json = []
    for review in reviews:
        output = {'id': review['id'], 'time': review['time_created'], 'text': review['text'], 'rating': review['rating']}
        reviews_json.append(output)

    nlp_prediction = yelpScraper(BUSINESS_ID)
    result = json.dumps(nlp_prediction, indent=2)

    return HttpResponse(result)


class YelpYelpScrapingCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = YelpYelpScraping.objects.all()
    serializer_class = YelpYelpScrapingSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class YelpYelpScrapingDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = YelpYelpScraping.objects.all()
    serializer_class = YelpYelpScrapingSerializer

