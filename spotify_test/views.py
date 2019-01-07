from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from spotify_test.config import client_id,client_secret
from django.urls import reverse
import urllib
import requests

# Create your views here.


def index(request):
    scope='playlist-read-private'
    response_type='code'
    show_dialog='true'
    return render(request, 'spotify_test/index.html', {'client_id':client_id, 'redirect_uri':redirect_uri, 'scope':scope, 'response_type':response_type, 'show_dialog':show_dialog })

def success(request):
    code = request.GET.get('code')
    redirect_uri = urllib.parse.quote(request.build_absolute_uri() + 'success/')
    access_token_request_data = {
        'grant_type':'authorization_code',
        'code':code,
        'redirect_uri':redirect_uri
    }
    r = requests.post(url='https://accounts.spotify.com/api/token', data=access_token_request_data)
    return HttpResponse(f'we\'re in bitch <br> here\'s your code ya filthy animal: <br> {code} <br> and the access token {r}')
