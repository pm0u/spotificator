from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from spotify_test.config import client_id,client_secret
from django.urls import reverse
import urllib
import requests
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from oauthlib.oauth2 import BackendApplicationClient
import json

# Create your views here.


def index(request):
    redirect_uri = request.build_absolute_uri() + 'success/'
    scope='playlist-read-private'
    show_dialog='true'
    request.session['redirect_uri'] = redirect_uri
    request.session['scope'] = scope
    request.session['show_dialog'] = 'true'
    oauth = OAuth2Session(client_id, redirect_uri=request.session['redirect_uri'], scope=request.session['scope'])
    print(oauth)
    #request.session['oauth'] =  oauth
    authorization_url, state = oauth.authorization_url('https://accounts.spotify.com/authorize', show_dialog='true')
    print(authorization_url)
    return render(request, 'spotify_test/index.html', { 'auth_url': authorization_url})

def success(request):

    auth = HTTPBasicAuth(client_id, client_secret)
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url='https://accounts.spotify.com/api/token', auth=auth)

    test_track = oauth.get('https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V')
    print(test_track.text)


    return HttpResponse(f'we\'re in bitch <br> here\'s your access token ya filthy animal: {token} <br><br> did the test track work? {test_track.text}')

def playlists(request):
    pass
