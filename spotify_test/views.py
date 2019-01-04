from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from spotify_test.config import client_id,client_secret
from django.urls import reverse

# Create your views here.



def index(request):
    redirect_uri = reverse('spotify_test:success')
    scope='playlist-read-private'
    response_type='code'
    return render(request, 'spotify_test/index.html', {'client_id':client_id, 'redirect_uri':redirect_uri, 'scope':scope, 'response_type':response_type })

def success(request):
    return HttpResponse("you've made it")
