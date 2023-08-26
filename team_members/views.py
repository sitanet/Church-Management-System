from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, 'team_members/dashboard.html')


def display_all_member(request):
    return render(request, 'team_members/display_all_member.html')


def display_comment(request):
    return render(request, 'team_members/display_comment.html')



def new_comment(request):
    return render(request, 'team_members/new_comment.html')




