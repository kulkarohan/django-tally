from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework import generics
from .models import YelpYelpScraping
from .serializers import YelpYelpScrapingSerializer
from tallylib.scraper import yelpScraper

import requests
import json


def index(request):
    return HttpResponse("Hello, world. You're at the Yelp review analytics app index page.")


def getPosNegPhrases(request, business_id):
    result = json.dumps(yelpScraper(business_id))
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

