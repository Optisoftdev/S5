from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'layout/index.html')