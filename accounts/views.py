from datetime import datetime
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import message
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import urlsafe_base64_decode

from accounts.utils import detectUser, send_verification_email
from follow_app.models import Member


from .forms import UserForm, UserProfileForm, UserProfilePictureForm
from .models import User, UserProfile
from django.contrib import messages, auth
# from .utils import detectUser, send_verification_email
from django.contrib.auth.decorators import login_required, user_passes_test

from django.core.exceptions import PermissionDenied
# from vendor.models import Vendor
# from django.template.defaultfilters import slugify
# from orders.models import Order
import datetime

# Create your views here.

# Restrict the vendor from accessing the customer page
def check_role_admin(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied


# Restrict the customer from accessing the vendor page
def check_role_coordinator(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied
    
def check_role_team_member(user):
    if user.role == 3:
        return True
    else:
        raise PermissionDenied
@login_required(login_url='login')
@user_passes_test(check_role_admin)
def registeruser(request):
     
     if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
          
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
            mail_subject = 'Please activate your account'
            email_template = 'accounts/email/accounts_verification_email.html'
            send_verification_email(request, user, mail_subject, email_template)
            messages.success(request, 'Your account has been registered sucessfully!')
            return redirect('registeruser')
        else:
            print('invalid form')
            print(form.errors)
     else:
        form = UserForm()
     context = {
        'form': form,
    }
     return render(request, 'accounts/registeruser.html', context)

@login_required(login_url='login')
def myAccount(request):
    user = request.user
    redirectUrl = detectUser(user)
    return redirect(redirectUrl)

@login_required(login_url='login')
def dashboard(request):
    member = Member.objects.filter(status=1).count()
    member_inctive = Member.objects.filter(status=2).count()
    member_male = Member.objects.filter(gender=1).count()
    member_female = Member.objects.filter(gender=2).count()
    member_single = Member.objects.filter(marital_status=1).count()
    member_married = Member.objects.filter(marital_status=2).count()
    

    context = {
        'member': member,
        'member_inctive': member_inctive,
        'member_male': member_male,
        'member_female': member_female,
        'member_single': member_single,
        'member_married': member_married,
    }
    return render(request, 'admin_staff/dashboard.html', context)

@login_required(login_url='login')
def coor_dashboard(request):
    member = Member.objects.filter(status=1).filter(team_lead=request.user).count()
    member_inctive = Member.objects.filter(status=2).filter(team_lead=request.user).count()
    member_male = Member.objects.filter(gender=1).filter(team_lead=request.user).count()
    member_female = Member.objects.filter(gender=2).filter(team_lead=request.user).count()
    member_single = Member.objects.filter(marital_status=1).filter(team_lead=request.user).count()
    member_married = Member.objects.filter(marital_status=2).filter(team_lead=request.user).count()
    

    context = {
        'member': member,
        'member_inctive': member_inctive,
        'member_male': member_male,
        'member_female': member_female,
        'member_single': member_single,
        'member_married': member_married,
    }
    return render(request, 'coordinators/coor_dashboard.html', context)

@login_required(login_url='login')
def team_dashboard(request):
    member = Member.objects.filter(status=1).filter(team_member=request.user).count()
    member_inctive = Member.objects.filter(status=2).filter(team_member=request.user).count()
    member_male = Member.objects.filter(gender=1).filter(team_member=request.user).count()
    member_female = Member.objects.filter(gender=2).filter(team_member=request.user).count()
    member_single = Member.objects.filter(marital_status=1).filter(team_member=request.user).count()
    member_married = Member.objects.filter(marital_status=2).filter(team_member=request.user).count()
    

    context = {
        'member': member,
        'member_inctive': member_inctive,
        'member_male': member_male,
        'member_female': member_female,
        'member_single': member_single,
        'member_married': member_married,
    }
    return render(request, 'team_members/team_dashboard.html', context)





def change_password(request):
    return render(request, 'accounts/change_password.html')



def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('myAccount')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('myAccount')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'You are logged in.')
    return redirect('login')



# def profile(request):
   
#     return render(request, 'accounts/profile.html')


# def profile(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')  # Redirect to the user's profile page
#     else:
#         form = UserForm(instance=request.user)
#     return render(request, 'accounts/profile.html', {'form': form})




def profile(request):
    if request.method == 'POST':
        form = UserProfilePictureForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updated.')
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = UserProfilePictureForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})






def activate(request, uidb64, token):
    # Activate the user by setting the is_active status to True
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulation! Your account is activated.')
        return redirect('myAccount')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('myAccount')



def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)

            # send reset password email
            mail_subject = 'Reset Your Password'
            email_template = 'accounts/email/reset_password_email.html'
            send_verification_email(request, user, mail_subject, email_template)

            messages.success(request, 'Password reset link has been sent to your email address.')
            return redirect('forgot_password')
        else:
            messages.error(request, 'Account does not exist')
            return redirect('forgot_password')
    return render(request, 'accounts/forgot_password.html')



def reset_password_validate(request, uidb64, token):
    # validate the user by decoding the token and user pk
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.info(request, 'Please reset your password')
        return redirect('reset_password')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('myAccount')



def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            pk = request.session.get('uid')
            user = User.objects.get(pk=pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('reset_password')
    return render(request, 'accounts/reset_password.html')


def change_password(request):
   
    return render(request, 'accounts/change_password.html')