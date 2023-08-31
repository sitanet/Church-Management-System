from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'admin_staff/dashboard.html')
@login_required(login_url='login')
def register_member(request):
    return render(request, 'admin_staff/register_member.html')

@login_required(login_url='login')
def display_all_member(request):
    return render(request, 'admin_staff/display_all_member.html')

@login_required(login_url='login')
def display_comment(request):
    return render(request, 'admin_staff/display_comment.html')


@login_required(login_url='login')
def new_comment(request):
    return render(request, 'admin_staff/new_comment.html')



