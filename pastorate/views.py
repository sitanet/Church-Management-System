from tokenize import Comment
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.models import User

from accounts.views import check_role_coordinator, check_role_pastorate
from follow_app.forms import CommentForm, MemberForm
from django.contrib import messages

from follow_app.models import Team_Lead, Member, TeamMember
from follow_app.models import Comment
from django.template.loader import render_to_string
from django.core.mail import send_mail


# Create your views here.

@user_passes_test(check_role_pastorate)
def past_register_member(request):
    
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        
        
       
        if form.is_valid():
            
           
            form = form.save(commit=False)
            
            form.user = request.user
          
            form.save()

            recipient_email = request.POST.get('email')
            recipient_name = request.POST.get('first_name')
            subject = 'Thank you for Coming'
            
            # Render the HTML email template
            html_message = render_to_string(
                'accounts/email/welcome_email.html',
                {
                    'recipient_name': recipient_name,
                
                }
            )

        # Send the email
            send_mail(
                subject,
                '',
                'The CityGate Church Follow Up Unit',
                [recipient_email],
                fail_silently=False,
                html_message=html_message,
            )

        
            messages.success(request, 'Account has been registered successfully!.')
            return redirect('coor_display_all_member')
            
        
    
        
        else:
            messages.warning(request, form.errors)
            messages.warning(request, 'Please Check the form filed and fill them before submission!.')
            return redirect('coor_register_member')
            # print('invalid form')
            
    else:
       
        form = MemberForm()
        current_user = request.user
        team_lead = Team_Lead.objects.filter(name=current_user)
        team_members = TeamMember.objects.all()
        member = User.objects.all()
       

        
        # cust_coa = Coa.objects.raw("select * from chart_of_accounts_coa where right(gl_no,3) = '200'")
        
        
        context = {
             'form': form,
             'team_lead': team_lead,
             'team_members': team_members,
             'member': member,
          
            
        }
   

    return render(request, 'pastorate/past_register_member.html', context)


@user_passes_test(check_role_pastorate)
def past_member_detail(request, id):
    member = get_object_or_404(Member, id=id)
    team_lead = None  # Initialize variables outside the 'else' block
    team_members = None
    
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been Updated successfully!.')
            return redirect('past_display_all_member')
    else:
        form = MemberForm(instance=member)
        current_user = request.user
        team_lead = Team_Lead.objects.filter(name=current_user)
        team_members = TeamMember.objects.all()
    
    return render(request, 'coordinators/past_member_detail.html', {'form': form, 'member': member, 'team_lead': team_lead, 'team_members': team_members})



@user_passes_test(check_role_pastorate)
def past_display_comment(request):
    current_user = request.user
    comment = Comment.objects.filter(coor_comm=current_user)
    mem_com = Member.objects.all()
    context = {
         'comment':comment,
         'mem_com':mem_com,
         
     } 
    return render(request, 'coordinators/past_display_comment.html', context)

@login_required(login_url='login')
@user_passes_test(check_role_pastorate)
def past_display_all_member(request):
    current_user = request.user
    member = Member.objects.filter(user=current_user).filter(status='1')
    # member = Member.objects.filter(team_lead=current_user).filter(status='1')

    return render(request, 'coordinators/past_display_all_member.html', {'member': member})

# @login_required(login_url='login')
# def coor_display_comment(request):
#     return render(request, 'coordinators/display_comment.html')


@login_required(login_url='login')
@user_passes_test(check_role_pastorate)
def past_new_comment(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.member = member
            comment.team_sup = request.user
            # comment.phone_number = UserProfile.phone_number
            comment.save()
            return redirect('past_display_comment')
   
    else:
        form = CommentForm()
    context = {
         'member':member,
         'form':form,   
     }
    return render(request, 'pastorate/past_new_comment.html', context)




# @login_required(login_url='login')
# @user_passes_test(check_role_pastorate)
# def my_team_member_list(request):
#     current_user = request.user
#     member = Member.objects.filter(team_lead=current_user)
#     context = {
#          'member':member,
#      } 
#     return render(request, 'pastorate/my_team_member_list.html', context)


# @login_required(login_url='login')
# @user_passes_test(check_role_pastorate)
# def my_team_member_comment(request):
#     current_user = request.user
#     member = Comment.objects.filter(coor_comm=current_user)
#     context = {
#          'member':member,
#      } 
#     return render(request, 'pastorate/my_team_member_comment.html', context)