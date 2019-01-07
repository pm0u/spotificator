from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from spotify_test.config import client_id,client_secret,redirect_uri,scope
from django.urls import reverse
import urllib
import requests
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from oauthlib.oauth2 import BackendApplicationClient
import json

oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)


# Create your views here.

def index(request):

    authorization_url, state = oauth.authorization_url('https://accounts.spotify.com/authorize', show_dialog='true')

    return render(request, 'spotify_test/index.html', { 'auth_url': authorization_url})

def backend(request):

    auth = HTTPBasicAuth(client_id, client_secret)
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url='https://accounts.spotify.com/api/token', auth=auth)

    test_track = oauth.get('https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V')
    print(test_track.text)

    return HttpResponse(f'we\'re in bitch <br> here\'s your access token ya filthy animal: {token} <br><br> did the test track work? {test_track.text}')

def success(request):

    authorization_response = request.get_full_path()
    token = oauth.fetch_token('https://accounts.spotify.com/api/token', client_id=client_id, client_secret=client_secret, authorization_response=authorization_response)
    request.session['token'] = token
    links = [{'href' : 'spotify_test:playlists', 'text': 'playlists'}, {'href': 'spotify_test:search', 'text': 'search'}]
    return render(request, 'spotify_test/success.html', { 'links': links, 'token': token })

def playlists(request):
    user_info = oauth.get('https://api.spotify.com/v1/me')
    user_json = json.loads(user_info.text)
    request.session['user_id'] = user_json['id']

    user_playlists = json.loads(oauth.get(f'https://api.spotify.com/v1/users/{request.session["user_id"]}/playlists').text)

    return render(request, 'spotify_test/playlists.html', { 'playlists': user_playlists['items'] } )

def search(request):

    return HttpResponse('this will be a search some day')
