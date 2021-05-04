from django.http import HttpResponse
from django.utils.html import escape

def index(request):
    return HttpResponse("Moe's new poll site in Djangoooo!")
