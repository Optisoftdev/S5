from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import UserCreationForm
from django.views import View
# from admission.forms import ApplyForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404

from django.urls import reverse

# import Users model from authentication module
from authentication.models import Users, AccountType

# import Schools model from administrator module
from administrator.models import Schools


# Create your views here.

# class ApplyView(View):
#     form_class = ApplyForm
#     template_name = 'admission/apply.html'


#     def get(self, request):
#         return render(request, 'apply.html')


#     def post(self, request):
#         if request.method == 'POST':
#             first_name = request.POST.get('first_name' or None)
#             middlename = request.POST.get('middlename' or None)
#             last_name = request.POST.get('last_name' or None)
#             email = request.POST.get('email' or None)
#             password = request.POST.get('password' or None)
#             phone = request.POST.get('phone' or None)
#             address = request.POST.get('address' or None)
#             gender = request.POST.get('gender' or None)
#             dob = request.POST.get('dob' or None)
#             passport = request.FILES.get('passport' or None)
#             category = request.POST.get('category' or None)
#             classes = request.POST.get('classes' or None)
#             religion = request.POST.get('religion' or None)
#             account_type = AccountType.objects.get(id=4)
#             school_id = 2

#             fresh = Users()
#             fresh.first_name = first_name
#             fresh.middlename = middlename
#             fresh.last_name = last_name
#             fresh.email = email
#             # fresh.set_password(password)
#             fresh.password = password
#             fresh.phone = phone
#             fresh.address = address
#             fresh.gender = gender
#             fresh.dob = dob
#             fresh.passport = passport
#             fresh.category = category
#             fresh.classes = classes
#             fresh.religion = religion
#             fresh.account_type = account_type
#             fresh.school_id = school_id
#             fresh.save()

#             fresh = authenticate(email=email, password=password)

#             if fresh is not None:
#                 login(request, fresh)
#                 return redirect('/')
#             else:
#                 return render(request, 'apply.html')


# apply for school admission
def apply(request, id):
    
    # fetch all the schools
    instance = get_object_or_404(Schools, id=id)
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name' or None)
        middlename = request.POST.get('middlename' or None)
        last_name = request.POST.get('last_name' or None)
        email = request.POST.get('email' or None)
        password = request.POST.get('password' or None)
        phone = request.POST.get('phone' or None)
        address = request.POST.get('address' or None)
        gender = request.POST.get('gender' or None)
        dob = request.POST.get('dob' or None)
        passport = request.FILES.get('passport' or None)
        category = request.POST.get('category' or None)
        classes = request.POST.get('classes' or None)
        religion = request.POST.get('religion' or None)
        account_type = AccountType.objects.get(id=4)
        # school_id = Schools.objects.get(id=4)
        school_id = instance

        fresh = Users()
        fresh.first_name = first_name
        fresh.middlename = middlename
        fresh.last_name = last_name
        fresh.email = email
        # fresh.set_password(password)
        fresh.password = password
        fresh.phone = phone
        fresh.address = address
        fresh.gender = gender
        fresh.dob = dob
        fresh.passport = passport
        fresh.category = category
        fresh.classes = classes
        fresh.religion = religion
        fresh.account_type = account_type
        fresh.school_id = school_id
        fresh.save()

        fresh = authenticate(email=email, password=password)

        if fresh is not None:
            login(request, fresh)
            return redirect('/')
        else:
            return render(request, 'apply.html')

    # context = {'instance':instance}
    return render(request, 'apply.html')
