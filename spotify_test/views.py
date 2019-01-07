from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from spotify_test.config import client_id,client_secret
from django.urls import reverse
import urllib
import requests
import json
import base64

# Create your views here.


def index(request):
    scope='playlist-read-private'
    response_type='code'
    show_dialog='true'
    redirect_uri = urllib.parse.quote(request.build_absolute_uri() + 'success/')
    return render(request, 'spotify_test/index.html', {'client_id':client_id, 'redirect_uri':redirect_uri, 'scope':scope, 'response_type':response_type, 'show_dialog':show_dialog })

def success(request):
    code = request.GET.get('code')
    redirect_uri = request.build_absolute_uri('/spotify/success/')
    access_token_request_data = {
        'grant_type':'authorization_code',
        'code':code,
        'redirect_uri':redirect_uri,
        #'client_id':client_id,
        #'client_secret':client_secret
    }
    combined_ids = f'{client_id}:{client_secret}'
    encoded_combined = base64.b64encode(combined_ids.encode('utf-8'))
    auth_headers = {
        'Authorization': f'Basic {encoded_combined}'
    }
    print(auth_headers)
    r = requests.post(url='https://accounts.spotify.com/api/token', data=access_token_request_data, headers=auth_headers)

    request.session['spotify_auth'] = json.loads(r.text)

    return HttpResponse(f'we\'re in bitch <br> here\'s your code ya filthy animal: <br> {code} <br> and the access token {request.session["spotify_auth"]}')

def playlists(request):
    pass
