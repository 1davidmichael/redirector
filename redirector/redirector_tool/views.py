from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from redirector_tool.models import Redirect
# Create your views here.
def index(request):
    all_redirects = Redirect.objects.order_by('-expiration_date')
    context = {'all_redirects': all_redirects}
    return render(request, 'redirector_tool/index.html', context)

def detail(request, redirect_id):
    redirect = get_object_or_404(Redirect, pk=redirect_id)
    return render(request, 'redirector_tool/detail.html', {'redirect': redirect})
