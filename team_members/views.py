from django.shortcuts import render

from accounts.views import check_role_admin


# Create your views here.



def team_display_all_member(request):
    return render(request, 'team_members/display_all_member.html')


def team_display_comment(request):
    return render(request, 'team_members/display_comment.html')



def team_new_comment(request):
    return render(request, 'team_members/new_comment.html')




# @login_required(login_url='login')
# def new_comment(request, id):
#     member = get_object_or_404(Member, id=id, team_member=2)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.member = member
#             comment.save()
#             return redirect('display_comment')
   
#     else:
#         form = CommentForm()
        
#     context = {
#          'member':member,
#          'form':form,
       
         
#      }
#     return render(request, 'admin_staff/new_comment.html', context)