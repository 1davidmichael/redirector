from django.shortcuts import render
from django.http import HttpResponse

from redirector_tool.models import Redirect
# Create your views here.
def index(request):
    all_redirects = Redirect.objects.order_by('-expiration_date')
    output = ', '.join([r.source_url for r in all_redirects])
    return HttpResponse(output)

def detail(request, redirect_id):
    return HttpResponse("you're looking at redirect %s" % redirect_id)
