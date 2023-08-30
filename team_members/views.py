from django.shortcuts import render

from accounts.views import check_role_admin


# Create your views here.



def team_display_all_member(request):
    return render(request, 'team_members/display_all_member.html')


def team_display_comment(request):
    return render(request, 'team_members/display_comment.html')



def team_new_comment(request):
    return render(request, 'team_members/new_comment.html')




