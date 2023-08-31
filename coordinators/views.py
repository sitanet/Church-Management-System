from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.

@login_required(login_url='login')
def coor_register_member(request):
    return render(request, 'coordinators/register_member.html')

@login_required(login_url='login')
def coor_display_all_member(request):
    return render(request, 'coordinators/display_all_member.html')

@login_required(login_url='login')
def coor_display_comment(request):
    return render(request, 'coordinators/display_comment.html')


@login_required(login_url='login')
def coor_new_comment(request):
    return render(request, 'coordinators/new_comment.html')




