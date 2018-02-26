from django.shortcuts import render

# Create your views here.

# registration home page
def register(request):
    return render(request, 'login.html')