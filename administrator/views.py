from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages

# import model from another module

# import Users model from authentication module
from authentication.models import Users, AccountType

# import model
from .models import Schools

# Create your views here.
def index(request, id):

    # fetch all the schools
    instance = get_object_or_404(Schools, id=id)

    context = {'instance':instance}
    return render(request, 'index.html', context)

# School registration page
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name' or None)
        address = request.POST.get('address' or None)
        state = request.POST.get('state' or None)
        lga = request.POST.get('lga' or None)
        logo = request.FILES.get('logo' or None)
        school_type = request.POST.get('school_type' or None)

        school = Schools()
        school.name = name
        school.address = address
        school.state = state
        school.lga = lga
        school.logo = logo
        school.school_type = school_type
        school.save()

        if school is not None:
            return HttpResponseRedirect(reverse('administrator:register'))
    else:
        return render(request, 'register.html')


# Show all School
def all_school(request):
    schools = Schools.objects.all()
    context = {'schools': schools, 'instance':instance}
    return render(request, 'all_school.html', context)


# view a specific school
def view_school(request, id):

    # fetch all the schools
    instance = get_object_or_404(Schools, id=id)

    # fetch all the school admin
    # school_admin = get_object_or_404(Users(), id=id)


    # Register School admin
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middlename = request.POST.get('middlename')
        email = request.POST.get('email')
        account_type = AccountType.objects.get(id=2)
        gender = request.POST.get('gender')
        school_id = id

        s_admin = Users()
        s_admin.first_name = first_name
        s_admin.last_name = last_name
        s_admin.middlename = middlename
        s_admin.email = email
        s_admin.account_type = account_type
        s_admin.gender = gender
        s_admin.school_id = school_id
        s_admin.save()

        if s_admin is not None:
            return HttpResponseRedirect(reverse('administrator:view_school', args=[id]))
    else:
        return render(request, 'view_school.html')

    context = {'instance':instance}
    return render(request, 'view_school.html', context)
