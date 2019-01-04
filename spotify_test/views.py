from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from spotify_test.config import client_id,client_secret
from django.urls import reverse
import urllib

# Create your views here.



def index(request):
    redirect_uri = urllib.parse.quote(request.build_absolute_uri() + 'success/')
    scope='playlist-read-private'
    response_type='code'
    show_dialog='true'
    return render(request, 'spotify_test/index.html', {'client_id':client_id, 'redirect_uri':redirect_uri, 'scope':scope, 'response_type':response_type, 'show_dialog':show_dialog })

def success(request):
    code = request.GET.get('code')
    return HttpResponse(f'we\'re in bitch <br> here\'s your code ya filthy animal: <br> {code}')
