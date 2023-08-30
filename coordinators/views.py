from django.shortcuts import render


# Create your views here.


def coor_register_member(request):
    return render(request, 'coordinators/register_member.html')


def coor_display_all_member(request):
    return render(request, 'coordinators/display_all_member.html')


def coor_display_comment(request):
    return render(request, 'coordinators/display_comment.html')



def coor_new_comment(request):
    return render(request, 'coordinators/new_comment.html')




