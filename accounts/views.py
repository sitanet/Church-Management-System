from datetime import datetime
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import message
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.utils.http import urlsafe_base64_decode

from accounts.utils import send_verification_email


from .forms import UserForm
from .models import User, UserProfile
from django.contrib import messages, auth
# from .utils import detectUser, send_verification_email
# from django.contrib.auth.decorators import login_required, user_passes_test

# from django.core.exceptions import PermissionDenied
# from vendor.models import Vendor
# from django.template.defaultfilters import slugify
# from orders.models import Order
import datetime

# Create your views here.
def registeruser(request):
    #  if request.user.is_authenticated:
    #     messages.warning(request, 'You are already logged in!')
    #     return redirect('registeruser')
     if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Create the user using the form
            # password = form.cleaned_data['password']
            
            # user = form.save(commit=False)
            
            # user.set_password(password)
            
            # user.save()

            # Create the user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
          
            password = form.cleaned_data['password']
            phone_number = form.cleaned_data['phone_number']
            role = form.cleaned_data['role']

            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, role=role, phone_number=phone_number, password=password)
            
            user.save()
            messages.success(request, 'You have successfull register User')

            # Send verification email
            # mail_subject = 'Please activate your account'
            # email_template = 'accounts/emails/account_verification_email.html'
            # send_verification_email(request, user, mail_subject, email_template)
            # messages.success(request, 'Your account has been registered sucessfully!')
            # return redirect('registeruser')
        else:
            print('invalid form')
            print(form.errors)
     else:
        form = UserForm()
     context = {
        'form': form,
    }
     return render(request, 'accounts/registeruser.html', context)


def dashboard(request):
    return render(request, 'admin_staff/dashboard.html')

def dashboard(request):
    return render(request, 'admin_staff/dashboard.html')



def profile(request):
    return render(request, 'accounts/profile.html')


def change_password(request):
    return render(request, 'accounts/change_password.html')



# def login(request):
#     return render(request, 'login.html')