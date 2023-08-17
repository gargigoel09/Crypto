from django.shortcuts import render
import requests
from django.http import HttpResponse
from django_ratelimit.decorators import ratelimit
from django_ratelimit.exceptions import Ratelimited

# Create your views here.


@ratelimit(key='ip', rate='10/hour')
def home_view(request):
    try:
        url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'
        data = requests.get(url).json()

        context = {'data': data}

        return render(request, 'main.html', context)
    except Ratelimited as e:
        # Handle rate limit exceeded
        return HttpResponse("Rate limit exceeded. Please try again later.", status=429)
