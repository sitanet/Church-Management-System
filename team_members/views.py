from django.shortcuts import render


# Create your views here.
# def register_member(request):
#     return render(request, 'admin_staff/register_member.html')


def display_all_member(request):
    return render(request, 'admin_staff/display_all_member.html')


def display_comment(request):
    return render(request, 'admin_staff/display_comment.html')



def new_comment(request):
    return render(request, 'admin_staff/new_comment.html')




